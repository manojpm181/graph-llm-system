import streamlit as st
import time

# ================= IMPORTS =================
from utils.loader import load_data
from graph.build_graph import build_graph
from ui.graph_view import visualize_graph

from services.query_router import route_query
from services.guardrails import validate_query

from graph.graph_utils import extract_nodes_from_result

from llm.agent import agent_answer
from llm.llm_engine import ask_llm
from llm.prompt import build_prompt
from llm.explainer import explain_result

from auth.auth import create_users_table, register_user, login_user

# ================= CONFIG =================
st.set_page_config(layout="wide")
create_users_table()

# ================= GLOBAL CSS =================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #020617, #0f172a);
    color: #e2e8f0;
}
section[data-testid="stSidebar"] {
    background: #020617;
    border-right: 1px solid #1e293b;
}
h1 {
    color: #38bdf8 !important;
    text-align: center;
    text-shadow: 0px 0px 20px rgba(56,189,248,0.7);
}
.metric-card {
    background: rgba(30,41,59,0.6);
    padding: 15px;
    border-radius: 12px;
    text-align: center;
}
.chat-container {
    max-height: 70vh;
    overflow-y: auto;
}
.chat-user {
    background: linear-gradient(90deg, #3b82f6, #06b6d4);
    padding: 10px;
    border-radius: 10px;
    margin: 8px 0;
    color: white;
    text-align: right;
}
.chat-bot {
    background: rgba(30,41,59,0.7);
    padding: 10px;
    border-radius: 10px;
    margin: 8px 0;
}
.typing span {
    display: inline-block;
    width: 6px;
    height: 6px;
    margin: 2px;
    background: #38bdf8;
    border-radius: 50%;
    animation: blink 1.4s infinite both;
}
@keyframes blink {
    0% { opacity: .2; }
    20% { opacity: 1; }
    100% { opacity: .2; }
}
</style>
""", unsafe_allow_html=True)

# ================= AUTH SESSION =================
if "user" not in st.session_state:
    st.session_state.user = None

# ================= LOGIN UI =================
if st.session_state.user is None:

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("""
        <div style="
            background: rgba(30,41,59,0.7);
            padding: 30px;
            border-radius: 15px;
            backdrop-filter: blur(12px);
            box-shadow: 0px 0px 25px rgba(0,0,0,0.5);
        ">
        """, unsafe_allow_html=True)

        st.markdown("## 🔐 Welcome Back")
        st.caption("Login or create a new account")

        tab1, tab2 = st.tabs(["🚀 Login", "✨ Register"])

        # ===== LOGIN =====
        with tab1:
            email_login = st.text_input("📧 Email", key="login_email")
            password_login = st.text_input("🔑 Password", type="password", key="login_pass")

            if st.button("Login", use_container_width=True):
                if not email_login or not password_login:
                    st.warning("⚠️ Fill all fields")
                else:
                    user = login_user(email_login, password_login)

                    if user:
                        st.session_state.user = user[1]
                        st.success("✅ Login successful")
                        st.rerun()
                    else:
                        st.error("❌ Invalid email or password")

        # ===== REGISTER =====
        with tab2:
            username_reg = st.text_input("👤 Username", key="reg_username")
            email_reg = st.text_input("📧 Email", key="reg_email")
            password_reg = st.text_input("🔑 Password", type="password", key="reg_pass")

            if st.button("Create Account", use_container_width=True):
                if not username_reg or not email_reg or not password_reg:
                    st.warning("⚠️ All fields required")

                elif "@" not in email_reg:
                    st.warning("⚠️ Invalid email")

                elif len(password_reg) < 4:
                    st.warning("⚠️ Password too short")

                else:
                    success = register_user(username_reg, email_reg, password_reg)

                    if success:
                        st.success("✅ Account created! Please login.")
                    else:
                        st.error("❌ Email already exists")

        st.markdown("</div>", unsafe_allow_html=True)

    st.stop()

# ================= LOAD DATA =================
@st.cache_data
def get_data():
    return load_data()

df = get_data()

# ================= SIDEBAR =================
st.sidebar.title("⚙️ Filters")
st.sidebar.success(f"👤 {st.session_state.user}")

if st.sidebar.button("Logout"):
    st.session_state.user = None
    st.rerun()

customer_filter = st.sidebar.multiselect("Select Customers", df['soldtoparty'].unique())
product_filter = st.sidebar.multiselect("Select Products", df['material'].unique())

if customer_filter:
    df = df[df['soldtoparty'].isin(customer_filter)]

if product_filter:
    df = df[df['material'].isin(product_filter)]

# ================= GRAPH BUILD =================
G = build_graph(df)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Data Summary")
st.sidebar.write(f"Orders: {len(df)}")
st.sidebar.write(f"Customers: {df['soldtoparty'].nunique()}")
st.sidebar.write(f"Products: {df['material'].nunique()}")

# ================= HEADER =================
st.title("🚀 Order-to-Cash Intelligence System")

col1, col2, col3 = st.columns(3)
col1.metric("📦 Orders", len(df))
col2.metric("👥 Customers", df['soldtoparty'].nunique())
col3.metric("📦 Products", df['material'].nunique())

st.divider()

# ================= MAIN LAYOUT =================
left, right = st.columns([2, 1])

# ================= GRAPH VIEW =================
with left:
    st.subheader("📊 Graph View")

    colA, colB = st.columns(2)
    colA.metric("🔗 Nodes", len(G.nodes()))
    colB.metric("🔄 Relationships", len(G.edges()))

    highlight_nodes = st.session_state.get("highlight_nodes", None)

    html_file = visualize_graph(G, highlight_nodes)

    with open(html_file, "r", encoding="utf-8") as f:
        st.components.v1.html(f.read(), height=700)

# ================= CHAT =================
with right:
    st.subheader("💬 AI Assistant")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("Ask anything...")

    if user_input:
        st.session_state.chat_history.append(("user", user_input))

        if not validate_query(user_input):
            st.error("❌ Invalid query")

        else:
            route = route_query(user_input)

            typing_placeholder = st.empty()
            typing_placeholder.markdown("""
            <div class="chat-bot">
                <div class="typing">
                    <span></span><span></span><span></span>
                </div>
            </div>
            """, unsafe_allow_html=True)

            time.sleep(1)

            # ===== SQL ROUTE =====
            if route == "sql":
                schema = "orders(salesorder, soldtoparty, material)"
                response = agent_answer(user_input, schema)

                sql = response["sql"]
                df_result = response["result"]

                st.subheader("🧾 Generated SQL Query")
                st.code(sql.strip(), language="sql")

                if not isinstance(df_result, str) and df_result is not None:

                    st.subheader("📊 Results")
                    st.dataframe(df_result)

                    csv = df_result.to_csv(index=False).encode('utf-8')
                    st.download_button("⬇️ Download Results", csv, "results.csv")

                    try:
                        st.subheader("📈 Visualization")
                        st.bar_chart(df_result.set_index(df_result.columns[0]))
                    except:
                        pass

                    nodes = extract_nodes_from_result(df_result)
                    st.session_state["highlight_nodes"] = nodes

                    st.subheader("💡 AI Explanation")
                    explanation = explain_result(user_input, df_result)

                    placeholder = st.empty()
                    output = ""

                    for char in explanation:
                        output += char
                        placeholder.markdown(output)
                        time.sleep(0.01)

                if df_result is not None and len(df_result) > 0:
                    try:
                        top_row = df_result.iloc[0]
                        col1 = df_result.columns[0]
                        col2 = df_result.columns[1]

                        bot_response = f"📊 Top result: {col1} = {top_row[col1]}, {col2} = {top_row[col2]}"
                    except:
                        bot_response = f"📊 Found {len(df_result)} results."
                else:
                    bot_response = "⚠️ No results found."

            # ===== GRAPH ROUTE =====
            elif route == "graph":
                bot_response = "📊 Explore graph on left"

            # ===== LLM ROUTE =====
            else:
                prompt = build_prompt(user_input)
                bot_response = ask_llm(prompt)

            typing_placeholder.empty()
            st.session_state.chat_history.append(("bot", bot_response))

    # ===== CHAT DISPLAY =====
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    for role, msg in st.session_state.chat_history:
        if role == "user":
            st.markdown(f'<div class="chat-user">{msg}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-bot">{msg}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ================= AUTO SCROLL =================
st.markdown("""
<script>
var chat = window.parent.document.querySelector('.chat-container');
if(chat) { chat.scrollTop = chat.scrollHeight; }
</script>
""", unsafe_allow_html=True)