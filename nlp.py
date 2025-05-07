import tkinter as tk
from tkinter import scrolledtext
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Veri setini yükle
df = pd.read_csv('genisletilmis_hastane_chatbot_veri_seti.csv')
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["soru"])

# Soru-cevap fonksiyonu
def get_answer(user_question):
    user_question_vec = vectorizer.transform([user_question])
    cosine_similarities = cosine_similarity(user_question_vec, tfidf_matrix)
    best_match_index = cosine_similarities.argmax()
    return df["cevap"].iloc[best_match_index]

# GUI oluştur
def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    chatbox.insert(tk.END, "Siz: " + user_input + "\n")
    response = get_answer(user_input)
    chatbox.insert(tk.END, "Bot: " + response + "\n\n")
    entry.delete(0, tk.END)

# Pencere
window = tk.Tk()
window.title("Hastane Chatbot")
window.geometry("500x700")

# Chat ekranı
chatbox = scrolledtext.ScrolledText(window, wrap=tk.WORD, state='normal')
chatbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Giriş alanı
entry = tk.Entry(window, font=("Arial", 14))
entry.pack(padx=10, pady=(0, 10), fill=tk.X)

# Gönder butonu
send_button = tk.Button(window, text="Gönder", command=send_message)
send_button.pack(padx=10, pady=(0, 10))

# Enter tuşuyla mesaj gönderme
window.bind('<Return>', lambda event: send_message())

# Başlat
window.mainloop()
