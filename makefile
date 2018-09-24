clean:
	rm **/*.pyc **/**/*.pyc **/**/**/*.pyc

docker-build:
	sudo docker build -t diegodukao/python3-kivy-buildozer .

docker-run:
	sudo docker run --rm -it --privileged -v $PWD:/src -v /dev/bus/usb:/dev/bus/usb -v buildozer:/home/kivy diegodukao/python3-kivy-buildozer /bin/bash

buildozer-init:
	buildozer init

update:
	buildozer android update

android-debug: update
	buildozer android debug > log.txt