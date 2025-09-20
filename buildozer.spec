[app]
# (str) Title of your application
title = DroneApp

# (str) Package name
package.name = droneapp

# (str) Package domain (reverse domain notation)
package.domain = org.mershan

# (str) Source code directory (relative to buildozer.spec)
source.dir = .

# (str) Application version
version = 1.0.0

# (list) Requirements
requirements = python3,kivy

# (str) Entry point of the app
entrypoint = main.py

# (str) Icon of the app
icon.filename = %(source.dir)s/icon.png

# (bool) Copy the directory to the APK
copy_mkdir = True

# (list) Include additional files
source.include_exts = py,png,jpg,kv,txt

# (str) Orientation
orientation = portrait

# (bool) Presplash
presplash.filename = %(source.dir)s/presplash.png

# (str) Supported Android API level
android.api = 33

# (str) Minimum SDK version
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (bool) Android logcat
android.logcat_filters = *:S python:D

# (bool) Android permissions (if needed)
android.permissions = INTERNET

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (bool) Android allow backup
android.allow_backup = true
