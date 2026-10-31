from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Physics Chronicles", page_icon="⚔️", layout="wide")
st.title("Physics Chronicles")
st.caption("게임 화면을 클릭한 뒤 조작하세요 · ← → 이동 · C 점프 · X 검 · Z 대시 · Q 기술 · ↑ 다음 방 · R 재시작")
components.html(Path(__file__).with_name("game.html").read_text(encoding="utf-8"), height=680, scrolling=False)
with st.expander("실행 안내"):
    st.write("PC 키보드용 게임입니다. 화면을 클릭해 키보드 포커스를 맞춰 주세요. 새로고침하면 진행 상황이 초기화됩니다.")
    st.write("세 시대의 일반 방과 보스 방을 차례로 클리어하세요. 적이 모두 사라지면 오른쪽 문에서 ↑를 누르면 됩니다.")
