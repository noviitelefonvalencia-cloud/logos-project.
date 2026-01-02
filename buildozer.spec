[app]
# (str) Title of your application
title = LogosProject

# (str) Package name
package.name = logosproject

# (str) Package domain (needed for android packaging)
package.domain = org.logos

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let's be specific)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Добавляем requests и cryptography, так как они часто нужны в таких проектах
requirements = python3,kivy==2.3.0,requests,cryptography,certifi

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android SDK version to use
android.sdk = 33

# (list) Architecture to build for (arm64-v8a обязателен для Google Play)
android.archs = arm64-v8a

# (bool) use build-tools from the sdk (keep it 1)
android.skip_update = False

# (bool) If True, then skip trying to update the Android sdk build-tools
android.accept_sdk_license = True

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
