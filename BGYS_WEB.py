import streamlit as st
from PIL import Image

menu = st.sidebar.selectbox("목록", ["자기소개", "학교소개", "동아리소개", "디지털 교과서(정보보안)", "디지털 교과서(인공지능)"])

if menu == "자기소개":
    st.title("자기소개(박병관, 정윤석)")
    st.title("1. 박병관")
    st.write('저는 청구고등학교를 다니고 있는 2학년 박병관 입니다!')
    st.write('저의 생년월일은 2006년 7월 29일 입니다.')
    st.write('제가 제일 좋아하는 동물은 곰입니다!')
    image_gom = Image.open('gom.png')
    st.image(image_gom, caption='곰 일러스트')
    st.write('저의 꿈은 정보보안 전문가로 안철수님의 V3처럼 백신프로그램을')
    st.write('만들어서 약자들한테 배포해주는게 꿈입니다.')
    st.subheader("정보보안 전문가 관련 영상")
    st.video('https://youtu.be/arcynoCFVAA?si=V0ybZ75Lgh-vIoML')
    st.title("")
    st.title("2. 정윤석")
    st.write("안녕하십니까! 저는 현재 청구고등학교에 재학중인 2학년 정윤석 이라고 합니다.")
    st.write("저는 2006년 3월에 대구에서 태어났습니다.")
    st.write("저의 관심분야는 인공지능 관련 분야인데 사람이 아닌 물체가 사람처럼 생각하고 행동한다는 것이 흥미로워 이 분야로 선택하게 되었습니다.")
    st.write("저의 최종목표, 즉 꿈은 언제나 든든하고 힘이 되어줄 수 있는 인공지능을 만들어 도움이 필요한 모두에게 힘과 마음을 나누어 주는 것입니다:)")
    st.subheader("인공지능이 대중의 마음에 영향을 미친 사례")
    st.video("https://www.youtube.com/watch?v=aBpstYAPOWY")
    st.write("위에 영상은 '만약 세상을 떠난 가수가 다시 살아 돌아온다면 어떨까?' 라는 일이 실제로 일어난 영상입니다.")
    st.write("과거 케이블 TV의 한 음악방송에서 대중들이 그리워하는 가수의 목소리를 인공지능으로 재현해 무대에 선보이는 특집 방송이였는데, 많은 대중과 돌아가신 가수의 지인들과 동생이 눈물을 훔치고 추억을 회상하는 등 마음을 울리고 위로해주는 모습이 저의 기억속에 크게 남아 소개하게 되었습니다.")

elif menu == "학교소개":
    st.title("학교소개")
    image_cg1 = Image.open("cheonggu1.png")
    image_cg2 = Image.open("cheonggu2.png")
    st.image(image_cg1, caption="")
    st.image(image_cg2, caption="")
    st.subheader("청구고등학교")
    st.write("- 청구고등학교는 한국전쟁 후 황폐해진 국가를 재건하는 데 기여하기 위해 고아원을 세워 전쟁고아들을 돌보고 정규학교에 다닐 수 없던 빈곤층 자녀들을 교육시키기 위해 설립한 ‘덕화학원’에 뿌리를 두고 있습니다.")
    st.write("- 그 설립 취지를 이어받아 ‘청구고등학교’라는 교명과‘사랑의 실천(근면·정직·봉사)' 이라는 교훈을 기반으로 도덕인, 창조인, 자주인, 건강인을 교육목표로 현재까지 2만 1천여 명의 졸업생을 배출하였습니다.")
    st.write("- 청구고등학교는 1963년 12월 24일에 설립되었으며 2023년 기준 학생수는 703명 입니다.")
    st.write("- 대구광역시 동구 국채보상로 827에 위치하고 있고 \n대구 도시철도 1호선 신천역 5번 출구에서 남쪽으로 800m 거리에 위치하고 있습니다.")
    
elif menu == "동아리소개":
    st.title("동아리소개")
    st.write('- 동아리명 : 명예로운 열혈 C언어 프로그래밍\n')
    st.write('- 배우는 것 : C언어 프로그래밍 및 관련 공모전\n')
    st.write('- 했던 활동 : C언어 프로그래밍, Ai 챗봇 만들기, 아두이노를 활용한 무드등만들기, 각종 공모전, 드론 만들기 등 \n')
    image_club0 = Image.open("IMG_3079.jpg")
    st.image(image_club0, caption="")
    image_club1 = Image.open("IMG_3076.jpg")
    st.image(image_club1, caption="")

elif menu == "디지털 교과서(정보보안)":
    st.title("디지털 교과서(정보보안)")
    st.subheader('1. 정보보안이란? \n')
    st.write('중요한 엔터프라이즈 정보를 악용, 승인되지 않은 액세스, 중단 또는 파기로부터 보호하는 일련의 보안 절차와 도구를 뜻하며, 정보보안을 하기위해선 어느정도 해킹 기법을 알아야 대응할 수 있으므로 해킹 기법과 보안 방법을 간단히 소개하겠습니다.')
    image_sec1 = Image.open("2Q.png")
    st.image(image_sec1, caption="")
    st.subheader('2. 암호기술이란? \n')
    st.write('무결성 / 기밀성 / 부인 불가 / 인증 등의 정보 보호 목적 달성을 위해 사회 전 분야에서 광범위하게 이용되고 있다.\n')
    st.write('2-1. 무결성-> 데이터를 보호하고 늘 정상적인 데이터를 유지하는 것. \n')
    st.write('2-2. 기밀성 -> 인가된 사용자만이 정보에 접근할 수 있으며, 정보의 비밀이 유지 되어야 한다는 것. \n')
    st.write('2-3. 부인불가 -> 개인 정보 유출 방지 및 위변조 방지 기술, 개인 정보 수집 최소화 기술이 사용됨. \n')
    st.write('2-4. 인증 -> 프라이버시 보장 암호기술, 검증 암호 기술, 이중 방지 암호 기술, 보장 기술 등이 사용됨. \n')
    st.subheader('3. 여러가지 해킹기법')
    image_sec2 = Image.open("security.png")
    st.image(image_sec2, caption="")
    st.write('3-1. 전송차단 -> 송신 측에서 수신 측에 메시지를 전송할 때 제3자가 수신 측과 연결할 수 없도록 데이터 전송을 차단하는 것이다. \n')
    st.write('3-2. 가로채기 -> 송신 측과 수신 측이 데이터를 주고받는 사이에 제3자가 도청하는 것이다.\n')
    st.write('3-3. 변조 -> 송신 측에서 수신 측으로 전송할 데이터를 제3자가 가로채서 데이터의 일부 또는 전부를 변경하는 것이다. \n')
    st.write('3-4. 위조 -> 송신 측도 모르게 제3자가 수신 측에서 송신 측이 메시지를 전송하는 것처럼 위조한 후 수신 측에 전송하는 것이다. \n')
    st.write('3-5. 분산 서비스 거부 공격 (Ddos) -> 네트워크 상의 비정상적인 대규모 접속을 발생시켜 과부화를 유발, 시스템의 중요 자원을 완전히 점거 후 사용 불가능한 상태로 만드는 기법\n')
    st.write('3-6. 스니핑 공격(sniffing) -> 네트워크 중간에서 다른 사람의 패킷 정보를 도청하는 해킹 유형의 하나이고, 스니핑을 할 수 있도록 설치되는 도구를 스니퍼라고 하며, 스니핑 공격은'
             '수동적 공격이고 스니퍼를 설치한 이후에도 네트워크에 별다른 이상 현상을 일으키지 않기 때문에 능동적으로 탐지해야 발견할 수 있다.\n')
    st.write('3-7. 스푸핑 공격(spoofing) -> 패킷을 정당한 사용자가 보낸 것처럼 자기 자신의 정보를 속여 다른 대상 시스템을 공격하는 기법, 식별 정보를 위조함으로써 역추적을 어렵게 만듬.\n')
    st.write('3-8. 세션 하이재킹(session hijacking) -> 세션 가로채기로 서버와 클라이언트 사이의 로그인 상태를 가로채는 것을 말하며, 합법적인 절차를 통해 인증받은 사용자의 세션을 탈취하는 공격\n')
    st.write('3-9. 악성코드 -> 바이러스, 웜, 트로이 목마와 백도어, 스파이웨어 등이 있다.')
    st.write('3-10. 바이러스 -> 원시형, 암호형, 은폐형, 다형성, 매크로, 전자 메일 바이러스 등이 있고, 특정 파일을 감염시켜 그 파일이 원래의 기능을 못하게 하거나 변형,파괴하는 등의 피해를 줌. \n')
    st.write('3-11. 웜 -> 대량 메일형, 시스템 공격형, 네트워크 공격형 등이 있고, 자신을 복제하여 네트워크 연결을 통해 컴퓨터에서 컴퓨터로 전파되는 프로그램이다.\n')
    st.write('3-12. 트로이목마 -> 사용자가 의도하지 않은 악성 소프트웨어 프로그램을 화면 보호기와 같은 정상적인 프로그램에 삽입한 형태를 취하며, 제한없는 접근을 통해 내부의 정보를 공격자의 컴푸터로 유출하는 악성 코드이다.\n')
    st.write('3-13. 백도어-> 운영체제나 프로그램을 생성할 떄 정상적인 인증 과정을 거치지 않고, 운영체제나 프로그램 등에 접근할 수 있도록 만든 일종의 통로로 트랩 도어라고 한다. \n')
    st.write('3-14. 스파이웨어 -> 사용자의 동의 없이 컴푸터의 구성을 변경하거나 광고성 정보를 수집하고 악의적으로 빼내는 악성 코드이다.\n')
    st.subheader('4. 관리적,물리적,기술적 측면에서의 대응방법')
    image_resolve = Image.open("images.png")
    st.image(image_resolve, caption="")
    st.write('4-1. 관리적 측면 : 정책 관리, 컴퓨터 바이러스 관련 정보 수집, 복구 디스켓 준비 등.\n')
    st.write('4-2. 물리적 측면 : Pc 사용 제한, 출입 통제 등.\n')
    st.write('4-3. 기술적 측면 : 최신 버전 백신, 정품 SW 사용 등.\n')

elif menu == "디지털 교과서(인공지능)":
    st.title("디지털 교과서(인공지능)")
    st.subheader("1. 인공지능이란?")
    st.write("인공지능(AI: Artificial Intelligence)은 인간의 지능으로 수행할 수 있는 다양한 인식, 사고, 학습 활동 등을 기계가 할 수 있도록 구현하는 기술이자 그 기술을 연구하는 학문 분야를 말합니다.")
    image_AI = Image.open("AI.png")
    st.image(image_AI, caption="")
    st.subheader("2. 인공지능의 특성")
    st.write("2-1. 인간 같은 행동")
    st.write("- 초기에 인공지능을 연구한 학자들은 사람의 언어로 대화하고 시각 장치를 통해 물체를 인식하고 문제해결을 위해 스스로 계획을 세워 실천하는 로봇이 인간 같은 행동이라고 정의하였습니다. 인간 같은 행동을 최초로 주장한 앨런 튜링은 튜링 테스트를 통과하면 인간과 같은 기계임이 증면된다고 하였지만 인간이 어떻게 생각하고 판단하고 행동하는가를 정의하는 것은 어렵기 떄문에 지금까지 튜링 테스트를 통과한 인공지능은 없습니다.")
    st.write("2-2. 인간 같은 사고")
    st.write("- 사람의 지능이 인공지능보다 우수하기 때문에 인간의 지능을 기계로 구현해야 한다고 생각하는 학자들이 생겨 인공지능의 판단 과정에 인간같은 사고가 생기게 되었습니다. 그리고 이러한 특성에 집중한 학자들은 사람들의 인지 과정과 마음을 연구하는 신경 과학과 심리학의 연구 결과를 바탕으로 계산 모델도 새롭게 만들어지게 되었습니다.")
    st.write("2-3. 합리적 행동")
    st.write("- 인간이 어떻게 행동울 하고 사고를 하는지 아는것은 어려웠고 그것을 인공지능으로 구현하는 것은 더 어려웠기 때문에 이것을 고민하지 말고 합리적으로 행동하는 기계를 만들자고 주장하는 학자들이 등장하면서 합리적 행동이라는 특성이 생기게 되었습니다.")
    st.write("2-4. 합리적 사고")
    st.write("- 합리적인 행동을 가능하도록 하기 위해 삼단 논법처럼 올바른 전제가 주어지면 항상 옳은 결과를 내도록 합리적 사고에 집중하는 학자들이 생겨났고 그로 인해 합리적 사고라는 개념이 생겨났지만 이 세상의 현상, 이론, 감정들은 무엇이 옳은지 판단하기 어렵고 복잡하기 때문에 인공지능에 적용하기는 쉽지 않았습니다.")