import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import os
import uuid
import datetime

# --------------------------
# Page Configuration
# --------------------------
st.set_page_config(
    page_title="Text2ImageGen-AI",
    layout="centered",
    page_icon="🎨",
)

@st.cache_resource
def load_model():
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    )
    pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    return pipe

pipe = load_model()

# --------------------------
# UI Title
# --------------------------
st.title("🎨 Text2ImageGen-AI")
st.write("Generate high-quality images from text using Stable Diffusion v1.5")

# --------------------------
# Prompt Input
# --------------------------
prompt = st.text_area(
    "Enter your prompt",
    placeholder="Example: A futuristic cyberpunk city with neon lights, 8K highly detailed"
)

steps = st.slider("Inference Steps", 20, 60, 30)
guidance_scale = st.slider("Guidance Scale", 1.0, 12.0, 7.5)

generate_btn = st.button("Generate Image 🚀")

# --------------------------
# Processing
# --------------------------
if generate_btn:
    if not prompt.strip():
        st.warning("Please enter a prompt.")
        st.stop()

    with st.spinner("Generating image... this can take a few seconds ⏳"):
        image = pipe(
            prompt,
            num_inference_steps=steps,
            guidance_scale=guidance_scale
        ).images[0]

    # Save Output
    os.makedirs("outputs", exist_ok=True)
    filename = f"outputs/{uuid.uuid4().hex}.png"
    image.save(filename)

    st.image(image, caption="Generated Image", use_column_width=True)
    st.success("Image generated successfully!")

    with open(filename, "rb") as img_file:
        st.download_button(
            label="Download Image",
            data=img_file,
            file_name=f"generated_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png",
            mime="image/png"
        )
