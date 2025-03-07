# FastAPI Microservice for AI Summarization

## 📌 Project Overview

This project is a **FastAPI microservice** that provides text summarization capabilities using an **open-source AI model** from Hugging Face (e.g., DistilBART). The microservice exposes two endpoints:

- `/query`: Accepts a basic user query and returns a structured response.
- `/summarize`: Accepts long-form text and returns a concise summary using AI.

This service is **production-ready**, includes **error handling**, and can be **containerized using Docker**.

---

## 🚀 Features

- **FastAPI** framework for high-performance API development
- **Hugging Face Transformers** for AI-powered text summarization
- **Asynchronous API Endpoints** for scalability
- **Input Validation & Error Handling** for security
- **Unit Tests** with `pytest` and `httpx`
- **Dockerized Deployment**

---

## 🛠️ Installation & Setup

### **1️⃣ Clone the Repository**

```sh
git clone https://github.com/your-username/fastapi-summarizer.git
cd fastapi-summarizer
```

### **2️⃣ Create Virtual Environment & Install Dependencies**

```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### **3️⃣ Run the API Locally**

```sh
uvicorn app.main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

---

## 🔥 API Endpoints

### **1️⃣ Basic Query Processing**

#### **Endpoint:**

```http
POST /query
```

#### **Request Body:**

```json
{
  "query": "Hello!"
}
```

#### **Response:**

```json
{
  "message": "Received query: Hello!"
}
```

---

### **2️⃣ Text Summarization**

#### **Endpoint:**

```http
POST /summarize
```

#### **Request Body:**

```json
{
  "text": "This is a long document that needs summarization..."
}
```

#### **Response:**

```json
{
  "summary": "Summarized version of the input text."
}
```

---

## 🧪 Running Unit Tests

Tests are included in the `tests/` directory.

### **Run Tests with pytest:**

```sh
pytest tests/
```

---

## 🐳 Docker Deployment

### **1️⃣ Build the Docker Image**

```sh
docker build -t fastapi-summarizer .
```

### **2️⃣ Run the Container**

```sh
docker run -p 8000:8000 fastapi-summarizer
```

---

## 🔒 Security & Performance Enhancements

- **Input Validation:** Ensures the text is long enough for summarization.
- **Graceful Error Handling:** Handles invalid inputs and API failures.
- **Logging:** Structured logs for debugging.

---

## 📊 Performance & Limitations

- **Inference Time:** ~1-2 seconds per request.
- **Max Input Length:** Limited to 1024 tokens.
- **Dockerized:** Easily deployable anywhere.

---

## 📜 License

MIT License. Free to use and modify.

---

## 🤝 Contributing

Feel free to fork this repository and submit pull requests!

---

## 📩 Contact

For any questions, reach out at [abid.hi2k"gmail.com](mailto:abid.hi2k"gmail.com).
