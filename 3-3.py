import streamlit as st


st.title("화원고등학교 3-3을 위한 웹페이지")

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다.
tab1, tab2, tab3,tab4 = st.tabs(['오늘의 급식','생일 축하합니다', '학교 일정','입시 정보'])

with tab1:
    # tab A 를 누르면 표시될 내용
    st.write("")
    st.subheader('화원고등학교')
    st.markdown("7/16 오늘의 급식 메뉴 🤤")
    st.markdown(" ")
    st.markdown("기장밥, 맑은어묵국, 청경채맛살무침, 돈큐브스테이크, 배추김치, 요구르트")


with tab2:
    # tab B를 누르면 표시될 내용
    st.subheader('3학년 3반')
    st.markdown(':red[**생일 축하해요~~!!🎉**]')
    month = st.slider('월을 선택하세요.',1,12,step=1)
    st.success(''+str(month)+'월의 생일자는?')
    if month==1:
        st.write("16일 신정원")
        st.write("21일 곽승훈")
    elif month==2:
        st.write("1일 전혜진")
        st.write("5일 이지원")
        st.write("22일 김지수")
    elif month==3:
        st.write("2일 이지훈")
        st.write("14일 서정빈")
    elif month==4:
        st.write("10일 이수민")
        st.write("15일 이소윤")
    elif month==5:
        st.write("14일 조재영")
    elif month==6:
        st.write("23일 배기탁")
    elif month==7:
        st.write("4일 문지수")
        st.write("5일 정민경")
        st.write("26일 서상현")
        st.write("28일 유영재")
    elif month==8:
        st.write("3일 이민수")
        st.write("4일 김환희")
        st.write("13일 이동건")
        st.write("21일 오예승")
    elif month==9:
        st.write("28일 강민찬")
    elif month==10:
        st.write("16일 김윤휘")
    elif month==11:
        st.write("25일 장은빈")
        st.write("29일 박재환")
    elif month==12:
        st.write("27일 함아린")




    

with tab3:
    # tab B를 누르면 표시될 내용
    st.subheader('화원고등학교 학사 일정')
    st.write('7/19 방학식')

with tab4:
    st.title("대학 입시 정보")
    st.caption("3학년들 올해만 잘 버티자")
    option=st.selectbox('월별 입시 정보 선택',('7월','8월','9월','10월','11월','12월','1월','2월'))
    st.write('선택한 월: ',option)
    if option=="7월":
        st.markdown("7월의 입시 정보")
        st.write("으에에")
    elif option=="8월":
        st.markdown("8월의 입시 정보")
        st.write("방학축하")
    elif option=="9월":
        st.markdown("9월의 입시 정보")
        st.write("수시원서접수")
    elif option=="10월":
        st.markdown("10월의 입시 정보")
        st.write("10월의 어느 멋진 날에")
    elif option=="11월":
        st.markdown("11월의 입시 정보")
        st.write("수능")
    elif option=="12월":
        st.markdown("12월의 입시 정보")
        st.write("대학 면접")
    elif option=="1월":
        st.markdown("1월의 입시 정보")
        st.write("합격 결과")
    elif option=="2월":
        st.markdown("2월의 입시 정보")
        st.write("추가모집")

    tx=st.text_input("본인 스스로에게 해주고 싶은 응원의 말은?")
    if tx != '' :
        st.subheader(tx + '! 힘내자!')


