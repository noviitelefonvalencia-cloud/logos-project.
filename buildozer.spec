[app]
title = Logos Project
package.name = logosproject
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,c,h,cpp
version = 0.1
requirements = python3,kivy

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a

# SDK/NDK configuration
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.0
android.accept_sdk_license = True
android.skip_update = True

# Forced path injection for GitHub Actions
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b

[buildozer]
log_level = 2
warn_on_root = 1
