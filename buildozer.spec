[app]
# (str) Title of your application
title = Apex_Vessel

# (str) Package name
package.name = logos_project

# (str) Package domain (for mask purposes)
package.domain = org.vessel.ether

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let extensions cover C/SO files)
source.include_exts = py,png,jpg,kv,atlas,c,h,so

# (str) Application versioning
version = 0.1.1

# (list) Application requirements
# Cython is pinned to match GitHub environment
requirements = python3,kivy,cython==0.29.33,cryptography

# (str) Supported orientation
orientation = portrait

# (list) Permissions
android.permissions = INTERNET,CAMERA

# (int) Target Android API
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version (stable for C-compilation)
android.ndk = 25b

# (bool) Skip the license prompt
android.accept_sdk_license = True

# (list) The Android architectures to build for
android.archs = arm64-v8a

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android logcat filters (Diagnostic Mode)
android.logcat_filters = *:S python:D vessel:D

# [app:custom] Section for "Moriarty" trace
m_signature = 0x88f2e77b10a1

[buildozer]
# (int) Log level (2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False)
warn_on_root = 1
