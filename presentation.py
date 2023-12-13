import os
from tkinter import *
from pytube import YouTube


def sort(root, entry1, entry2, entry3, entry4, entry5):
    entries = [entry1, entry2, entry3, entry4, entry5]

    label_before = Label(root, text=f"before: {', '.join(entries)}", font=('Arial', 10, 'bold'), pady=10, padx=40, fg="Black", bg="Grey", )
    label_before.place(x=100, y=420)

    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    sorted_entries = bubble_sort(entries)

    label_after = Label(root, text=f"after: {', '.join(sorted_entries)}", font=('Arial', 10, 'bold'), pady=10, padx=40, fg="Black", bg="Grey",)
    label_after.place(x=100, y=450)



def Algoritmat():
    root = Tk()
    root.title("Algoritmat")
    root.geometry("500x550")
    root.config(background="Grey")

    label = Label(root, text="Algoritmat", font=('Arial', 20, 'bold'), pady=20, padx=80, bg="Grey", fg="Black", relief=RAISED)
    label.place(x=100, y=0)

    label_1 = Label(root, text="Nr. 1", font=('Arial', 12, 'bold'), bg="Grey", fg="Black")
    label_1.place(x=0, y=100)
    entry_1 = Entry(root, width=30, font=('Arial', 10,))
    entry_1.place(x=120, y=100)

    label_2 = Label(root, text="Nr. 2", font=('Arial', 12, 'bold'), bg="Grey", fg="Black")
    label_2.place(x=0, y=150)
    entry_2 = Entry(root, width=30, font=('Arial', 10,))
    entry_2.place(x=120, y=150)

    label_3 = Label(root, text="Nr. 3", font=('Arial', 12, 'bold'), bg='Grey', fg='Black')
    label_3.place(x=0, y=200)
    entry_3 = Entry(root, width=30, font=('Arial', 10,))
    entry_3.place(x=120, y=200)

    label_4 = Label(root, text="Nr. 4", font=('Arial', 12, 'bold'), bg='Grey', fg='Black')
    label_4.place(x=0, y=250)
    entry_4 = Entry(root, width=30, font=('Arial', 10,))
    entry_4.place(x=120, y=250)

    label_5 = Label(root, text="Nr. 5", font=('Arial', 12, 'bold'), bg='Grey', fg='black')
    label_5.place(x=0, y=300)
    entry_5 = Entry(root, width=30, font=('Arial', 10,))
    entry_5.place(x=120, y=300)

    button_sort = Button(root, text="Sorto", font=('Arial', 15, 'bold'), pady=10, padx=80, bg='Grey', fg='Black', relief=RAISED,
                         command=lambda: sort(root, entry_1.get(), entry_2.get(), entry_3.get(), entry_4.get(), entry_5.get()))
    button_sort.place(x=150, y=350)

    root.mainloop()


def info():
    def ts_info():
        ts = Tk()
        ts.geometry("500x500")
        ts.title("Test")
        ts.config(background="Grey")

        label = Label(ts, text="Kam krijuar një buton të quajtur 'Test', të cilin e kam lënë si opsion nëse dua të shtoj diçka në këtë projekt.",
                        wraplength=500,
                        fg="black",
                        bg="Grey",
                        relief=RAISED,
                        font=('Arial',15,'bold'))
        label.place(x=0, y=50)

        label = Label(ts, text="")

        ts.mainloop()

    def al_info():
        al = Tk()
        al.geometry("500x500")
        al.title("Algoritmat")
        al.config(background="Grey")

        label = Label(al, text="Kam krijuar një buton në aplikacionin tim ku përdoruesi mund të jepë në total pesë numra. Kur përdoruesi shtyp butonin 'Sorto', algoritmi i sortimit me metodën e shkëmbimit (bubble sort) do të përdoret për të renditur këto numra nga më i vogli në më të madhi. Kjo ndërveprim i lejon përdoruesin të organizojë dhe të paraqesë numrat e tyre në një rend të rregullt duke përdorur një metodë të thjeshtë, siç është bubble sort. Kjo ndryshim është bërë për të optimizuar përvojën e përdoruesit dhe për të ofruar një mënyrë të lehtë për të organizuar numrat në rradhë ascendente.",
                          wraplength=500,
                          fg="black",
                          bg="Grey",
                          relief=RAISED,
                          font=('Arial',15,'bold'))
        label.place(x=0, y=50)

        al.mainloop()

    def yt_info():
        yt = Tk()
        yt.geometry("500x500")
        yt.title("YouTube")
        yt.config(background="Grey")

        label = Label(yt, text="Në projektin tim, kam implementuar një veçori të quajtur butoni YT Converter, që mundëson përdoruesit të shkarkojnë video nga YouTube në formatin MP4 me lehtësi. Kjo funksion i përdorshëm lejon individët të vendosin URL-në e çfarëdo videoje në YouTube për të shkarkuar në formatin e preferuar, duke i ofruar përdoruesve një përvojë të thjeshtë dhe efikase. Për më tepër, përdoruesit kanë mundësinë të shkarkojnë videot në formatin MP4, por pa përfshirë imazhet, duke i dhënë kështu opsionet e nevojshme për të përshtatur shkarkimet sipas dëshirave të tyre. Ky buton shërben si një mjet i fuqishëm për përdoruesit që duan të mbajnë kopje të videove të tyre të preferuara nga YouTube në mënyrë të lehtë dhe të shpejtë.",
                          wraplength=500,
                          fg="Black",
                          bg="Grey",
                          relief=RAISED,
                          font=('Arial',15,'bold'))
        label.place(x=0, y=50)

        yt.mainloop()


    info = Tk()
    info.title("Info")
    info.geometry("550x500")
    info.config(background="Grey")

    label = Label(info, text="About", font=('Arial',17,'bold'), pady=20, padx=80, bg='Grey', fg="Black")
    label.place(x=140, y=0)

    button_yt = Button(info, text="Youtube Converter", 
                             pady=10, padx=100, 
                             font=("Arial",15,'bold'), 
                             bg='Grey', 
                             fg='Black', 
                             relief=RAISED,
                             command=yt_info)
    button_yt.place(x=80, y=100)

    button_al = Button(info, text="Algoritmat", 
                             pady=10, padx=140, 
                             font=("Arial",15,'bold'), 
                             bg='Grey', 
                             fg='Black', 
                             relief=RAISED,
                             command=al_info)
    button_al.place(x=80, y=200)

    button_ts = Button(info, text="Test", 
                             pady=10, padx=168, 
                             font=("Arial",15,'bold'), 
                             bg='Grey', 
                             fg='Black', 
                             relief=RAISED,
                             command=ts_info)
    button_ts.place(x=80, y=300)

    info.mainloop()


# downloads youtube videos in mp4 file format
def download_and_convert(url, output_filename='output.mp4'):
    try:
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        output_path = os.path.join(desktop_path, output_filename)

        # Using progressive=True to get both audio and video streams
        YouTube(url).streams.filter(progressive=True, file_extension="mp4").first().download(output_path)

        print("Download and conversion completed successfully. File saved to desktop.")
    except Exception as e:
        print(f"Error: {e}")


# downloads youtube audio in mp4 but has no video
def convert_to_mp3(url, output_filename='output.mp3'):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Set the output path to the desktop
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        output_path = os.path.join(desktop_path, output_filename)

        audio_stream.download(output_path)
        print("Conversion completed successfully. File saved on the desktop as:", output_filename)

    except Exception as e:
        print(f"Error: {e}")


# this func gets called when "YT converter" button is clicked
def youtube():
    # this is the window adjustments
    root = Tk()
    root.geometry("500x500")
    root.title("Youtube Converter")
    root.config(background="Black")

    label = Label(root, text="Youtube Converter", fg="White", bg="black", font=('Arial', 20, "bold"), padx=100, pady=20)
    label.place(x=40, y=0)

    # this is the type bar for url paste
    entry_url = Entry(root, width=30, font=('Arial', 13))
    entry_url.place(x=100, y=190)

    label_url = Label(root, text="Video URL:", fg="white", bg="Black", font=('Arial', 14, 'bold'), padx=50, pady=5)
    label_url.place(x=130, y=150)

    # this is type bar for file name (optional)
    entry_name = Entry(root, width=30, font=('Arial', 13))
    entry_name.place(x=100, y=300)

    label_name = Label(root, text="Name the Folder(optional) :", fg="White", bg="Black", font=('Arial', 14, 'bold'),
                       padx=50, pady=5)
    label_name.place(x=60, y=260)

    # when this button is clicked it will start the download for mp3 'demo' version format
    button_mp3 = Button(root,
                        text="Download MP3",
                        fg="Black",
                        bg="Grey",
                        font=('Arial', 13, 'bold'),
                        padx=20,
                        pady=5,
                        command=lambda: convert_to_mp3(entry_url.get(), entry_name.get()))
    button_mp3.place(x=150, y=430)

    # when this button is clicked the video will start getting downloaded in mp4 format
    button_download = Button(root,
                             text="Download",
                             fg="black",
                             bg="Grey",
                             font=('Arial', 15, 'bold'),
                             padx=100,
                             pady=10,
                             command=lambda: download_and_convert(entry_url.get(), entry_name.get()))
    button_download.place(x=80, y=350)

# this is the main window
main_window = Tk()
main_window.geometry("1000x500")
main_window.title("Account")
main_window.config(background="Black")

# when this button is clicked it will call the youtube func
button_yt_converter = Button(main_window,
                             text="YT converter",
                             fg="black",
                             bg="white",
                             pady=10,
                             padx=100,
                             command=youtube,
                             font=('Arial', 15, 'bold'))
button_yt_converter.place(x=100, y=150)

# this button is still under work
button_test = Button(main_window,
                     text="  Algoritmat  ",
                     fg="black",
                     bg="white",
                     pady=10,
                     padx=100,
                     font=('Arial', 15, 'bold'),
                     command=Algoritmat)
button_test.place(x=100, y=300)

# this button is still under work
button_info = Button(main_window,
                     text="      Test     ",
                     fg="black",
                     bg="white",
                     pady=10,
                     padx=100,
                     font=('Arial', 15, 'bold'))
button_info.place(x=500, y=150)

# When this button is clicked to will show info about the creator and the motive of starting this project
button_test_2 = Button(main_window,
                       text="      About     ",
                       fg="black",
                       bg="white",
                       pady=10,
                       padx=100,
                       command=info,
                       font=('Arial', 15, 'bold'))
button_test_2.place(x=500, y=300)

label_h1 = Label(main_window, text="Welcome", fg="white", bg="black", font=('Arial', 25, 'bold'), padx=100, pady=20)
label_h1.place(x=300, y=0)

main_window.mainloop()
