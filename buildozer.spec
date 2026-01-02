[app]
title = LogosProject
package.name = logosproject
package.domain = org.logos
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,sh
version = 0.1
requirements = python3,kivy,requests,cryptography

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a

# Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Android API (Stability focus)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33

# Build options
android.logcat_filters = *:S python:D
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
