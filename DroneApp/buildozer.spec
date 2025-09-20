[app]
[app]
title = DroneApp
package.name = droneapp
package.domain = com.mershanpeter
source.include_exts = py,png,jpg,kv,atlas
version = 1.0          # <---- Add this line
requirements = python3,kivy


orientation = portrait
fullscreen = 0
entrypoint = main.py

requirements = python3,kivy,kivy_garden.joystick
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
