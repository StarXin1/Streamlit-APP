import streamlit as st

chat_msg = st.chat_message("user")
chat_msg.write("这是一个聊天框~")

container = chat_msg.container()
container.write("这个容器在聊条框里面吗？")
