[app]
title = LogosProject
package.name = logosproject
package.domain = org.logos

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1

# Updated requirements based on build analysis
requirements = python3,kivy==2.3.0,kivymd==1.1.1,pillow,requests,certifi,openssl,cython<3.0

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Target SDK and NDK optimization
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_path = 

# Performance and build stability
android.skip_update = False
android.accept_sdk_license = True
android.logcat_filters = *:S python:D

# Buildozer engine settings
p4a.branch = master
p4a.bootstrap = sdl2
