setup:
	powershell .\setup.ps1
	powershell . .\env\Scripts\activate
build-dev:
	docker build -t gityaml-dev -f docker/dev/dockerfile .