import pickle
import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Load the trained model
url = "https://github.com/Dawood006/ByteWorth-app/raw/950e6900c670862d1415bbb625bf27e55e5f2780/RF_model/laptop_randomf_model.pkl"
model_path = "laptop_randomf_model.pkl"

# Download model file
urllib.request.urlretrieve(url, model_path)
with open(model_path, "rb") as file:
    model = pickle.load(file)


st.title('*Laptop Price Prediction*💻')

with st.form(key='price'):
    brand = st.selectbox('Brand', options=['ASUS',	'Acer'	,'Apple'	,'DELL'	,'HP'	,'Infinix'	,'Lenovo',	'MICROSOFT',	'MSI',	'SAMSUNG',	'others'])
    if brand in ('ASUS',	'Acer'	,'Apple'	,'DELL'	,'HP'	,'Infinix'	,'Lenovo',	'MICROSOFT',	'MSI',	'SAMSUNG',	'others'):
        if brand=='ASUS':
            brand=[1,0,0,0,0,0,0,0,0,0,0]
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

    type=st.selectbox('What Kind of Laptop you Looking for ?',options=['Chromebook', 'Notebook','Laptop','Thin and Light Laptop','Handheld Gaming PC','2 in 1 Laptop','Business Laptop','Gaming Laptop','Dual Screen Laptop'])
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
    
    st.caption('## Screen Resolution')
    col1,col2=st.columns(2) #columns to fit screen resolution without distrubing the allingment
    b=col1.number_input('Width (Pixels)', min_value=800, step=100)
    c=col2.number_input('Height (Pixels)', min_value=800, step=100)
    #column wise


    col1,col2,col3=st.columns(3)
    #first_row
    finger = col1.checkbox('Fingerprint Sensor', value=True)
    finger = int(finger) 

    

    Ms= col2.checkbox('Microsoft Office', value=True)
    Ms= int(Ms)

    backlit = col3.checkbox('Backlit Keyboard', value=True)
    backlit = int(backlit)


    

    #Second_row
    Touchscreen = col1.checkbox('Touchscreen ', value=True)
    Touchscreen = int(Touchscreen)

    Face = col2.checkbox('Face Recognition ', value=True)
    Face = int(Face)
    col3.markdown("<br>", unsafe_allow_html=True) 

    #Third_row
    pro_brand = col1.selectbox('Processor Brand',options=['Apple','Intel','Mediatek','Qualcomm','AMD'])
    if pro_brand in ('Apple','Intel','Mediatek','Qualcomm','AMD'):
        if pro_brand=='AMD':
            pro_brand=[1,0,0,0,0]
        elif pro_brand=='Apple':
            pro_brand=[0,1,0,0,0]   
        elif pro_brand=='Intel':
            pro_brand=[0,0,1,0,0]
        elif pro_brand=='Mediatek':
            pro_brand=[0,0,0,1,0]
        else:
            pro_brand=[0,0,0,0,1]
    else:
        st.warning('Select  Valid Option')
    
    p_variant = col2.selectbox('Processor Variant',options=['High Performance H','Ultra Efficent U','Entry-Level N'])
    if p_variant in ('High Performance H','Ultra Efficent U','Entry-Level N'):
        if p_variant=='High Performance H':
            p_variant=3
        elif p_variant=='Ultra Efficent U':
            p_variant=2
        elif p_variant=='Entry-Level N':
            p_variant=1
        else:
            p_variant=0
    else:
        st.warning('Select  Valid Option')
    
    

    os_rank=col3.selectbox('Operating System',options=['DOS','Prime OS','Chrome','Ubuntu','Windows 10 Home','Windows 10 Pro','Windows 10','Windows 11 Home','Windows 11 Pro','Mac OS Big Sur','macOS Sonoma','macOS Sequoia'])
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

    #fourth_row

    drive = col1.selectbox('Storage',options=['SSD','HDD','Hybrid','eMMC'])
    if drive in('SSD','HDD','Hybrid','eMMC'):
        if drive=='SSD' :
            drive=[1,0,0,0]
        elif drive=='HDD':
            drive=[0,1,0,0]
        elif drive=='Hybrid':
            drive=[0,0,1,0]
        else:
            drive=[0,0,0,1]
    else:
        st.warning('Select Valid Storage')

    SSD = col2.number_input('SSD (GB)',min_value=0,step=128)
    HDD = col3.number_input('HDD (GB)',min_value=0,step=128)

    #fifth_row
    g_card = col1.selectbox('Graphic Processor',options=['Intel','NVIDA','Qualcomm','Not Avialable','MediaTek'])
    
    if g_card in ('AMD','Intel','NVIDA','Qualcomm','Not Avialable','MediaTek'):
        if g_card=='AMD':
            g_card=[1,0,0,0,0,0]
        elif g_card=='Intel':
            g_card=[0,1,0,0,0,0]
        elif g_card=='MediaTek':
            g_card=[0,0,1,0,0,0]
        elif g_card=='Not Avialable':
            g_card=[0,0,0,1,0,0]
        elif g_card=='NVIDA':
            g_card=[0,0,0,0,1,0]
        elif g_card=='Qualcomm':
            g_card=[0,0,0,0,0,1]
    else :
        st.warning('Enter Valid Graphic Card')

    d_graphic_mem = col2.number_input('Graphic Memory Capacity (GB)',min_value=0,step=2)

    apple_chip = col3.selectbox('Apple Chip',options=['M3', 'M2', 'M1', 'M3 Pro', 'M3 Max', 'M4 Max', 'M4 Pro', 'M4','None'])
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
    
     #sixth_row
    ram = col1.number_input('RAM (GB)',min_value=2,step=2)
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
    

    #seventh_row
    NCore = col1.number_input('Number of Cores',min_value=0,step=1)
    # Expmemory = col2.number_input('Expandable Memory (GB)')
    exp_ssd = col3.number_input('Expandable SSD Capacity (GB)')
    
     
    
    #eigth_row
    
    

    #ninth_row
    
    

    p = col1.form_submit_button('Predict')

if p:
    # Convert inputs to the expected format (ensure numerical values where needed)
    input_features = np.array([

     finger,Ms,backlit,Touchscreen,Face,NCore, int(ram), ram_rank ,

     int(SSD), int(HDD),brand[0],brand[1],brand[2],brand[3],brand[4],brand[5],brand[6],brand[7],brand[8],brand[9],brand[10],

     drive[0],drive[1],drive[2],drive[3],

     int(d_graphic_mem),pro_brand[0],pro_brand[1],pro_brand[2],pro_brand[3],pro_brand[4],

     apple_chip, p_variant,int(exp_ssd),g_card[0],g_card[1],g_card[2],g_card[3],g_card[4],g_card[5],
     
     os_rank,type,b*c]).reshape(1, -1)  # Reshape for prediction

    
    try:
        predicted_price = float(model.predict(input_features)[0])  
        st.success(f"Predicted Price: ₹{round(predicted_price,2)}")
    except ValueError as e:
        st.error(f"Error in prediction: {e}")
        st.write(f"Input features shape: {input_features.shape}")
