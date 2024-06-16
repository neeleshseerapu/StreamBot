import streamlit as st
import google.generativeai as genai

API_KEY = st.secrets["API_KEY"]

genai.configure(
    api_key=API_KEY
)

model = genai.GenerativeModel('gemini-pro')

info = '''
At R&D Auto Repair, we use cutting-edge technology and industry best practices to provide high-quality services to our customers.
Established in 2014, R&D Auto Repair has been a family-owned and operated business for over 5 years. 
We offer complete auto repairs on most car models. We offer repair services that keep your vehicle running as it should, no matter what condition you bring it in.
Rey, R&D's repair expert, has over 10 years of experience working with various cars. He's extremely knowledgeable and is quick with his work.
The best part is that his prices are incredibly fair, and he's willing to work with your budget!
4.9 Rating on Yelp for reliable and efficient repairs.

Services:
Auto Diagnosis or Inspection
Auto Maintenance
Auto Mirror Replacement
Auto Noise Diagnosis
Auto Repairs
Check Engine Light
Oil Changes
Tire Pressure Monitoring System Diagnosis
Auto Electronics Installation
Auto Window Replacement
Window Tinting
Auto General Diagnosis
Auto Mirror Repair
Auto No-Start Diagnosis
Auto Pre-Purchase Inspection
Auto Vibration Diagnosis
Engine Oil Light Diagnosis
Routine Automotive Maintenance
Transmission Leak Inspection
Auto Window Repair
Auto Windshield Replacement

Hours: 
Saturday	8:30 AM - 5:30 PM
Sunday	Closed
Monday	9 AM - 7 PM
Tuesday	9 AM - 7 PM
Wednesday	9 AM - 7 PM
Thursday	9 AM - 7 PM
Friday  9 AM - 7 PM

Adress: 1567 Laurelwood Rd, Santa Clara, CA
Phone: 408-728-5517
'''

initial_instruction = f'''
You are a chatbot named Rey.Ai that handles questions for a business called R&D Auto Repair.
Always use a friendly tone and answer questions as accurately as possible.
Do not make up fake information or answer unrelated questions. 
If you do not know an answer to a question, tell the user you don't know and ask them to contact this phone number: (408-728-5517)
Here is information regarding the business: {info}
'''

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

st.title("R&D Auto Chat Bot")

def role_to_streamlit(role):
    if role == 'model':
        return 'assistant'
    else:
        return role
    
first_resp = st.session_state.chat.send_message(initial_instruction+"\nNow greet the user briefly, and ask them what they need help with.")


for message in st.session_state.chat.history:
    if message.parts[0].text == initial_instruction+"\nNow greet the user briefly, and ask them what they need help with.":
        pass
    else:
        with st.chat_message(role_to_streamlit(message.role)):
            st.markdown(message.parts[0].text)

if prompt := st.chat_input("What can I do for you?"):
    st.chat_message("user").markdown(prompt)
    response = st.session_state.chat.send_message(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)
# streamlit run streambot.py
