import tkinter as tk
from tkinter import ttk
from newspaper import Article


root = tk.Tk()
root.title("News Article Summarizer")
root.geometry('1920x1080')  
root.configure(bg='#dddddd')  


def summarize():
    url = url_entry.get()
    article = Article(url)

    try:
        article.download()
        article.parse()
        article.nlp()

        title_text.config(state='normal')
        author_text.config(state='normal')
        date_text.config(state='normal')
        summary_text.config(state='normal')

        title_text.delete('1.0', 'end')
        title_text.insert('1.0', article.title)

        author_text.delete('1.0', 'end')
        author_text.insert('1.0', ', '.join(article.authors))

        date_text.delete('1.0', 'end')
        date_text.insert('1.0', str(article.publish_date))

        summary_text.delete('1.0', 'end')
        summary_text.insert('1.0', article.summary)

        title_text.config(state='disabled')
        author_text.config(state='disabled')
        date_text.config(state='disabled')
        summary_text.config(state='disabled')
    except Exception as e:
        title_text.delete('1.0', 'end')
        title_text.insert('1.0', "Error")
        author_text.delete('1.0', 'end')
        author_text.insert('1.0', str(e))
        date_text.delete('1.0', 'end')
        summary_text.delete('1.0', 'end')
        summary_text.insert('1.0', "Unable to summarize the article.")


label_font = ('Helvetica', 14)
label_bg = '#2e2e2e'
label_fg = 'white'
label_width = 20

title_label = ttk.Label(root, text="Title:", font=label_font, background=label_bg, foreground=label_fg)
title_label.place(x=50, y=50)

author_label = ttk.Label(root, text="Author(s):", font=label_font, background=label_bg, foreground=label_fg)
author_label.place(x=50, y=100)

date_label = ttk.Label(root, text="Publishing Date:", font=label_font, background=label_bg, foreground=label_fg)
date_label.place(x=50, y=150)

summary_label = ttk.Label(root, text="Summary:", font=label_font, background=label_bg, foreground=label_fg)
summary_label.place(x=50, y=200)


text_font = ('Helvetica', 12)
text_bg = '#2e2e2e'
text_fg = 'white'
text_state = 'disabled'
text_width = 130
text_height = 2  

title_text = tk.Text(root, height=text_height, width=text_width, state=text_state, font=text_font, bg=text_bg, fg=text_fg)
title_text.place(x=200, y=50)

author_text = tk.Text(root, height=text_height, width=text_width, state=text_state, font=text_font, bg=text_bg, fg=text_fg)
author_text.place(x=200, y=100)

date_text = tk.Text(root, height=text_height, width=text_width, state=text_state, font=text_font, bg=text_bg, fg=text_fg)
date_text.place(x=200, y=150)

summary_text = tk.Text(root, height=15, width=text_width, state=text_state, font=text_font, bg=text_bg, fg=text_fg)
summary_text.place(x=200, y=200)


url_label = ttk.Label(root, text="Enter the URL:", font=label_font, background=label_bg, foreground=label_fg)
url_label.place(x=50, y=500)

url_entry = ttk.Entry(root, width=195)
url_entry.place(x=200, y=500)


summarize_button = ttk.Button(root, text="Summarize", command=summarize)
summarize_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)  # Center the button



root.mainloop()
