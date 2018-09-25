[app]


title = Tasks
version = 0.0.7
package.name = tasks
package.domain = io.github.juacywillian

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,png
source.include_patterns = assets/*,image/*
source.exclude_dirs = tests, bin
presplash.filename = %(source.dir)s/assets/image/presplash.png
icon.filename = %(source.dir)s/assets/image/icon.png

requirements = python,kivy,git+https://github.com/JuacyWillian/kivymd-updates.git,peewee,enum34,sqlite3

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.presplash_color = #008080

[buildozer]
log_level = 2
warn_on_root = 1
build_dir = /home/kivy/
