import streamlit as st
import speech_recognition as sr

st.title("Speech vs Manual Accuracy checker")

col1 , col2 = st.columns(2)

with col1:
    st.subheader("Box 1: Mic Text")
    audio_value = st.audio_input("Recording audio")
    recognized_text = ""
    if audio_value is not None:
        recognizer = sr.Recognizer()
        with open("audio.wav","wb") as f:
            f.write(audio_value.getvalue())
        
        with sr.AudioFile("audio.wav") as source:
            audio_data = recognizer.record(source)
            
        recognized_text = recognizer.recognize_google(audio_data)
        st.success("Audio Converted!")
    
    mic_text = st.text_area("Your recorded audio : ", value=recognized_text)
    for_mic = mic_text.lower().replace(".","").split()
    
with col2:
    st.subheader("Box 2: Manual Text")
    manual_text = st.text_area("Enter your text here : ")
    for_manual = manual_text.lower().replace(".","").split()
    
match_count = 0
if st.button("Check Accuracy"):
    if len(for_manual)>0:
        for word in for_manual:
            if word in for_mic:
                match_count +=1
        accuracy = ((match_count/len(for_manual))*100)
        st.write(f"Words in Mic Text are : {len(for_mic)}")
        st.write(f"Words in Manual Text are : {len(for_manual)}")
        st.write(f"The accuracy of {match_count}/{len(for_manual)} is {accuracy:.2f}%")

    else:
        st.warning("Please enter text into 'Box 2' to find currect accuracy.")