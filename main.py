# importing Modules
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk,ImageDraw,ImageFont



# window
window = Tk()
window.title("WaterMark App")
window.config(padx=50, pady=50, bg="#f8fafc")
text_entry = None
image = None



def img_show():
    global image, tk_img
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    if file_path:
        canvas_width = 350
        canvas_height = 250

        image = Image.open(file_path)
        image = image.resize((canvas_width, canvas_height))
        tk_img = ImageTk.PhotoImage(image)

        canvas.delete("all")
        canvas.create_image(canvas_width // 2, canvas_height // 2, image=tk_img)



def add_watermark():
    global text_entry

    frame = Frame(window, bg="#f8fafc")
    frame.pack(pady=5)

    text_entry = Entry(frame, font=("Arial", 10, "bold"))
    text_entry.pack(side=LEFT, padx=5)

    ok_button = Button(frame, text="OK ✅", font=("Arial", 10, "bold"), command=apply_watermark)
    ok_button.pack(side=LEFT)

def apply_watermark():
    global image, tk_img, text_entry

    if image and text_entry:
        text = text_entry.get()
        if text.strip() == "":
            return

        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 30)
        width, height = image.size
        text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:]
        position = ((width - text_width) // 2, (height - text_height) // 2)
        draw.text(position, text, fill=(255, 255, 255, 180), font=font)

        tk_img = ImageTk.PhotoImage(image)
        canvas.delete("all")
        canvas.create_image(175, 125, image=tk_img)


def save_image():
    global image
    if image:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
        )
        if file_path:
            image.save(file_path)
            print("✅ Image saved at:", file_path)



# title of App
label_title = Label(
    window,
    text="✨ WaterMark App ✨",
    font=("Poppins", 24, "bold"),   # modern rounded font
    fg="#1e3a8a",                   # deep blue color
    bg="#f8fafc"                    # match window background
)
label_title.pack(pady=20)


# open image Button
img_button = Button(
    window,
    text="📷  Open Image",
    font=("Helvetica", 14, "bold"),
    bg="#2563eb",        # blue background
    fg="white",          # white text
    activebackground="#1d4ed8",  # darker blue on click
    activeforeground="white",
    relief="flat",       # flat, modern style
    padx=15,
    pady=8,
    cursor="hand2"  ,# hand cursor on hover
    command=img_show
)
img_button.pack(pady=5)


# Canvas to show image
canvas = Canvas(window, width=350, height=250, bg="#e5e7eb", highlightthickness=0)
canvas.pack(pady=20)

add_watermark_button = Button(
    window,
    text="Add WaterMark",
    font=("Arial", 13, "bold"),
    command=add_watermark
)
add_watermark_button.pack(pady=5)

save_button = Button(
    window,
    text="💾 Save Image",
    font=("Helvetica", 13, "bold"),
    bg="#22c55e",          # green
    fg="white",
    activebackground="#16a34a",
    activeforeground="white",
    relief="flat",
    padx=15,
    pady=8,
    cursor="hand2",
    command=save_image
)
save_button.pack(pady=10)



window.mainloop()
