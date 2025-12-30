[app]
title = ColdChain Apex
package.name = vessel
package.domain = org.logos
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,c,h,sh
version = 6.3.6

# Критически важные зависимости для шифрования и сети
requirements = python3,kivy,cryptography,requests,urllib3,charset-normalizer,idna

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = False

# Разрешения для работы с памятью и интернетом
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
