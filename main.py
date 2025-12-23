import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# Page setup
st.set_page_config(
    page_title= 'Great.Portfolio',
    page_icon= ':raising_hand_man:',
    layout= 'wide'
)

#assets
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)
local_css("pages/Style/style.css")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_anim1 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_anim2 = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_u25cckyh.json")
image = Image.open("pages/OIP.webp")


# Slidebar
st.sidebar.title("Info")
url1 = "https://www.linkedin.com/in/chijioke-great-17868a315/"
url2 = "https://github.com/GreatChijioke-01"
st.sidebar.write(f"[Linkedin]({url1}):briefcase:")
st.sidebar.write(f"[Github]({url2}) :hammer_and_wrench:")
with open("pages/Great_Chijioke_CV.pdf", "rb") as file:
    btn = st.sidebar.download_button(label=":page_facing_up: Download My CV", data= file, file_name= "Great_Chijioke_CV.pdf", mime= "application/pdf")

#  Intro
st.write("##")
st.subheader("Hello :wave:")
st.title("I'm Great Chijioke")
st.write("Software devolopment | AI and Machine learning | Computing")

st.divider()

#Option menu
with st.container():
    selected = option_menu(
        menu_title= None,
        options = ['About','Projects', "Contact"],
        icons = ['person','code-slash', 'chat-left-text-fill'],
        orientation = "horizontal",
        styles ={
            "container": {"padding": "0!important", "background-color": "#3B4056"},
            "nav-link-selected": {"background-color": "#0047AB"}
        }
    )
if selected == 'About':
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("Great Chijioke")
            st.write("A hardworking student who is passionate about Computing and IT who is currently studying for A-levels in Coundon court sixth form," \
            " aspiring to be potential participant in the future of digital innovations and computation, to solve the challenges and drawbacks faced by tech " \
            "industries all over the world both now and in future. Inspired by the huge transition into AI and machine learning, I look forward to become a " \
            "software engineer specialising in AI researching and model development")
            st.caption("Use the side-bar at the top left for more info...")
        with col2:
            st_lottie(lottie_anim1)

    st.divider()
    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("""
            Education
            -GCSE, Coundon Court (2024- 2025)
                         
                - Mathematics(H) Grade (8)
                         
                - Combined Science Grade (9)
                         
                - History Grade (7)
                         
                - Creative Imedia (D2)
                          
                - Geography Grade (6)
                         
                - English lang/lit Grade (5/6)   
            -A level, Coundon court(2025-till date)
                         
                -Mathematics
                         
                -Further Mathematics
                         
                -Computer science
                         
                -Physics
            """)
        with col4:
            st.subheader("""
            Experience
            - IT and Sales manager, The imaging professionals
            - Web Designer/Dev, Rccg Holy ghost zone Coventry(G2G).
            """)

if selected == 'Projects':
    with st.container():
        st.header("My projects")
        st.write("##")
        col5, col6 = st.columns((1,2))
        with col5:
            st.image(image)
        with col6:
            st.subheader("Portfolio website")
            st.write("Using Streamlit framework I built a fully functioning website with python programming language. ")
            url3 = "https://github.com/GreatChijioke-01/my-portfolio"
            st.markdown("[Visit Github Repo]({url3})")
            st.caption("Next project is loading....")

if selected == 'Contact':
    st.header("Get in touch!")
    st.write("##")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/chijiokegreat3@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here..." required></textarea>
        <button type="submit">Send Message</button>
    </form>
    """
    left_col, right_col = st.columns((2,1))
    with left_col:
        st.markdown(contact_form, unsafe_allow_html= True, )
    with right_col:
        st_lottie(lottie_anim2, height= 300)