import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정 및 제목
st.set_page_config(page_title="문학 해설 챗봇", page_icon="📚")
st.title("📚 문학 해설 AI 챗봇")
st.subheader("시, 소설 등 어떤 문학 작품이든 물어보세요!")

# 2. Streamlit Secrets에서 API 키 불러오기 및 설정
try:
    # Secrets에 저장된 키 이름을 사용합니다.
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except KeyError:
    st.error("⚠️ Streamlit Secrets에 'GEMINI_API_KEY'가 설정되지 않았습니다. 대시보드 설정을 확인해주세요.")
    st.stop()

# 3. 세션 상태(Session State)로 채팅 기록 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "안녕하세요! 저는 문학 해설을 도와주는 AI 비서입니다. 궁금한 작품, 작가, 또는 특정 구절에 대해 질문해주세요! (예: 윤동주의 '서시' 해설해줘)"
        }
    ]

# 4. 기존 채팅 기록 화면에 출력
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 5. 사용자 입력 받기
if user_input := st.chat_input("질문을 입력하세요..."):
    # 사용자 메시지를 화면에 출력 및 세션에 저장
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # AI 응답 생성 과정 (오류 처리 포함)
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        with st.spinner("문학 작품을 분석 중입니다..."):
            try:
                # gemini-2.5-flash-lite 모델 로드
                # 페르소나 부여를 위해 system_instruction 추가
                model = genai.GenerativeModel(
                    model_name="gemini-2.5-flash-lite",
                    system_instruction="당신은 깊이 있고 친절한 문학 평론가이자 해설가입니다. 사용자가 묻는 문학 작품의 주제, 배경, 심상, 표현 기법 등을 쉽고 명확하게 설명해주세요."
                )
                
                # 이전 대화 맥락을 포함하여 API 호출 준비
                # Gemini의 대화 형식(user, model)에 맞게 이전 메시지 변환
                history = []
                for msg in st.session_state.messages[:-1]: # 방금 넣은 user_input 제외
                    role = "user" if msg["role"] == "user" else "model"
                    history.append({"role": role, "parts": [msg["content"]]})
                
                # 대화 시작 및 메시지 전송
                chat = model.start_chat(history=history)
                response = chat.send_message(user_input)
                
                # 결과 출력 및 저장
                ai_response = response.text
                response_placeholder.write(ai_response)
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
                
            except Exception as e:
                error_msg = f"❌ API 호출 중 오류가 발생했습니다: {str(e)}"
                response_placeholder.error(error_msg)
