# ydp-python-team-project

영등포 Chat GPT와 함께하는 파이썬 코팅 팀 프로젝트

![이미지 설명](./github-url-qrcode.png)

## 설치 방법

1. 리포지토리 클론하기

```bash
git clone https://github.com/hyperbora/ydp-python-team-project.git
```

2. python 가상환경 만들고 활성화, 비활성화

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
| [SQLAlchemy](https://www.sqlalchemy.org/) | 데이터 베이스 ORM           |
