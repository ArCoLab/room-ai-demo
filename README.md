# 🏠 Room AI: Professional Virtual Staging API

[![Streamlit App](https://img.shields.io/badge/Streamlit-App-ff4b4b?style=flat&logo=streamlit)](https://room-ai-demo.streamlit.app) 
[![RapidAPI](https://img.shields.io/badge/RapidAPI-Connect-blue)](https://rapidapi.com/wpcoderu/api/room-ai-virtual-staging-professional-interior-design)

**High-performance Virtual Staging infrastructure for developers, real estate platforms, and PropTech startups.**

Transform empty room photos into fully furnished, photorealistic interior designs in seconds. Powered by NVIDIA RTX 5090.

-----

### ⚡ Powered by Enterprise Hardware

  * **GPU:** NVIDIA GeForce RTX 5090 (32GB VRAM)
  * **RAM:** 128GB High-Speed Memory
  * **Architecture:** Optimized X-Decoder + ControlNet pipeline for 100% spatial accuracy.

-----

### 🛠️ Developer Integration (Quick Start)

#### 1\. Initialize Staging (POST)

    curl --request POST \ 
    --url 'https://room-ai-virtual-staging-professional-interior-design.p.rapidapi.com/staging' \
    --header 'x-rapidapi-key: YOUR\_API\_KEY' \  
    --form 'image=@room.jpg' \  
    --form 'room=living\_room' \  
    --form 'style=industrial' \ 
    --form 'furnish=true'

#### 2\. Check Status (GET)

    curl --request GET \ 
    --url 'https://room-ai-virtual-staging-professional-interior-design.p.rapidapi.com/status/TASK\_ID' \
    --header 'x-rapidapi-key: YOUR\_API\_KEY'

#### 3\. Download Result (GET)

    curl --request GET \
    --url 'https://room-ai-virtual-staging-professional-interior-design.p.rapidapi.com/download/FILENAME' \
    --header 'x-rapidapi-key: YOUR\_API\_KEY'

-----

### 🎨 Supported Configurations

| Parameter | Options |
| :--- | :--- |
| **Room Types** | living\_room, bedroom, kitchen, office, bathroom, dining\_room, hallway, nursery |
| **Styles** | modern, scandinavian, industrial, classic, boho, minimalist, art\_deco |

-----

### 📝 License

This reference implementation is available under the MIT License.

Built for the PropTech community.
[Get API Access on RapidAPI](https://rapidapi.com/wpcoderu/api/room-ai-virtual-staging-professional-interior-design)
