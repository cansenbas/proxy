import tkinter as tk
from tkinter import ttk
import requests

def get_proxies():
    url = "https://www.proxy-list.download/api/v1/get?type=http"
    response = requests.get(url)
    proxies = response.text.split("\n")
    return proxies

def use_proxy():
    selected_proxy = text_widget.get("1.0", "end-1c")
    selected_proxy = selected_proxy.split("\n")
    selected_proxy = selected_proxy[text_widget.index("insert").split(".")[0]]
    print(f"Seçilen proxy: {selected_proxy}")
    # Use the selected proxy in your program here

root = tk.Tk()
root.title("Proxy Listesi")

proxies = get_proxies()

text_widget = tk.Text(root, height=20, width=50)
text_widget.pack()

for proxy in proxies:
    text_widget.insert(tk.END, proxy + "\n")

use_proxy_button = ttk.Button(root, text="Proxy Kullan", command=use_proxy)
use_proxy_button.pack()

root.mainloop()
