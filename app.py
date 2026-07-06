
import streamlit as st, json
st.set_page_config(page_title="Shafi Values",layout="wide")
st.title("🍎 Shafi Values")
st.caption("Blox Fruits Trading Values")

with open("data.json") as f:
    data=json.load(f)

q=st.text_input("Search")
tab=st.radio("Category",["Normal Fruits","Limiteds","Gamepasses"])

key={"Normal Fruits":"normal","Limiteds":"limited","Gamepasses":"gamepasses"}[tab]
rows=data[key]
if q:
    rows=[r for r in rows if q.lower() in r["name"].lower()]
st.dataframe(rows,use_container_width=True)
