# **Custom Pomodoro Timer**

I always wanted my own custom Pomodoro app with sounds and an interface I enjoy. So, I created one using Python! 🚀

This app allows you to customize your Pomodoro sessions, including work time, break durations, and the number of cycles. It also plays sound notifications for each phase transition.

## **How to Use**

There are two ways to use this app:

### **1. As a Standalone Application (Recommended)**
If you're not a programmer (then what are you doing on GitHub? 😄) or you just don't want to deal with code, you can use the pre-built version:

1. Locate the **`dist`** folder.
2. Move it anywhere on your PC.
3. Inside `dist`, create a shortcut for **`gui.exe`** and place it on your Desktop.
4. Double-click the shortcut and enjoy your fully functional Pomodoro app! 🎉

### **2. Running from Source Code**
If you're comfortable with coding or want to modify the app, you can run it directly from the source:

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/pomodoro-app.git  
   cd pomodoro-app
   ```
2. Create a virtual environment (optional but recommended):  
   ```sh
   python -m venv venv  
   source venv/bin/activate  # macOS/Linux  
   venv\Scripts\activate  # Windows  
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt  
   ```
4. Run the application:
   ```sh
   python gui.py  
   ```

---

## **Customization**
You can modify work/break durations and sound notifications directly in the app's interface. No need to edit the code!

---

## **Building an Executable (.exe)**
If you want to create your own `.exe` file:

1. Install **PyInstaller**:  
   ```sh
   pip install pyinstaller  
   ```
2. Run the build command:  
   ```sh
   pyinstaller --onefile --windowed --icon=icon.ico gui.py  
   ```
3. Your executable will be in the `dist` folder. Follow the first method above to set it up.

---

## **Features**
✅ Customizable work and break durations  
✅ Sound notifications  
✅ Simple and user-friendly interface  
✅ Standalone executable for easy use  
✅ Open-source and modifiable  

---

Enjoy your productivity boost! 💪⏳

