import streamlit as st
import random

# 1900년대 한국 근대문학 목록
BOOKS = [
    {
        "title": "무정",
        "author": "이광수",
        "year": 1917,
        "genre": "장편소설",
        "desc": "한국 최초의 근대 장편소설. 봉건적 구습과 근대적 자아 사이에서 갈등하는 청년의 이야기."
    },
    {
        "title": "운수 좋은 날",
        "author": "현진건",
        "year": 1924,
        "genre": "단편소설",
        "desc": "인력거꾼 김첨지의 비극적 하루를 통해 일제강점기 하층민의 삶을 사실적으로 그린 단편."
    },
    {
        "title": "감자",
        "author": "김동인",
        "year": 1925,
        "genre": "단편소설",
        "desc": "환경에 의해 타락해가는 여성 복녀의 이야기로, 자연주의 문학의 대표작."
    },
    {
        "title": "날개",
        "author": "이상",
        "year": 1936,
        "genre": "단편소설",
        "desc": "식민지 지식인의 내면 분열을 실험적 기법으로 그린 한국 모더니즘 문학의 정수."
    },
    {
        "title": "소나기",
        "author": "황순원",
        "year": 1953,
        "genre": "단편소설",
        "desc": "순수한 소년과 소녀의 짧은 만남과 이별을 서정적으로 담은 한국 단편문학의 명작."
    },
    {
        "title": "진달래꽃",
        "author": "김소월",
        "year": 1922,
        "genre": "시",
        "desc": "이별의 정한을 한국적 정서로 표현한 근대 시문학의 대표작."
    },
    {
        "title": "님의 침묵",
        "author": "한용운",
        "year": 1926,
        "genre": "시집",
        "desc": "불교적 사상과 민족적 저항의식을 담은 88편의 시를 수록한 시집."
    },
    {
        "title": "혈의 누",
        "author": "이인직",
        "year": 1906,
        "genre": "신소설",
        "desc": "한국 최초의 신소설. 청일전쟁을 배경으로 근대적 개화사상을 담은 작품."
    },
    {
        "title": "B사감과 러브레터",
        "author": "현진건",
        "year": 1925,
        "genre": "단편소설",
        "desc": "기숙사 사감의 위선과 억압된 욕망을 풍자적으로 그린 단편소설."
    },
    {
        "title": "태평천하",
        "author": "채만식",
        "year": 1938,
        "genre": "장편소설",
        "desc": "일제강점기 친일 부르주아 가족의 타락상을 풍자한 채만식의 대표작."
    },
    {
        "title": "레디메이드 인생",
        "author": "채만식",
        "year": 1934,
        "genre": "단편소설",
        "desc": "식민지 시대 실업 지식인의 고통을 날카로운 풍자로 그린 작품."
    },
    {
        "title": "동백꽃",
        "author": "김유정",
        "year": 1936,
        "genre": "단편소설",
        "desc": "토속적 배경 속 순박한 남녀의 사랑을 해학적으로 표현한 농촌 소설."
    },
    {
        "title": "봄봄",
        "author": "김유정",
        "year": 1935,
        "genre": "단편소설",
        "desc": "순박하고 우직한 데릴사위와 장인의 갈등을 해학과 웃음으로 풀어낸 명작."
    },
    {
        "title": "사랑손님과 어머니",
        "author": "주요섭",
        "year": 1935,
        "genre": "단편소설",
        "desc": "어린 소녀의 시선으로 바라본 어머니의 이루지 못한 사랑을 섬세하게 그린 작품."
    },
    {
        "title": "광염 소나타",
        "author": "김동인",
        "year": 1929,
        "genre": "단편소설",
        "desc": "예술지상주의를 극단적으로 추구하는 천재 음악가의 광기를 그린 작품."
    },
]

# 페이지 설정
st.set_page_config(
    page_title="한국 근대문학 추천",
    page_icon="📚",
    layout="centered"
)

st.title("📚 한국 근대문학 랜덤 추천")
st.caption("1900년대 ~ 1950년대 한국 근대문학 작품을 랜덤으로 추천해드립니다.")

st.divider()

if st.button("🎲 랜덤 추천받기", use_container_width=True, type="primary"):
    book = random.choice(BOOKS)
    st.subheader(f"『{book['title']}』")
    col1, col2, col3 = st.columns(3)
    col1.metric("작가", book["author"])
    col2.metric("발표연도", book["year"])
    col3.metric("장르", book["genre"])
    st.info(book["desc"])

st.divider()
st.caption(f"총 {len(BOOKS)}편의 작품이 등록되어 있습니다.")
