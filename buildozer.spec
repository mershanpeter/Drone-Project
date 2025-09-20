[app]
# (str) Title of your application
title = DroneApp

# (str) Package name
package.name = droneapp

# (str) Package domain (unique)
package.domain = org.mershanpeter

# (str) Source code directory
source.dir = .

# (list) List of requirements
requirements = python3,kivy,kivy_garden.joystick,socket

# (str) Version
version = 1.0.0

# (str) Icon of the app
icon.filename = %(source.dir)s/icon.png

# (str) Entry point of your app
# main.py is your Kivy Python script
entrypoint = main.py

# (bool) Include all source files in the package
source.include_exts = py,png,jpg,kv,atlas

# (list) Permissions (for UDP / networking)
android.permissions = INTERNET

# (bool) Whether to copy the README and LICENSE
copy_metadata = True

# (list) Android orientation
orientation = portrait

[buildozer]
# (str) Path to build folder (temporary)
build_dir = ./.buildozer

# (str) Path to bin folder (APK output)
bin_dir = ./bin

[android]
# Target Android API
android.api = 33
# Minimum Android API
android.minapi = 21
# Java version
android.javac = 17
# Android SDK is auto-installed by p4a, no need to specify old config
