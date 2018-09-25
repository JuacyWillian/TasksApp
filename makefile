clean:
	buildozer android clean

init:
	buildozer init

update:
	buildozer android update

debug:
	buildozer android debug deploy run

release:
	buildozer android release deploy run
