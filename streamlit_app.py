import streamlit as st

chat_msg = st.chat_message("user")
chat_msg.write("这是一个聊天框~")

container = chat_msg.container(border=True)
container.markdown("这是一条markdown消息")
container.write("这个容器在聊天框里面吗？")

st.write("这个消息在聊天框外面吗？")
