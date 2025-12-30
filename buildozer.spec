[app]
title = Logos Apex
package.name = apex
package.domain = org.logos
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,c,h,json,vessel
version = 6.3.8
requirements = python3,kivy,cryptography,requests

# Android конфигурация
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
# ВАЖНО: Путь подстроен под стандарт GitHub Actions
android.ndk_path = /home/runner/work/${{ github.event.repository.name }}/${{ github.event.repository.name }}/android-ndk-r25b
android.accept_sdk_license = True
android.archs = arm64-v8a
android.skip_update = False

[buildozer]
log_level = 2
warn_on_root = 1
