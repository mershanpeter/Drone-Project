[app]
title = DroneApp
package.name = droneapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

orientation = portrait
fullscreen = 0
entrypoint = main.py

requirements = python3,kivy,kivy_garden.joystick
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
