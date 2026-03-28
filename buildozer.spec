[app]
title = MDT 97
package.name = mdt97
version = 1.0
requirements = python3,kivy,cython

[buildozer]
# (str) Android API version to use
android.api = 21

# (str) Android API version to use for the application
android.minapi = 21
android.targetapi = 33

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
