import streamlit as st
import requests
import time
from PIL import Image
import io

# Configuration
st.set_page_config(page_title="Room AI API Demo", layout="wide")

st.title("🏠 Room AI: Professional Virtual Staging")
st.write("Reference implementation for developers. [API Documentation](https://rapidapi.com/your-link)")

# Sidebar for Auth
st.sidebar.header("Authentication")
RAPIDAPI_KEY = st.sidebar.text_input("RapidAPI Key", type="password")
HOST = "room-ai-virtual-staging-professional-interior-design.p.rapidapi.com"

# API Mapping
ROOM_CONFIG = {
    "living_room": "Living Room",
    "bedroom": "Bedroom",
    "kitchen": "Kitchen",
    "office": "Office",
    "bathroom": "Bathroom",
    "dining_room": "Dining Room",
    "hallway": "Hallway",
    "nursery": "Nursery"
}

STYLE_CONFIG = {
    "modern": "Modern Luxury",
    "scandinavian": "Scandinavian Hygge",
    "industrial": "Industrial Chic",
    "classic": "Classic Elegance",
    "boho": "Boho Chic",
    "minimalist": "Zen Minimalist",
    "art_deco": "Art Deco Glamour"
}

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 1. Request Configuration")
    uploaded_file = st.file_uploader("Upload Room Photo", type=['jpg', 'jpeg', 'png'])
    
    selected_room = st.selectbox("Room Type", options=list(ROOM_CONFIG.keys()), format_func=lambda x: ROOM_CONFIG[x])
    selected_style = st.selectbox("Design Style", options=list(STYLE_CONFIG.keys()), format_func=lambda x: STYLE_CONFIG[x])
    furnish = st.checkbox("Furnish Room", value=True)
    
    generate_btn = st.button("Start Staging ✨")

with col2:
    st.markdown("### 2. Output & Logs")
    
    if generate_btn:
        if not RAPIDAPI_KEY:
            st.error("Missing RapidAPI Key")
        elif not uploaded_file:
            st.error("Please upload an image")
        else:
            headers = {
                "x-rapidapi-host": HOST,
                "x-rapidapi-key": RAPIDAPI_KEY
            }

            # --- STEP 1: INITIALIZE STAGING ---
            with st.status("Processing...") as status:
                st.write("Uploading image to GPU cluster...")
                
                files = {"image": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                data = {
                    "furnish": str(furnish).lower(),
                    "room": selected_room,
                    "style": selected_style
                }

                try:
                    res = requests.post(f"https://{HOST}/staging", headers=headers, files=files, data=data)
                    res.raise_for_status()
                    task_data = res.json()
                    task_id = task_data.get("task_id") # Предполагаем, что API возвращает ID здесь
                    
                    st.write(f"Task created: `{task_id}`")
                    
                    # --- STEP 2: POLLING STATUS ---
                    finished = False
                    filename = None
                    for _ in range(30): # 60 seconds timeout
                        time.sleep(2)
                        status_res = requests.get(f"https://{HOST}/status/{task_id}", headers=headers)
                        status_data = status_res.json()
                        
                        current_status = status_data.get("status")
                        st.write(f"Status: `{current_status}`")
                        
                        if current_status == "completed":
                            filename = status_data.get("file")
                            finished = True
                            break
                        elif current_status == "failed":
                            st.error("Staging failed")
                            break

                    # --- STEP 3: DOWNLOAD RESULT ---
                    if finished and filename:
                        st.write("Downloading high-res result...")
                        img_res = requests.get(f"https://{HOST}/download/{filename}", headers=headers)
                        
                        if img_res.status_code == 200:
                            result_img = Image.open(io.BytesIO(img_res.content))
                            st.image(result_img, caption="Staged Interior", use_column_width=True)
                            st.balloons()
                            status.update(label="Staging Complete!", state="complete")
                        else:
                            st.error("Failed to download image")

                except Exception as e:
                    st.error(f"Error: {str(e)}")

    if not generate_btn and not uploaded_file:
        st.info("Upload an image and click 'Start Staging' to see the API in action.")
