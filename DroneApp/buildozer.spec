[app]
title = DroneApp
package.name = droneapp
package.domain = com.mershanpeter
source.dir = .                  # <-- REQUIRED inside [app]
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,kivy_garden.joystick,requests
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
android.api = 33
android.minapi = 21
android.ndk = 25b
