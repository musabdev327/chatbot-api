# 🚀 Chatbot API with FastAPI

This project is a simple chatbot API built using **FastAPI**, designed to respond to user messages intelligently. It handles various user inputs with fuzzy matching and predefined responses.

---

## 📌 Features

✅ **FastAPI-powered** backend  
✅ **Health Check Endpoint** to monitor service status  
✅ **Interactive Chatbot** with response variation  
✅ **Fuzzy String Matching** to handle message variations  
✅ **Predefined Conversational Responses**  
✅ **Fully Async API** for better performance  

---

## 📂 Project Structure

```
/chatbot-api
│── /backend
│   │── /routers
│   │   │── health.py      # Health check endpoint
│   │   │── chat.py        # Chatbot API logic
│   │── main.py            # Entry point for FastAPI
│── requirements.txt       # Project dependencies
│── README.md              # Documentation
```

---

## 🔧 Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone <repository-url>
cd chatbot-api
```

### **2️⃣ Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the API

Start the FastAPI server using **Uvicorn**:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 🔥 API Endpoints

### **🛠 Health Check**
```http
GET /health
```
✔ Returns `200 OK` if the server is running.

---

### **💬 Chat Endpoint**
```http
POST /chat
```
#### **Request Body**
```json
{
  "message": "hello"
}
```

#### **Response Example**
```json
{
  "response": "Hi there! Need assistance?"
}
```

✔ Handles multiple variations of greetings, questions, and goodbyes.  
✔ Uses fuzzy matching for better interaction.

---

## 📌 Author

Developed by **Musab**  
For queries, contact: musabdev327@gmail.com  

---
