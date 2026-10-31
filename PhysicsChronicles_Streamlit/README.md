# Physics Chronicles — Streamlit 웹 버전

Tkinter 원본의 콘셉트를 바탕으로 재구현한 경량 웹 프로토타입입니다.
**Python/Streamlit은 웹페이지를 제공하며, 실제 게임은 브라우저의 JavaScript Canvas로 실행됩니다.** Tkinter 원본 자체를 Streamlit에서 실행하는 방식이 아닙니다.

## GitHub → Streamlit Community Cloud
1. 이 ZIP을 압축 해제합니다.
2. GitHub에 새 저장소를 만듭니다.
3. `app.py`, `game.html`, `requirements.txt`, `README.md`를 **저장소 최상위**에 업로드합니다. ZIP 자체를 올리지 마세요.
4. Streamlit Community Cloud에서 GitHub 계정으로 로그인하고 앱 생성을 선택합니다.
5. 해당 저장소, 실제 사용하는 브랜치(보통 main), 실행 파일 `app.py`를 지정해 배포합니다.
6. 앱에서 게임 화면을 클릭한 뒤 키보드로 플레이합니다.

Community Cloud의 메뉴 명칭은 변경될 수 있습니다. Python 버전 선택 항목이 있으면 Python 3.11 또는 3.12를 권장합니다.

## 로컬 실행
```bash
pip install -r requirements.txt
streamlit run app.py
```
VS Code 터미널에서도 위 명령을 사용합니다. `python app.py`가 아니라 `streamlit run app.py`입니다.

## 조작
← → / A D 이동 · C 더블점프 · ↓+C 발판 통과 · X 검 · Z 대시 · Q 기술 · ↑ 문 진입.
상점은 1/2/3 구매, Enter 또는 ↑ 다음 시대. 사망·엔딩 후 R 재시작.
화면을 벗어나면 입력이 해제되며 일시정지됩니다. 다시 클릭해 주세요.

## 구성과 제한
- 세 시대별 일반 방 + 보스 방, 총 6개 전투방.
- 체력·동전·대시·검·특수 범위 공격·강화 상점.
- 원작의 24라운드·총·패링·사냥돌진·음악·배 연출은 제외했습니다.
- Q 기술은 시대별 이름과 피해량을 달리한 간소화 범위 공격입니다. 원본의 물리 기술을 모두 재현하지 않습니다.
- PC 키보드용. 모바일 터치 조작은 지원하지 않습니다.
- 진행 상태는 브라우저 메모리에만 있으며 새로고침하면 초기화됩니다.
- 별도 그림·음악·API 키·게임 서버가 필요 없습니다.

## 검증
Python 구문 검사, JavaScript 구문 검사, 핵심 점프/바닥 로직 모의 테스트를 수행했습니다.
실제 Streamlit Cloud 배포 및 브라우저 플레이 테스트는 수행하지 못했습니다.
