# ydp-python-team-project

영등포 Chat GPT와 함께하는 파이썬 코팅 팀 프로젝트

![Github페이지](./github-url-qrcode.png)

## 설치 방법

1. 리포지토리 클론하기

```bash
git clone https://github.com/hyperbora/ydp-python-team-project.git
```

2. python 가상환경 만들고 활성화

```bash
# 예시는 가상환경명이 myenv 이며 파이썬버전이 3.12.7 인 경우
# conda
conda create --name myenv python=3.12.7
conda activate myenv
```

```bash
# python env
python -m venv myenv
# myenv가 만들어진 폴더 이동 후 폴더 아래에서 명령어 실행
activate
```

3. 패키지 설치하기

```bash
pip install -r requirements.txt
```

4. vscode extension 설치하기

```bash
cat extensions.txt | xargs -L 1 code --install-extension
```

5. 프로그램 실행

```bash
python main.py
```

## 기술 스택

| 이름                                      | 설명                        |
| ----------------------------------------- | --------------------------- |
| [Kivy](https://kivy.org/)                 | 크로스플랫폼 GUI 프레임워크 |
| [SQLite](https://www.sqlite.org/)         | 데이터 베이스               |
| [SQLAlchemy](https://www.sqlalchemy.org/) | 데이터 베이스 ORM           |

## 폴더 구조

Project Root

```bash
├── .vscode
│ ├── extensions.txt          # vscode 확장파일 목록
│ └── settings.json           # vscode 프로젝트 설정
│
├── models/                   # 데이터와 데이터베이스 로직 (DB ORM 포함)
│   ├── __init__.py
│   └── *.py                  # 데이터 모델 등
│
├── views/                    # 사용자 인터페이스 레이아웃 및 화면
│   ├── __init__.py
│   └── *.kv                  # Kivy KV 언어로 작성된 뷰 레이아웃
│
├── viewmodels/               # UI와 Model을 연결하는 로직
│   ├── __init__.py
│   └── *.py                  # 화면에 대한 로직
│
├── services/                 # 앱 전체에서 사용할 비즈니스 로직 및 유틸리티
│   ├── __init__.py
│   ├── data_service.py       # 데이터 가져오기 및 저장하기 등
│   └── utils.py              # 공통으로 사용할 유틸리티
│
├── tests                     # 테스트 코드
│   └── *.py                  # 코드 테스트
├── main.py                   # 메인 파이썬 파일
├── README.md                 # 프로젝트 설명 파일
└── requirements.txt          # 필요 라이브러리 목록
```
