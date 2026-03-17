[app]

# (str) Title of your application
title = IR Interpreter

# (str) Package name
package.name = irinterpreter

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.3.0,kivymd,pillow,requests

# (str) Custom source folders for requirements
# Requirements can be installed from custom source directories
# requirements.source.kivymd = ../kivymd

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# WE HAVE COMMENTED THIS OUT TO FIX THE "FILE NOT FOUND" ERROR
# icon.filename = %(source.dir)s/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
# android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid downloads if the users already has it
android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only.
android.accept_sdk_license = True

# (str) Android entry point, default is to use start.py
# android.entrypoint = main.py

# (str) Android app theme, default is ok for Kivy
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the simple-type file chooser
# android.whitelist =

# (str) The format used to package the app for release mode (aab or apk)
android.release_artifact = apk

# (str) The format used to package the app for debug mode (aab or apk)
android.debug_artifact = apk

[buildozer]

# (int) log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
