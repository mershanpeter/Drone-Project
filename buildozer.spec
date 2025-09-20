[app]

# (str) Title of your application
title = DroneApp

# (str) Package name
package.name = droneapp

# (str) Package domain (unique)
package.domain = com.mershanpeter

# (str) Source directory where your main.py is located
source.dir = .

# (str) Main script filename
source.main = main.py

# (str) Version of your application
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy,pyjnius,kivy_garden.joystick,socket

# (str) Icon of the app
icon.filename = %(source.dir)s/icon.png

# (bool) Whether the app should be fullscreen
fullscreen = 0

# (str) Supported orientation: landscape, portrait
orientation = portrait

# (list) Permissions your app needs
android.permissions = INTERNET

# (bool) Use AndroidX
android.use_androidx = True

# (str) Minimum Android API your app supports
android.minapi = 21

# (str) Target Android API (leave Buildozer default, no need to set android.sdk)
# android.sdk = 33  <-- removed deprecated line

# (str) Android NDK version (optional)
# android.ndk = 25b

# (bool) Android logcat filters (optional)
log_level = 2

# (list) Exclude files/folders from the package
exclude_dirs = tests,docs

# (bool) Presplash (loading) image
# presplash.filename = %(source.dir)s/presplash.png
