import streamlit as st
import openai

def generate_content(prompt: str) -> str:
    # Open the API key file
#     with open(r".\secret.txt", "r") as f:
#         openai.api_key = f.read()
    openai.api_key = st.secrets["API_KEY"]
    # Generate the content
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=750,
        n=1,
        stop=None,
        temperature=0.9,
    )
    return completions.choices[0].text

col1, col2 = st.columns([2, 4])

with st.sidebar:

    # Create a blank dictionary to store user data
    user_data = {}

    # Set the title
    st.title("Resume Builder")

    # Get user's name
    name = st.text_input("Name")

    # Get user's email
    email = st.text_input("Email")

    # Get user's contact info
    contact = st.text_input("Contact Number")
    
    # Get user's location
    location = st.text_input("Location")
    
    # Get user's education
    education = st.text_input("Education")
    
    # Get user's experience
    experience = st.text_input("Experience")
    
    # Get user's skills
    skills = st.text_input("Skills")
    
    # Add user data to the dictionary
    user_data['name'] = name
    user_data['email'] = email
    user_data['contact'] = contact
    user_data['location'] = location
    user_data['education'] = education
    user_data['experience'] = experience
    user_data['skills'] = skills

    generate_resume = st.button("Generate Resume")

# Render the resume
if generate_resume:
    
    # Name and contact info
    st.markdown(f"<h1 style='text-align: center; color: black;'>{user_data['name']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: black;'>{user_data['email']} || {user_data['contact']} || {user_data['location']}</p>", unsafe_allow_html=True)
    
    # Summary
    st.markdown(f"<h3 style='text-align: left; color: black;'>Summary</h3>", unsafe_allow_html=True)
            ###### AI PROMPT ######
    ai_summary = generate_content(prompt=f'Create a professional summary in 80 words or less, embelish on their abilities & use flowery language, make it 1st person, do not mention contact details, only using this data: {user_data}. ')
    st.markdown(f"<p style='text-align: left; color: black;'>{ai_summary}</p>", unsafe_allow_html=True)
    
    # Experience
    st.markdown(f"<h3 style='text-align: left; color: black;'>Experience</h3>", unsafe_allow_html=True)
    ai_experience = generate_content(prompt=f'Neatly format their experience where the duties are summarized into a bullet point list, embelish on their duties & use flowery language, make it 1st person, make it past tense, do not mention contact details, only using this data: {user_data}. ')
    st.markdown(f"<p style='text-align: left; color: black;'>{ai_experience}</p>", unsafe_allow_html=True)
    
    # Education
    st.markdown(f"<h3 style='text-align: left; color: black;'>Education</h3>", unsafe_allow_html=True)
    # ai_education = generate_content(prompt='')
    st.markdown(f"<p style='text-align: left; color: black;'>{user_data['education']}</p>", unsafe_allow_html=True)
    
    # Skills
    st.markdown(f"<h3 style='text-align: left; color: black;'>Skills</h3>", unsafe_allow_html=True)
    ai_skills = generate_content(prompt=f'Create a bullet-point list of skills, embelish on their skills & use flowery language, make it 1st person, only using this data: {user_data}.')
    st.markdown(f"<p style='text-align: left; color: black;'>{ai_skills}</p>", unsafe_allow_html=True)
    
    # References
    st.markdown(f"<h3 style='text-align: left; color: black;'>References</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: left; color: black;'>Excellent character & professional references available upon request.</p>", unsafe_allow_html=True)

        
