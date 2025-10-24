import streamlit as st

st.title("出演バンド選考・演奏順管理")

st.write("ここでは出演バンドの選考や演奏順を管理できます。")

# 仮のUI例
st.subheader("出演バンド一覧")
bands = ["SoundEnergy", "EchoWave", "Midnight Cats", "Rising Sun"]
selected = st.multiselect("出演バンドを選択", bands)

if selected:
    st.write("選ばれたバンド：", selected)

st.subheader("演奏順設定")
order = st.number_input("演奏順（1〜）", min_value=1, max_value=len(bands))
st.write(f"設定された演奏順: {order}")
