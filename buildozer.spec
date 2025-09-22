[app]

# (str) Title of your application
title = MyApp

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (str) The main .py file to use as the main entry point
source.main = main.py

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (portrait, landscape, all)
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# (int) Target API
android.api = 33

# (int) Minimum API your app will support
android.minapi = 21

# (int) Android SDK version to compile with
android.sdk = 33

# (int) Android NDK version
android.ndk = 25b

# (bool) Release build?
android.release = 0

# (str) Icon
# icon.filename = %(source.dir)s/icon.png

[buildozer]

# (str) Log level
log_level = 2

# (str) Build directory
build_dir = ./build

# (bool) Clean build each time
clean_build = 1

# (bool) Enable GitHub Actions optimized build
# This allows automatic download of SDK/NDK during CI
android.gitignore = 0
