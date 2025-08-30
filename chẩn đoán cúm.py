import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
import pandas as pd
from tkinter import *
from tkinter import ttk

#code perception lấy dữ liệu từ file excel theo đúng yêu cầu của thầy
file_path = r"C:\Users\ADMIN\Desktop\du_doan_cum_0.1.xlsx"
data = pd.read_excel(file_path)
def convert_temp(x):
    if x == "<36":
        return 35.9
    elif x == ">40":
        return 40.1
    else:
        return float(x)
data["Nhiet_do"] = data["Nhiet_do"].apply(convert_temp)
X = []
y = []
for _, row in data.iterrows():
    a = 1 if row["Nhiet_do"] >= 38 else 0
    b = row["Dau_dau"]
    c = row["Ho"]
    d = row["Met_moi"]
    e = row["Dau_hong"]
    f = 3  
    g = row["So_muoi"] 
    X.append([a, b, c, d, e, g])
    y.append(row["Cum"])
X = np.array(X)
y = np.array(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
model = Perceptron(max_iter=1000, eta0=0.1, random_state=42)
model.fit(X_train, y_train)


#code tạo giao diện
root = Tk()
root.title("Chẩn đoán cúm")
root.geometry("400x500")
root.state("zoomed")

Label(root, text="Nhiệt độ của bạn là bao nhiêu? (°C):", font=("Times", 18)).pack()
temp = ttk.Combobox(root, values=[36.0,36.1,36.2,36.3,36.4,36.5,36.6,36.7,36.8,36.9,37.0,37.1,37.2,37.3,37.4,37.5,37.6,37.7,37.8,37.9,38.0,38.1,38.2,38.3,38.4,38.5,38.6,38.7,38.8,38.9,39.0,39.1,39.2,39.3,39.4,39.5,39.6,39.7,39.8,39.9,40.0], font=("Times", 18), width=8)
temp.pack()
dd = IntVar()
Label(root, text="bạn có đau đầu không?", font=("Times", 18)).pack()
Radiobutton(root, text="Có", variable=dd, value=1, font=("Times", 18)).pack()
Radiobutton(root, text="Không", variable=dd, value=0, font=("Times", 18)).pack()
ho = IntVar()
Label(root, text="bạn có ho không?", font=("Times", 18)).pack()
Radiobutton(root, text="Có", variable=ho, value=1, font=("Times", 18)).pack()
Radiobutton(root, text="Không", variable=ho, value=0, font=("Times", 18)).pack()
mm = IntVar()
Label(root, text="bạn có mệt mỏi không?", font=("Times", 18)).pack()
Radiobutton(root, text="Có", variable=mm, value=1, font=("Times", 18)).pack()
Radiobutton(root, text="Không", variable=mm, value=0, font=("Times", 18)).pack()
dh = IntVar()
Label(root, text="bạn có đau họng không?", font=("Times", 18)).pack()
Radiobutton(root, text="Có", variable=dh, value=1, font=("Times", 18)).pack()
Radiobutton(root, text="Không", variable=dh, value=0, font=("Times", 18)).pack()
cm = IntVar()
Label(root, text="bạn có chảy mũi không?", font=("Times", 18)).pack()
Radiobutton(root, text="Có", variable=cm, value=1, font=("Times", 18)).pack()
Radiobutton(root, text="Không", variable=cm, value=0, font=("Times", 18)).pack()
ket_qua = Label(root, text="", font=("Times", 20), fg="blue")
ket_qua.pack(pady=20)
def predict():
    a = 1 if float(temp.get()) >= 38 else 0
    b = dd.get()
    c = ho.get()
    d = mm.get()
    e = dh.get()
    g = cm.get()
    bn1 = [a, b, c, d, e, g]
    ketqua = "BẠN BỊ CÚM" if model.predict([bn1]) == 1 else "BẠN KHÔNG BỊ CÚM"
    ket_qua.config(text=ketqua)

Button(root, text="Dự đoán", font=("Times", 18), bg="lightgreen", command=predict).pack()

root.mainloop()
