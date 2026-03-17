[app]

# (str) Title of your application
title = IR Interpreter

# (str) Package name
package.name = irinterpreter

# (str) Package domain (needed for android packaging)
package.domain = org.science

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let's include everything)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0

# --- MODIFIED REQUIREMENTS ---
# This includes KivyMD for the modern look and Pillow for images
requirements = python3, kivy==2.3.0, kivymd, pillow

# (str) Custom source for any requirements
# requirements.source.kivymd = https://github.com/kivymd/KivyMD/archive/master.zip

# (str) Presumes you uploaded icon.png to the main folder
icon.filename = %(source.dir)s/icon.png

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (list) The Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow backup
android.allow_backup = True

# (bool) Accept SDK license
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
