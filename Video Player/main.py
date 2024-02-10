import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk, Image
import cv2 as cv

# Modes: "System" (standard), "Dark", "Light"
ctk.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
ctk.set_default_color_theme("blue")


class VideoPlayerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Video Player")
        self.geometry("1100x580")
        # self.attributes('-fullscreen', True)

        # Configure grid layout (3 rows, 4 columns)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure((0, 1, 2, 4, 5), weight=0)
        self.grid_rowconfigure(0, weight=0)  # Top row
        self.grid_rowconfigure(1, weight=1)  # Middle row
        self.grid_rowconfigure(2, weight=0)  # Bottom row

        self.camera_options = self.get_available_cameras()
        self.paused = False
        self.camera_var = tk.StringVar(self)
        self.camera_var.set(self.camera_options[0])
        # self.isStreaming = True
        self.capCam = cv.VideoCapture(2)
        if (self.capCam.isOpened() == False):
            print("Unable to read camera feed")
        else:
            width = self.capCam.get(cv.CAP_PROP_FRAME_WIDTH)
            height = self.capCam.get(cv.CAP_PROP_FRAME_HEIGHT)
            print(f"Hi I am subhan {(height,width)}")

        self.isStreaming = True
        self.isStreaming_Int = tk.IntVar(value=1)

        self.streaming_radiobutton = ctk.CTkRadioButton(
            self, text="Streaming", value=1, variable=self.isStreaming_Int, command=self.disable_video_player)
        self.streaming_radiobutton.grid(
            row=0, column=0, padx=10, pady=10, sticky="e")

        self.video_radiobutton = ctk.CTkRadioButton(
            self, text="Video", value=0, variable=self.isStreaming_Int, command=self.disable_stream)
        self.video_radiobutton.grid(
            row=0, column=1, padx=10, pady=10, sticky="e")

        self.camera_dropdown = ctk.CTkOptionMenu(
            self, values=self.camera_options, variable=self.camera_var, command=self.change_camera)
        self.camera_dropdown.grid(
            row=0, column=2, padx=10, pady=10, sticky="ew")

        self.video_input_CTkEntry = ctk.CTkEntry(self)
        self.video_input_CTkEntry.grid(
            row=0, column=3, padx=10, pady=10, sticky="ew")

        self.browse_button = ctk.CTkButton(
            self, text="Browse", command=self.select_video)
        self.browse_button.grid(row=0, column=4, padx=10, pady=10, sticky="ew")

        # Row 2: Video Panel

        self.video_panel = ctk.CTkFrame(
            self)

        self.video_panel.grid(row=1, column=0, columnspan=6,
                              sticky="nsew")

        self.label = ttk.Label(self.video_panel)
        self.label.pack()

        # Row 3: Controls for video playback
        self.play_pause_button = ctk.CTkButton(
            self, text="Play/Pause", command=self.play_pause)
        self.play_pause_button.grid(
            row=2, column=0, padx=10, pady=10, sticky="ew")

        self.backward_button = ctk.CTkButton(
            self, text="<<", command=self.skip_backward)
        self.backward_button.grid(
            row=2, column=1, padx=10, pady=10, sticky="ew")

        self.forward_button = ctk.CTkButton(
            self, text=">>", command=self.skip_forward)
        self.forward_button.grid(
            row=2, column=2, padx=10, pady=10, sticky="ew")

        self.speed_dropdown = ctk.CTkOptionMenu(
            self, values=[f"{i * 0.25}" if i*0.25 != 1 else "Normal" for i in range(1, 9)])
        self.speed_dropdown.grid(
            row=0, column=5, padx=10, pady=10, sticky="ew")
        self.speed_dropdown.set("Normal")

        # self.speed_dropdown = ctk.CTkOptionMenu(
        #     self, values=[f"{i * 0.25}" if i*0.25 != 1 else "Normal" for i in range(1, 9)])
        # self.speed_dropdown.grid(
        #     row=2, column=5, padx=10, pady=10, sticky="ew")
        # self.speed_dropdown.set("Normal")

        self.color_mode_dropdown = ctk.CTkOptionMenu(
            self, values=["Color", "Grayscale", "Black and White"])
        self.color_mode_dropdown.set("Color")

        self.color_mode_dropdown.grid(
            row=2, column=4, padx=10, pady=10, sticky="ew")

        self.disable_video_player()

    def disable_stream(self):
        print("I am Playing Video")
        self.camera_dropdown.configure(state=tk.DISABLED)
        self.browse_button.configure(state=tk.NORMAL)
        self.browse_button.configure(state=tk.NORMAL)
        self.play_pause_button.configure(state=tk.NORMAL)
        self.speed_dropdown.configure(state=tk.NORMAL)
        self.isStreaming = False
        self.capCam.release()

    def get_available_cameras(self):
        index = 0
        arr = []
        while True:
            cap = cv.VideoCapture(index)
            if not cap.read()[0]:
                break
            else:
                arr.append(f"Camera {index + 1}")
            cap.release()
            index += 1
        return arr

    def disable_video_player(self):
        print("I am Streaming")
        self.browse_button.configure(state=tk.DISABLED)
        self.browse_button.configure(state=tk.DISABLED)
        self.play_pause_button.configure(state=tk.DISABLED)
        self.speed_dropdown.configure(state=tk.DISABLED)
        self.camera_dropdown.configure(state=tk.NORMAL)
        self.video_input_CTkEntry.configure(state=ctk.NORMAL)
        self.video_input_CTkEntry.delete(0, tk.END)
        self.video_input_CTkEntry.configure(state=ctk.DISABLED)
        self.isStreaming = True
        self.capCam.release()
        camera_index = int(self.camera_var.get().split()[1]) - 1
        self.capCam = cv.VideoCapture(camera_index)

        if (self.capCam.isOpened() == False):
            print("Unable to read camera feed")
        else:
            width = self.capCam.get(cv.CAP_PROP_FRAME_WIDTH)
            height = self.capCam.get(cv.CAP_PROP_FRAME_HEIGHT)
            print(f"Hi I am subhan {(height,width)}")
        self.Streaming()

    def change_camera(self, *args):
        camera_index = int(self.camera_var.get().split()[1]) - 1
        self.isStreaming = True
        self.capCam.release()
        self.capCam = cv.VideoCapture(camera_index)
        if not self.capCam.isOpened():
            print("Unable to read camera feed")
        else:
            width = self.capCam.get(cv.CAP_PROP_FRAME_WIDTH)
            height = self.capCam.get(cv.CAP_PROP_FRAME_HEIGHT)
            print(
                f"Hi, I am using camera {camera_index + 1}, dimensions: {(height, width)}")
            self.Streaming()

    def play_pause(self):
        self.paused = not self.paused
        print(self.paused)

    def select_video(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])
        if file_path:
            if self.capCam:
                self.capCam.release()
                self.paused = False
                # Release previous capture if exists
            self.capCam = cv.VideoCapture(file_path)
            self.video_input_CTkEntry.configure(state=ctk.NORMAL)
            self.video_input_CTkEntry.delete(0, tk.END)
            self.video_input_CTkEntry.insert(0, file_path)
            self.video_input_CTkEntry.configure(state=ctk.DISABLED)
            self.isStreaming = False

    def skip_backward(self):
        # Move backward by 5 frames (adjust as needed)
        self.capCam.set(cv.CAP_PROP_POS_FRAMES,
                        self.capCam.get(cv.CAP_PROP_POS_FRAMES) - 20)

    def skip_forward(self):
        # Move forward by 5 frames (adjust as needed)
        self.capCam.set(cv.CAP_PROP_POS_FRAMES,
                        self.capCam.get(cv.CAP_PROP_POS_FRAMES) + 20)

    def Streaming(self):
        print(f"in stREAM yes {self.isStreaming}")

        while self.isStreaming:
            print(f"yes {self.isStreaming}")
            img = self.capCam.read()[1]
            img = cv.flip(img, 1)
            img = self.ConvertImg(img)
            img = self.Resize(img)
            img = ImageTk.PhotoImage(Image.fromarray(img))
            self.label['image'] = img
            self.update()

    def ConvertImg(self, img):
        selected_mode = self.color_mode_dropdown.get()
        if selected_mode.lower() == "Grayscale".lower():
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            return img

        elif selected_mode.lower() == "Color".lower():
            return cv.cvtColor(img, cv.COLOR_BGR2RGB)

        elif selected_mode.lower() == "Black and White".lower():
            im_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            (thresh, im_bw) = cv.threshold(im_gray, 128,
                                           255, cv.THRESH_BINARY | cv.THRESH_OTSU)
            thresh = 175
            return cv.threshold(im_gray, thresh, 255, cv.THRESH_BINARY)[1]
        else:
            print("Invalid color mode selected:", selected_mode)
            return cv.cvtColor(img, cv.COLOR_BGR2RGB)

    def play_video(self):

        if self.capCam and not self.isStreaming and not self.paused:

            ret, frame = self.capCam.read()
            if ret:
                # cv2image = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
                img = self.ConvertImg(frame)
                img = self.Resize(img)
                # img = Image.fromarray(cv2image).resize((760, 400))
                imgtk = ImageTk.PhotoImage(Image.fromarray(img))
                # imgtk = ImageTk.PhotoImage(image=img)
                self.label.imgtk = imgtk
                self.label.configure(image=imgtk)
        self.label.after(10, self.play_video)

    def Resize(self, img):

        panel_width = self.video_panel.winfo_width()
        panel_height = self.video_panel.winfo_height()

        # Calculate the aspect ratio of the image

        img_width, img_height = img.shape[1], img.shape[0]
        img_aspect_ratio = img_width / img_height

        # Calculate the aspect ratio of the video panel
        panel_aspect_ratio = panel_width / panel_height

        if img_aspect_ratio > panel_aspect_ratio:
            # If image is wider than panel, fit to width
            new_width = panel_width
            new_height = int(new_width / img_aspect_ratio)
        else:
            # If image is taller than panel, fit to height
            new_height = panel_height
            new_width = int(new_height * img_aspect_ratio)

        # Resize the image
        resized_img = cv.resize(img, (new_width-10, new_height-10))
        return resized_img


if __name__ == "__main__":
    app = VideoPlayerApp()
    app.Streaming()
    app.play_video()
    app.mainloop()
