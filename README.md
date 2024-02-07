# 수정 필요 부분
- 프로젝트의 목적: 프로젝트에 맞춰서 적기
- 팀원 소개: 팀원들의 깃허브 주소 공유하기
- 테스트 준비 및 방법: git clone에 각자의 repo 주소 적기
- 데모페이지: 총 완성된 스트림릿 페이지 적기
- 주요 메서드 설명 추가
- 완성된 발표자료 pdf 파일 추가

# 프로젝트의 목적
- 본 프로젝트는 부동산 데이터를 활용하여 대시보드를 개발하는 목적은 부동산 시장 동향을 시각화하고 사용자에게 부동산 투자 결정을 돕기 위함입니다. 이를 통해 사용자는 지역별 가격 변동, 투자 수익률 예측 및 부동산 시장의 트렌드를 쉽게 파악하고 최적의 부동산 투자 전략을 수립할 수 있도록 도와주기 위함입니다.

## 팀원 소개
- 나한울 팀장 : 깃허브 주소 공유
- 김영환 팀원 : 깃허브 주소 공유
- 양인선 팀원 : 깃허브 주소 공유
- 이상훈 팀원 : 깃허브 주소 공유
- 정소영 팀원 : 깃허브 주소 공유
- 황유진 팀원 : 깃허브 주소 공유



# 본 프로젝트에서 사용한 주요 개발환경 요약  (예시)
  + Programming Languages : Python(ver. 3.12.1)
  + Web Framework : Streamlit (ver. 1.31.0)

## 주요 라이브러리 버전
  + [requirements.txt](requirements.txt) 파일 참조

## 테스트 준비 및 방법
- 원격 저장소의 주소를 복사한 다음 로컬 환경에 복제합니다.

```bash
git clone "본인의 원격저장소 주소를 입력하시오"   #수정 필요
```

- 폴더 최상위 경로에서 가상환경을 설치합니다.

```bash
pip install virtualenv #기존에 설치한 가상환경이 있다면 생략 가능
virtualenv venv
```

- 가상환경에 접속합니다.
```bash
source venv/Scripts/activate
```

- 라이브러리를 설치합니다.
```bash
pip install -r requirements.txt
```

- 일반적인 파이썬 `.py` 파일을 실행할 경우
```bash
python a.py
```

- Streamlit 파일 `.py` 파일을 실행할 경우
```bash
streamlit run app.py
```

# 데모페이지
- Streamlit에서 구현한 Demo는 다음과 같습니다.
  + https://app-api-qkxzk2zdlacnuwxcqwxyyq.streamlit.app/

 ## 주요 기능
 - 본 프로젝트에서 자체 개발 및 활용한 주요 메서드는 다음과 같습니다.

| Functions | Location | Description |
|---|---|---|
| main | app.py  | for deploy |
| load_api | data_collect.py | for collecting data from API |

### main()
- main 함수는 ~~~
```python
def main():
   # 코드 설명
```
- 결과 이미지가 있으면 표시 

### data_collect()
-  data_collect() 함수는 ~~~~


## 코드 에러 문의 
- 메뉴 `Issues`-`New Issues`-`메모 남기기`-`Submit new issue`


# 발표자료 PDF 
- 공모전에서 입상한 발표자료 PDF는 아래와 같습니다.
  + [00발표자료_2024](portfolio.pdf)


## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)