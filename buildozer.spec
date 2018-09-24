[app]

title = Tasks
package.name = tasks
package.domain = io.github.juacywillian

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,png
source.include_patterns = assets/*,image/*
source.exclude_dirs = tests, bin

version = 0.0.1

presplash.filename = %(source.dir)s/assets/image/presplash.png
icon.filename = %(source.dir)s/assets/image/icon.png

orientation = portrait

requirements = python,kivy,git+https://gitlab.com/kivymd/kivymd.git,peewee


osx.python_version = 3
osx.kivy_version = 1.10.1

fullscreen = 0


[buildozer]
log_level = 2
warn_on_root = 1
build_dir = /home/kivy/
