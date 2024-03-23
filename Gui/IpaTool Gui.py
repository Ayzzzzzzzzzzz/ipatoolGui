import tkinter as tk
from tkinter import ttk, filedialog
import subprocess
import webbrowser

def download_ipa():
    bundle_identifier = bundle_identifier_entry.get()
    output_path = output_path_entry.get()
    purchase = purchase_var.get()

    command = ["ipatool", "download", "--bundle-identifier", bundle_identifier, "--output", output_path]
    if purchase:
        command.append("--purchase")
    
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            output_text.insert(tk.END, result.stdout)
        else:
            output_text.insert(tk.END, result.stderr)
    except Exception as e:
        output_text.insert(tk.END, str(e) + "\n")

def search_apps():
    search_term = search_term_entry.get()
    limit = limit_var.get()

    command = ["ipatool", "search", search_term, "--limit", str(limit)]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            output_text_search.insert(tk.END, result.stdout)
        else:
            output_text_search.insert(tk.END, result.stderr)
    except Exception as e:
        output_text_search.insert(tk.END, str(e) + "\n")

def purchase_license():
    bundle_identifier = purchase_bundle_identifier_entry.get()

    command = ["ipatool", "purchase", "--bundle-identifier", bundle_identifier]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            output_text_purchase.insert(tk.END, result.stdout)
        else:
            output_text_purchase.insert(tk.END, result.stderr)
    except Exception as e:
        output_text_purchase.insert(tk.END, str(e) + "\n")

def browse_output_path():
    output_path = filedialog.asksaveasfilename(defaultextension=".ipa")
    output_path_entry.delete(0, tk.END)
    output_path_entry.insert(0, output_path)

def browse_purchase_bundle_identifier():
    bundle_identifier = filedialog.askopenfilename()
    purchase_bundle_identifier_entry.delete(0, tk.END)
    purchase_bundle_identifier_entry.insert(0, bundle_identifier)

def open_github():
    webbrowser.open_new("https://github.com/Ayzzzzzzzzzzz")

def open_instagram():
    webbrowser.open_new("https://www.instagram.com/jak_bec/")

def open_ipatool():
    webbrowser.open_new("https://github.com/majd/ipatool")    

root = tk.Tk()
root.title("IPA Tool Gui made by Ayz")

notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

download_frame = tk.Frame(notebook)
notebook.add(download_frame, text="Download")

bundle_identifier_label = tk.Label(download_frame, text="Bundle Identifier:")
bundle_identifier_label.grid(row=0, column=0, sticky="w")
bundle_identifier_entry = tk.Entry(download_frame)
bundle_identifier_entry.grid(row=0, column=1, padx=5, pady=5)

output_path_label = tk.Label(download_frame, text="Output Path:")
output_path_label.grid(row=1, column=0, sticky="w")
output_path_entry = tk.Entry(download_frame)
output_path_entry.grid(row=1, column=1, padx=5, pady=5)
browse_button = tk.Button(download_frame, text="Browse", command=browse_output_path)
browse_button.grid(row=1, column=2, padx=5, pady=5)

purchase_var = tk.BooleanVar()
purchase_checkbutton = tk.Checkbutton(download_frame, text="Purchase", variable=purchase_var)
purchase_checkbutton.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

download_button = tk.Button(download_frame, text="Download", command=download_ipa)
download_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

output_text = tk.Text(download_frame, height=10, width=50)
output_text.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

search_frame = tk.Frame(notebook)
notebook.add(search_frame, text="Search")

search_term_label = tk.Label(search_frame, text="Search Term:")
search_term_label.grid(row=0, column=0, sticky="w")
search_term_entry = tk.Entry(search_frame)
search_term_entry.grid(row=0, column=1, padx=5, pady=5)

limit_label = tk.Label(search_frame, text="Limit:")
limit_label.grid(row=1, column=0, sticky="w")
limit_var = tk.IntVar(value=5)
limit_entry = tk.Entry(search_frame, textvariable=limit_var)
limit_entry.grid(row=1, column=1, padx=5, pady=5)

search_button = tk.Button(search_frame, text="Search", command=search_apps)
search_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

output_text_search = tk.Text(search_frame, height=10, width=50)
output_text_search.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

purchase_frame = tk.Frame(notebook)
notebook.add(purchase_frame, text="Purchase")

purchase_bundle_identifier_label = tk.Label(purchase_frame, text="Bundle Identifier:")
purchase_bundle_identifier_label.grid(row=0, column=0, sticky="w")
purchase_bundle_identifier_entry = tk.Entry(purchase_frame)
purchase_bundle_identifier_entry.grid(row=0, column=1, padx=5, pady=5)
browse_purchase_button = tk.Button(purchase_frame, text="Browse", command=browse_purchase_bundle_identifier)
browse_purchase_button.grid(row=0, column=2, padx=5, pady=5)

purchase_button = tk.Button(purchase_frame, text="Purchase", command=purchase_license)
purchase_button.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

output_text_purchase = tk.Text(purchase_frame, height=10, width=50)
output_text_purchase.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

credits_frame = tk.Frame(notebook)
notebook.add(credits_frame, text="Credits")

github_button = tk.Button(credits_frame, text="GitHub", command=open_github)
github_button.pack(pady=10)

instagram_button = tk.Button(credits_frame, text="Instagram", command=open_instagram)
instagram_button.pack(pady=10)

ipatool_button = tk.Button(credits_frame, text="ipatool", command=open_ipatool)
ipatool_button.pack(pady=10)

root.mainloop()
