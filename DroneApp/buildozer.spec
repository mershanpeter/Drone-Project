[app]
# (str) Title of your application
title = DroneApp

# (str) Package name
package.name = droneapp

# (str) Package domain (reverse DNS style)
package.domain = org.mershan

# (str) Source code where main.py is located
source.dir = .

# (str) Main Python file
source.main = main.py

# (str) Version of your app
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy,kivy_garden.joystick

# (str) Icon of the app (optional)
icon.filename = %(source.dir)s/icon.png

# (bool) Indicate if the app is fullscreen
fullscreen = 0

# (str) Supported orientation: portrait, landscape, all
orientation = portrait

# (list) Permissions (since your app uses UDP)
android.permissions = INTERNET

# (int) Minimum API level
android.minapi = 21

# (int) Target API level
android.api = 33

# (int) Android SDK build tools version
android.sdk = 33

# (str) Android NDK version
android.ndk = 25b

# (str) Android entry point (do not change)
android.entrypoint = org.kivy.android.PythonActivity

# (str) Presplash image (optional)
presplash.filename = %(source.dir)s/presplash.png

# (bool) Allow debug build
debug = 1
