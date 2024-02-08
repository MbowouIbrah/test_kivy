[app]
# (str) Title of your application
title = Transdocs

# (str) Package name
package.name = my.kivymd.app

# (str) Package domain (needed for android/ios packaging)
package.domain = org.myapp.kivymd

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (str) Application versioning (method 1)
# version = 0.1

# (str) Application versioning (method 2)
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,kivymd

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (bool) Run the application in debug mode
#debug.port = 5678

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (str) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so

# (str) Android additional libraries to copy into libs/x86
#android.add_libs_x86 = libs/android_x86/*.so

# (list) Permissions
#android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
#android.api = 27

# (int) Minimum API your APK will support.
#android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 17c

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
#android.skip_update = False

# (str) Bootstrap to use for android builds
# android.bootstrap = sdl2

# (int) Port used to transfer the application
#port = 9999

# (str) Log level (debug, info, warning, error, critical)
log_level = 2

# (str) Enable Kivy launcher
#kivy.landscape = 1
#kivy.icon = %(app_icon)s
#kivy.window = 1

# (str) iOS settings
#ios.ipad_support = 0
#ios.iphone_support = 1
#ios.requires_fullscreen = 1

# (str) OSX settings
#osx.icon = %(app_icon)s

# (str) The release mode (either dev, debug, release)
# Controls how the application is packaged and starts
mode = release

# (list) Python modules to include (let empty to include all)
#python_modules =

# (str) Application entry point
# Some recipes require a specific main filename.
# Set relative to source directory.
#main.filename = main.py

# (str) Text to display in the emulator toolbar
#android.emulator_title = %(app_title)s

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) The OUYA Console category of the app
#ouya.category = GAME

# (str) The default orientation of the app on OUYA
#ouya.orientation = landscape

# (list) Permissions for the OUYA console
#ouya.permissions = INTERNET

# (str) If you need to insert variables into your AndroidManifest.xml file,
# you can do so with the manifestPlaceholders property.
#manifest_placeholders = key1=value1,key2=value2

# (bool) If set to True, save packaging to cache directory
#packaging.cache = False

# (str) Path to a custom hook for python-for-android
#python-for-android.hook = my_hook_directory/hook_name.py

# (str) Bootstrap to use for python-for-android
#python-for-android.bootstrap = sdl2

# (list) List of build dependencies to be checked before build
#python-for-android.depends = sdl2_ttf,jpeg

# (str) The backend to use for python-for-android
#python-for-android.backend = opengl

# (str) The directory in which to find the python-for-android source
# Use this to locally test a new version of python-for-android
#python-for-android.source_dir = /home/user/python-for-android