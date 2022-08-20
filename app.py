import streamlit as st
import wikipedia
import json
import requests
import streamlit as st
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import pandas as pd
import folium

KEY = "56d9570aefd64506abb385750f54d4cc"

def load_lottiefile(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)
    
    
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None 
    return r.json

lottie_hello = load_lottiefile("/Users/meetjethwa/Developer/Projects/Wiki_shorts/lottie_files/hello.json")
lottie_coding = load_lottiefile("/Users/meetjethwa/Developer/Projects/Wiki_shorts/lottie_files/coding.json")

st.title("Wiki Shorts")
st_lottie(
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",
    height = None,
    width=None,
    key=None
)
st_lottie(lottie_hello, key="hello")

def app():
    KEY = "56d9570aefd64506abb385750f54d4cc"
    st.title('Number Tracker')
    number = st.text_input('Phone Number with country code')
    if number:   
        meetNumber = phonenumbers.parse(number)
        yourLocation = geocoder.description_for_number(meetNumber, "en")
        serviceProvider = phonenumbers.parse(number)
        gecoder = OpenCageGeocode(KEY)
        query = str(yourLocation)
        results = gecoder.geocode(query)
        #print(results)
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        st.write(carrier.name_for_number(serviceProvider, "en"))
        st.write(yourLocation)
        m = folium.Map(location=[lat, lng], zoom_start=5)
        folium.Marker([lat,lng],popup=yourLocation).add_to((m))
        m.save("numberLocation.html")
        file = open("numberLocation.html", "r")
        components.html(file.read())
        
    else:
        st.write("Sorry Enter a valid phone number")
        
app()