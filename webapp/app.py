import streamlit as st
from ultralytics import YOLO
from PIL import Image

model_path = "/home/gourav/ML/PCB Fault Detection/webapp/model/best.pt"
st.set_page_config(page_title="PCB Fault Detection ", page_icon=":shark:", layout="wide",)

#title
st.title("PCB Fault Detection")

#subtitle
st.markdown("This application helps you to detect the faults in pcb's. ")

@st.cache_resource(show_spinner="Loading the app..")
def load_model(model_name):
    model = YOLO(model_name)
    return model

model = load_model(model_path)
image_shape = [640,640]
  
#image uploader
image = st.file_uploader(label = "Upload your image here", type=['png','jpg','jpeg'])

if image is not None:

    img = Image.open(image) 
    with st.spinner("Detecting the faults"):
        # img = img.resize(image_shape)
        result = model.predict(img, conf = 0.5, show_conf = False )
        plot_img = result[0].plot()
        result_img = Image.fromarray(plot_img)
    
    col1, col2 = st.columns(2)

    with col1:
        st.header("Original Image")
        st.image(img)

    with col2:
        st.header("Detected Fault Image")
        st.image(result_img)
else:
    st.write("Upload an Image first")


st.caption("Made by Gourav Chouhan ")


  