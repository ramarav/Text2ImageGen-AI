# HealthAssist AI 🧠💬  
### *Medical Advice Assistant using Llama-3 (Open Source) + Streamlit*

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10+-yellow)
![Streamlit](https://img.shields.io/badge/Streamlit-Enabled-red)
![Model](https://img.shields.io/badge/Model-Llama--3.2--1B-orange)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-success)

---

## 📌 Overview  
HealthAssist AI is an intelligent, local-first medical advice assistant built using:

- **Llama-3.2-1B (Quantized – CPU friendly)**
- **Streamlit UI**
- **Prompt-engineering-based reasoning**
- **Safety layer + hallucination protection**

This project is designed for beginners and intermediate ML engineers who want to *build and deploy an open‑source LLM medical assistant* without relying on expensive cloud APIs.

⚠️ *Disclaimer: This tool does **not** replace professional medical diagnosis. It is only for educational purposes.*

---

## 🚀 Features  
- ✔️ Local inference — no external API required  
- ✔️ Lightweight CPU model  
- ✔️ Multi‑turn medical chat  
- ✔️ “Low-risk advice only” safety filter  
- ✔️ Explanation mode (simple vs. detailed)  
- ✔️ Clean Streamlit UI  

---

## 📂 Project Structure  
```
HealthAssist-AI/
│── app.py
│── model/
│     ├── llama-3.2-1b-gguf.bin
│── assets/
│     ├── sample_prompts.txt
│── README.md
│── requirements.txt
```

---

## 🛠️ Installation  
```
pip install -r requirements.txt
streamlit run app.py
```

---

## 📘 Sample Prompts  
See `assets/sample_prompts.txt` for high-quality prompts.

---

## 🧪 Testing  
Run:
```
python test_model.py
```

---

## 📝 License  
MIT License – free for personal & commercial use.

---

## 🤝 Contributing  
PRs are welcome.  
Raise an issue if you want GPU acceleration or LangChain integration.

---

## ⭐ Show Your Support  
If you like this project, please ⭐ star the repo!

