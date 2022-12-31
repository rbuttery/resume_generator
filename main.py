import streamlit as st
# st.set_page_config(layout="wide")

st.set_page_config(
    page_title="Resume Builder",
    # layout="wide",
    initial_sidebar_state="expanded",
    page_icon='📄'
)

# Page title
st.markdown("""
<html>
<head>
  <style>
    h1 {
      font-size: 36px;
      font-weight: bold;
      text-align: center;
      margin: 0;
    }
    h2 {
      font-size: 20px;
      font-weight: normal;
      text-align: center;
      margin: 0;
    }
    p {
      font-size: 16px;
      font-weight: normal;
      text-align: center;
      margin: 0;
    }
    .title {
      padding-bottom: 10px;
    }
  </style>
</head>
<body>
  <div class="title">
    <h1>AI-Assisted Resume & Cover Letter<br><br></h1>
  </div>
</body>
</html>""", unsafe_allow_html=True)

html_buttons = """
<html>
  <head>
    <style>
      .column {
        width: 50%;
        float: left;
        text-align: center;
      }
      .button {
        display: inline-block;
        padding: 15px 25px;
        font-size: 38px;
        cursor: pointer;
        text-align: center;
        text-decoration: none;
        outline: none;
        color: #fff;
        background-color: #FF534C;
        border: none;
        border-radius: 15px;
      }
      

      .button:hover {
        background-color: #FFCBC9;
      }
    </style>
  </head>
  
  <body>
    <div class="column">
      <a href="http://www.example.com" target="_blank" class="button" style="color: #ffffff";>Resumes</a>
    </div>
    <div class="column">
      <a href="http://www.example.com" target="_blank" class="button" style="color: #ffffff";>Cover Letters</a>
    </div>
  </body>

"""

with st.sidebar:
  st.markdown("""<a href="https://beta.openai.com/docs/introduction" style="color: #191919;">Build your own OpenAI Models</a>""", unsafe_allow_html=True)

col1, col2, col3= st.columns([1.5, 0.1, 1.5])

with col1:
    with st.container():
      st.markdown("<p>Get assistance from a model that is trained on creating ATS-friendly Resumes and Cover Letters.<br><br>Maintain as much creative freedom as you like, <i>but its no longer necessary.</i><br><br><br>", unsafe_allow_html=True)
    
with col2:
    # This just creates a space between the two columns
    with st.container():
        pass


with col3:
    with st.container():
        # st.image('https://i.imgur.com/XHnIEZE.png')
        pass

with st.container():
  st.markdown(html_buttons, unsafe_allow_html=True)