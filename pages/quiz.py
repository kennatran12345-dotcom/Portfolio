import streamlit as st

st.header("What's your house-pet spirit animal? 🐾")

 #new         
option1=st.selectbox("Pick a season:",("spring","summer","fall","winter"))
st.write("You picked:", option1)
        
option2=st.selectbox("What's your personality type?",("extra","lowkey","chill","contetxt-dependent"),)
st.write("You picked:",option2)

#new
num1=st.number_input("How clingy are you? (pick 0-10)",min_value=0,max_value=10,step=1)
st.write("Clingy level:",num1)

num2=st.number_input("How energetic are you feeling? (pick 0-10)",min_value=0,max_value=10,step=1)
st.write("Energy level:",num2)

option3=st.selectbox("What's your ideal night?",("movies","beach walk","getting work done","sleeping"),)
st.write("You picked:",option3)

#new
sleep=st.slider("How many hours of sleep do you get?",min_value=0,max_value=24,step=1)

"CLICK RESULT!"==True
#new
if st.button("CLICK RESULT!")==True:
    st.header("Results 👀")
    #new
    st.audio("audio/freesound_community-tada-fanfare-a-6313.mp3", format="audio/mp3")
    #new
    st.balloons()

    dogscore=0
    catscore=0

    total=dogscore+catscore
    if option1=="spring"  or option1=="summer":
        dogscore+=1
    elif option1=="fall" or option1=="winter":
        catscore+=1
    total=dogscore+catscore


    if option2=="extra"  or option2=="context-dependent":
        dogscore+=1
    elif option2=="lowkey" or option2=="chill":
        catscore+=1
    total=dogscore+catscore
    
    if num1>5:
        dogscore+=1
    elif num1<5:
        catscore+=1
    else:
        dogscore+=0
        catscore+=0
    total=dogscore+catscore

    if num2>5:
        dogscore+=1
    elif num2<5:
        catscore+=1
    else:
        dogscore+=0
        catscore+=0
    total=dogscore+catscore


    if option3=="movies"  or option3=="beach walk":
        dogscore+=1
    elif option3=="getting work done" or option3=="sleeping":
        catscore+=1
    total=dogscore+catscore


    if 0<=sleep<=11:
        dogscore+=1
    elif 12<sleep<=24:
        catscore+=1
    else:
        dogscore+=0
        catscore+=0
    total=dogscore+catscore


    if dogscore>catscore:
        st.write("YOU ARE A DAWG 🐶")
        st.image("Images/Imagedog.jpg")
    elif catscore>dogscore:
        st.write("you are a cat 😼")
        st.image("Images/cat.jpg")
    else:
        st.write("You are a hamster 🐹")
        st.image("Images/hamster.jpg")
