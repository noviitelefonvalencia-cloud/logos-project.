[app]
title = ColdChainApex
package.name = apex
package.domain = net.logos
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,c,h,sh
version = 6.3.8
requirements = python3,kivy==2.2.1,requests,cryptography

# Android specific
android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_path = 
android.sdk_path = 
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = False

# Build options
p4a.branch = master
