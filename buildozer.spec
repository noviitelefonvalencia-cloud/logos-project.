[app]
title = Vessel
package.name = vessel
package.domain = org.vessel.ether
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,pub,so
source.include_patterns = assets/*,lib/*,key.pub
version = 1.0.4

requirements = python3,kivy==2.2.1,pillow,hostpython3,ctypes

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = False

# Permission for the vault resonance
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# SDK/NDK sync with Workflow v.118
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.ndk_path = ~/.buildozer/android/platform/android-ndk-r25b
android.sdk_path = ~/.buildozer/android/platform/android-sdk

# Infrastructure
p4a.branch = master
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
