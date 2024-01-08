import streamlit as st

chat_msg = st.chat_message("user")
chat_msg.write("这是一个聊天框~")
chat_msg.markdown(''':red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in] :gray[pretty] :rainbow[colors].''')

container = chat_msg.container(border=True)
container.markdown("Here's a bouquet &mdash; :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
container.write("这个容器在聊天框里面吗？")

st.write("这个消息在聊天框外面吗？")
