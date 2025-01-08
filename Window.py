import customtkinter
from tkinter import *
from Backend import *
from yt_dlp.utils import *
import threading

class Window:
    def __init__(self):
        root = customtkinter.CTk()

        def download_btn_clicked():

            status_label.configure(text = "")
            link = link_entry.get()

            def label_update():
                try:
                    status_label.configure(text = "Downloading", text_color = 'white')
                    title = Backend(link).title_provider()
                    status_label.configure(text = f"Downloading {title}")
                except:
                    status_label.configure(text = "Error while fatching video details")
            
            def downloader():
                try:
                    title = Backend(link).title_provider()
                    Backend(link).downloader(title)
                    status_label.configure(text = f"Successully downloaded {title}")
                except(UnsupportedError, ExtractorError):
                    status_label.configure(text = "UNSUPPORTED ERROR OCCURED\nPlease provide a valid link")
                except:
                    status_label.configure(text = "Error while fatching video details")
                
            t1 = threading.Thread(target = label_update)
            t2 = threading.Thread(target = downloader)
            t1.start()
            t2.start()

        # customtkinter.set_appearance_mode("system") --> This is by default on
        root.geometry("640x480")
        root.title("Youtube Downloader")

        top_label = customtkinter.CTkLabel(master = root,
                                                text="Paste the vide link below",
                                                font=("", 14, "bold")
                                            )

        link_entry = customtkinter.CTkEntry(master = root,
                                                width=400,
                                                height=40,
                                                placeholder_text="Paste the link here!",
                                                corner_radius=15,
                                                border_width=3
                                            )

        download_btn = customtkinter.CTkButton(master=root, text="Download",
                                                command = download_btn_clicked,
                                                border_color="black",
                                                fg_color="#039dfc",
                                                hover_color="#03befc",
                                                border_width=2,
                                                font=("", 14, "bold"),
                                                corner_radius=15,
                                                border_spacing=10                                           
                                            )

        status_label = customtkinter.CTkLabel(master = root,
                                                text = "", text_color="red",
                                                font=("", 14)
                                            )
        
        top_label.place(relx = 0.5, rely = 0.1, anchor = CENTER)
        
        link_entry.place(relx = 0.5, rely = 0.3, anchor = CENTER)

        download_btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        status_label.place(relx = 0.5, rely = 0.7, anchor = CENTER)

        root.mainloop()


if __name__ == "__main__":
    app = Window()
