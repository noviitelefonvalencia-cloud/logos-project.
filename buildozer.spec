[app]
title = Logos Apex
package.name = apex
package.domain = org.logos.apex
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,c,h
version = 0.1
requirements = python3,kivy,cryptography,hostpython3

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a
android.allow_backup = False

# Android specific configuration
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25c
android.accept_sdk_license = True
android.skip_setup = False

[buildozer]
log_level = 2
warn_on_root = 1
