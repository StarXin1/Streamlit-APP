import streamlit as st

chat_msg = st.chat_message("user")
chat_msg.write("这是一个聊天框~")
chat_msg.markdown(''':red[Streamlit] :orange[可以] :green[生成] :blue[各种] :violet[颜色] :gray[的] :rainbow[文本].''')

container = chat_msg.container(border=True)
container.markdown("这有一束花 &mdash; :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
container.write("这个容器在聊天框里面吗？")

st.write("这个消息在聊天框外面吗？")

if st.button("语音交流"):
  st.write("按钮名字改变")
