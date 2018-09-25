clean:
	buildozer android clean
	rm **/*.pyc **/**/*.pyc **/**/**/*.pyc

init:
	buildozer init

update:
	buildozer android update

debug:
	buildozer android debug deploy run

release:
	buildozer android release deploy run

deploy: release
	buildozer android deploy

run: deploy
	buildozer android run
