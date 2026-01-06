# 📧 Spam Email Classification Web App

A modern **Machine Learning + Flask** web application that classifies email or SMS messages as **Spam** or **Ham** using **TF-IDF** and **Naive Bayes**.

This project is beginner-friendly, explainable, and perfect for **learning NLP**, **ML model deployment**, and **portfolio showcase**.

---

## 🚀 Features

- ✅ Spam vs Ham email/SMS classification  
- 🧠 Machine Learning model (Naive Bayes + TF-IDF)  
- 🌐 Interactive Flask web application  
- 🎨 Modern, responsive UI  
- 📦 Model persistence using `joblib`  
- 👤 About Developer button (LinkedIn integration)

---

## 🧩 Tech Stack

- Python  
- Flask  
- Scikit-learn  
- Pandas  
- Joblib  
- HTML & CSS  

---

## 📁 Project Structure

```
spam-email-classifier/
│
├── app.py
├── spam_email_model.joblib
├── tfidf_vectorizer.joblib
│
├── templates/
│   └── index.html
│
└── static/
```

---

## 📊 Dataset

The model is trained using a labeled spam email dataset from Kaggle:

- **Columns**
  - `email_text` → Content of the email/SMS
  - `label` → spam / ham

Dataset path used in Kaggle:
```
/kaggle/input/spam-email-classification-dataset/email_spam_dataset.csv
```

---

## ▶️ How to Run Locally

### 1️⃣ Install dependencies
```bash
pip install flask scikit-learn pandas joblib
```

### 2️⃣ Run the app
```bash
python app.py
```

### 3️⃣ Open in browser
```
http://127.0.0.1:5000
```

---

## 🧪 Example Test Messages

**Spam**
```
Congratulations! You won a cash prize. Click now to claim.
```

**Ham**
```
Hi, our meeting is scheduled for tomorrow at 11 AM.
```

---

## 👨‍💻 Developer

**Nayon Ahmed**  
🔗 LinkedIn: https://www.linkedin.com/in/nayonahmed/

---

## ⭐ Use Case

- NLP beginners  
- Machine Learning practice project  
- Flask deployment demo  
- Resume / portfolio project  

If you find this project useful, feel free to ⭐ the repository!
