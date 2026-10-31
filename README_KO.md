# Physics Chronicles — 원본 Python 브라우저 호환판

## 중요한 차이
이전 간소화 게임은 사용하지 않았습니다. `original_game.py`는 첨부하신 **해커은신처.py와 바이트 단위로 동일**합니다. 원본의 전투·라운드·패턴·설정·그래픽 생성 코드를 그대로 Python으로 실행합니다.

Tkinter 자체는 브라우저에 없으므로 `web_adapter.py`가 Tkinter의 화면·이미지·키 입력·전체화면·음악 연결을 대신합니다. Python은 Pyodide(WebAssembly)로 각 방문자의 브라우저에서 실행됩니다. 게임 전용 서버나 플레이어의 Python 설치는 필요 없습니다.

## GitHub 업로드
1. ZIP을 압축 해제합니다.
2. 아래 파일들을 `game3` 저장소의 **최상위**에 올려 기존 index.html을 교체합니다. 폴더째 올리지 마세요.
   - index.html
   - original_game.py
   - web_adapter.py
   - physics_chronicles.wav
   - .nojekyll (숨김 파일, 가능하면 포함)
3. Commit changes를 누릅니다.
4. Settings → Pages의 `main` / `/ (root)` 설정은 그대로 둡니다.
5. 배포 완료 후 Visit site로 열고 **게임 시작 / 음악 켜기**를 누릅니다.

기존 PhysicsChronicles_Streamlit 폴더가 남아 있어도 관계없지만, 실행 파일은 위 파일들입니다. Streamlit 설정이나 requirements.txt는 필요 없습니다.

## 사용 조건
- PC 키보드용. 첫 실행은 외부 CDN에서 Python 실행환경을 다운로드하므로 인터넷 연결과 로딩 시간이 필요합니다. 사용자가 직접 다운로드/설치하는 단계는 없습니다.
- 로컬에서 HTML을 더블클릭하는 방식은 Python 파일 읽기 보안 제한으로 동작하지 않을 수 있습니다. GitHub Pages에서 실행하세요.
- 외부 CDN 접속이 차단된 학교/회사망에서는 로딩이 안 될 수 있습니다.
- 최신 Chrome/Edge/Firefox 권장. 모바일 터치 조작은 추가하지 않았습니다.
- 브라우저의 자동재생 제한 때문에 시작 버튼 클릭 후 음악이 재생됩니다. M 설정의 음악 토글도 연결됩니다.
- 탭을 벗어나면 일시정지됩니다. 새로고침하면 진행이 초기화됩니다.

## 보존과 호환성 범위
- 원본 Python 파일: 수정 없음.
- 라운드·물리·공격·보스·상점·축복·스탯·설정·플레이어 픽셀 생성: 원본 로직 사용.
- 원본 _fixed_update를 60Hz 누산기로 호출합니다. 데스크톱 Tk 예약 콜백은 웹 requestAnimationFrame으로 대체했습니다.
- Tkinter 도형·태그·배경 이동·이미지 명령을 HTML Canvas로 연결합니다.
- 운영체제 창/오디오 기능은 브라우저 전체화면과 WAV 반복 재생으로 연결합니다.
- 선의 스무딩, stipple 패턴 투명도, 글꼴/글자 폭, 호의 테두리 등은 HTML Canvas와 Tkinter의 차이로 완전히 동일하지 않을 수 있습니다. 게임 데이터는 바꾸지 않았지만 화면의 픽셀 단위 동일성이나 동일 성능은 보장하지 않습니다.
- 대량 도형을 Python에서 Canvas로 전달하므로 기기에 따라 데스크톱 원본보다 느릴 수 있습니다.

## 검증
제공된 원본과 SHA-256 동일성, Python 구문, JavaScript 구문, 원본 초기화 및 프레임 진행/24라운드 화면 생성의 로컬 호환층 테스트를 수행합니다. 실제 브라우저/Pyodide 및 GitHub 배포 플레이 테스트는 수행하지 못했습니다. 웹 호환판이므로 첫 실행 시 오류가 있으면 페이지 하단 오류 문구를 보내주세요.
