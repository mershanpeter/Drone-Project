[app]
title = DroneApp
package.name = droneapp
package.domain = com.mershanpeter
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,kivy_garden.joystick,requests
orientation = portrait

fullscreen = 0
entrypoint = main.py
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
