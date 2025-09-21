[app]
# (str) Title of your application
title = DroneApp

# (str) Package name
package.name = droneapp

# (str) Package domain (reverse DNS style)
package.domain = org.mershan

# (str) Source code where the main.py file is located
source.dir = .

# (str) Main entry point of the app
source.main = main.py

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if permissions are required
android.permissions = INTERNET,ACCESS_WIFI_STATE

# (str) Icon of the app
icon.filename = icon.png

# (list) Presplash image
presplash.filename = presplash.png

# (str) Supported Android API
android.sdk_api = 33

# (str) Minimum Android API
android.minapi = 21

# (str) Target Android API
android.target = 33

# (str) Android SDK path
android.sdk_path = /home/runner/work/Drone-Project/Drone-Project/DroneApp/android-sdk

# (str) Android NDK path (leave blank to auto-download)
android.ndk_path =

# (str) Build-tools version (stable for Buildozer)
android.build_tools_version = 33.0.2

# (str) Java version
android.javac = 17

# (str) Python version
python3 = 3.10

# (bool) Allow backup of APKs
preserve_apk = False

# (bool) Use SDL2 backend
android.kivy_android = True

# (bool) Copy needed dependencies automatically
copy_mylibs = 1

# (str) Package format
android.arch = armeabi-v7a

# (bool) Whether to include debug symbols
android.debug = 1

# (bool) Enable splash screen
android.presplash_color = #FFFFFF

# (str) Additional environment variables (for CI/CD)
env =
    ANDROID_HOME=/home/runner/work/Drone-Project/Drone-Project/DroneApp/android-sdk
    PATH=/home/runner/work/Drone-Project/Drone-Project/DroneApp/android-sdk/cmdline-tools/latest/bin:/home/runner/work/Drone-Project/Drone-Project/DroneApp/android-sdk/platform-tools:$PATH

# (bool) Log build output
log_level = 2

# (str) Target architecture for the APK
android.archs = armeabi-v7a
