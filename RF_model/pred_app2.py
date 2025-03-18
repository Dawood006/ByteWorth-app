import pickle
import numpy as np
import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import joblib

model_path = "/mount/src/laptop-price-benchmark-app/RF_model/laptop_randomf_model.pkl"
with open(model_path, "rb") as file:
    model = joblib.load(file)  # Use joblib instead of pickle


#Styling
st.markdown(
    '''
    
    <style>
    .main { background-color: #002147; } /* Deep Royal Blue */
    h1 { color: #FFD700; text-align: center; } /* Gold */
    .stSelectbox label, .stCheckbox label, .stNumberInput label { color: #FFFFFF; } /* White */
    .stButton button { background-color: #8A2BE2; color: white; font-size: 18px; } /* Purple */
,   </style>
'''
    , unsafe_allow_html=True
)

# Title
st.title("💻 Laptop Price Prediction")

# Layout for Inputs
st.markdown("### Select Laptop Features")
col1, col2, col3 = st.columns(3)

# Brand Selection
brand = st.selectbox('Brand', options=['ASUS',	'Acer'	,'Apple'	,'DELL'	,'HP'	,'Infinix'	,'Lenovo',	'MICROSOFT',	'MSI',	'SAMSUNG',	'others'])
if brand in ('ASUS',	'Acer'	,'Apple'	,'DELL'	,'HP'	,'Infinix'	,'Lenovo',	'MICROSOFT',	'MSI',	'SAMSUNG',	'others'):
    if brand=='ASUS':
        brand=[1,0,0,0,0,0,0,0,0,0,0] #we will use indexing to pass values
    elif brand=='Acer':
        brand=[0,1,0,0,0,0,0,0,0,0,0]
    elif brand=='Apple':
        brand=[0,0,1,0,0,0,0,0,0,0,0]
    elif brand=='DELL':
        brand=[0,0,0,1,0,0,0,0,0,0,0]
    elif brand=='HP':
        brand=[0,0,0,0,1,0,0,0,0,0,0]
    elif brand=='Infinix':
        brand=[0,0,0,0,0,1,0,0,0,0,0]
    elif brand=='Lenovo':
        brand=[0,0,0,0,0,0,1,0,0,0,0]
    elif brand=='Microsoft':
        brand=[0,0,0,0,0,0,0,1,0,0,0]
    elif brand=='MSI':
        brand=[0,0,0,0,0,0,0,0,1,0,0]
    elif brand=='SAMSUNG':
        brand=[0,0,0,0,0,0,0,0,0,1,0]
    else:
        brand=[0,0,0,0,0,0,0,0,0,0,1]
else:
    st.warning("Brand doesn't Exists ")

# Laptop Type
type=st.selectbox('Laptop Type',options=['Chromebook', 'Notebook','Normal Laptop','Thin and Light Laptop','Handheld Gaming PC','2 in 1 Laptop','Business Laptop','Gaming Laptop','Dual Screen Laptop'])
if type in ('Chromebook', 'Notebook','Normal Laptop','Thin and Light Laptop','Handheld Gaming PC','2 in 1 Laptop','Business Laptop','Gaming Laptop','Dual Screen Laptop'):
    if type=='Chromebook':
        type=0
    elif type=='Notebook':
        type=1
    elif type=='Normal Laptop':
        type=2
    elif type=='Thin and Light Laptop':
        type=3
    elif type=='Handheld Gaming PC':
        type=4
    elif type=='2 in 1 Laptop':
        type=5
    elif type=='Business Laptop':
        type=6
    elif type=='Gaming Laptop':
        type=7
    elif type=='Dual Screen Laptop':
        type=8
else:
    st.warning('Select Valid Options')

# Touchscreen & Backlit Keyboard
Touchscreen = col1.checkbox('Touchscreen')
Backlit = col2.checkbox('Backlit Keyboard')
NVIDIA_GPU = col3.checkbox('NVIDIA GPU')

# RAM & RAM Type
ram = col1.number_input('RAM (GB)', min_value=2, step=2)
ram_rank = col2.selectbox('RAM Type',options=['DDR4','LPDDR4','LPDDR4X','DDR5','LPDDR5', 'LPDDR5X','Unified Memory'])
if ram_rank in ('DDR4','LPDDR4','LPDDR4X','DDR5','LPDDR5', 'LPDDR5X','Unified Memory'):
    if ram_rank=='DDR4':
        ram_rank=0
    elif ram_rank=='LPDDR4':
        ram_rank=1
    elif ram_rank=='LPDDR4X':
        ram_rank=2
    elif ram_rank=='DDR5':
        ram_rank=3
    elif ram_rank=='LPDDR5':
        ram_rank=4
    elif ram_rank=='LPDDR5X':
        ram_rank=5
    elif ram_rank=='Unified Memory':
        ram_rank=6
else:
    st.warning('Enter valid Type')

# Number of Cores
NCore = col3.number_input('Number of Cores', min_value=2, step=1)


# Operating System
os_rank=st.selectbox('Operating System',options=['DOS','Prime OS','Chrome','Ubuntu','Windows 10 Home','Windows 10 Pro','Windows 10','Windows 11 Home','Windows 11 Pro','Mac OS Big Sur','macOS Sonoma','macOS Sequoia'])
if os_rank in ('DOS','Prime OS','Chrome','Ubuntu','Windows 10 Home','Windows 10 Pro','Windows 10','Windows 11 Home','Windows 11 Pro','Mac OS Big Sur','macOS Sonoma','macOS Sequoia'):
    if os_rank=='DOS':
        os_rank=0
    elif os_rank=='Prime OS':
        os_rank=1
    elif os_rank=='Chrome':
        os_rank=2
    elif os_rank=='Ubuntu':
        os_rank=3
    elif os_rank=='Windows 10 Home':
        os_rank=4
    elif os_rank=='Windows 10 Pro':
        os_rank=5
    elif os_rank=='Windows 10':
        os_rank=6
    elif os_rank=='Windows 11 Home':
        os_rank=7
    elif os_rank=='Windows 11 Pro':
        os_rank=8
    elif os_rank=='Mac OS Big Sur':
        os_rank=9
    elif os_rank=='macOS Sonoma':
        os_rank=10
    elif os_rank=='macOS Sequoia':
        os_rank=11
        
else:
    st.warning('Select valid Options')

# Apple Chip
apple_chip = st.selectbox('Apple Chip',options=['M3', 'M2', 'M1', 'M3 Pro', 'M3 Max', 'M4 Max', 'M4 Pro', 'M4','None'])
if apple_chip in ('M3', 'M2', 'M1', 'M3 Pro', 'M3 Max', 'M4 Max', 'M4 Pro', 'M4','None'):
    if apple_chip=='M3':
        apple_chip=3
    elif apple_chip=='M1':
        apple_chip=1
    elif apple_chip=='M2':
        apple_chip=2
    elif apple_chip=='M4':
        apple_chip=4
    elif apple_chip=='M3 Pro':
        apple_chip=3.5
    elif apple_chip=='M3 Max':
        apple_chip=3.75
    elif apple_chip=='M4 Max':
        apple_chip=4.75
    elif apple_chip=='M4 Pro':
        apple_chip=4.5   
    elif apple_chip=='None':
        apple_chip=0
else:
    st.warning('select Valid optons')
# Processor
processor = st.selectbox('Processor', options=['None', 'Apple', 'Qualcomm'])
processor = [int(processor == 'Apple'), int(processor == 'Qualcomm')]

# SSD & Expandable SSD
SSD = col1.number_input('SSD (GB)', min_value=0, step=128)
exp_ssd = col2.number_input('Expandable SSD (GB)', min_value=0, step=128)
col3.markdown("<br><br>", unsafe_allow_html=True)

# Screen Resolution
st.markdown("### Screen Resolution")
col1, col2 = st.columns(2)
screen_x = col1.number_input('Width (pixels)', min_value=800, step=100)
screen_y = col2.number_input('Height (pixels)', min_value=600, step=100)
screen_resolution = screen_x * screen_y



# Predict Button
if st.button('🔮 Predict Price'):
    input_features = np.array([

        int(Backlit), int(Touchscreen), int(NCore), int(ram), ram_rank,
        int(SSD), processor[0], processor[1], apple_chip,
        int(exp_ssd), int(NVIDIA_GPU), os_rank,type, screen_resolution,
        brand[0],brand[1],brand[2],brand[3],brand[4],brand[5],brand[6],brand[7],brand[8],brand[9],brand[10]
    ]).reshape(1, -1)
    
    try:
        predicted_price = float(model.predict(input_features)[0])
        st.success(f'💰 Predicted Price: ₹{round(predicted_price, 2)}')
    except ValueError as e:
        st.error(f'Error in prediction: {e}')
