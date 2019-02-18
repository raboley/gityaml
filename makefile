setup:
	powershell .\setup.ps1
	powershell . .\env\Scripts\activate
build-dev:
	docker build -t gityaml-dev -f docker/dev/dockerfile .
test:
	docker build -t gityaml-dev -f docker/dev/dockerfile .
	docker run --rm -v C:\Users\rboley\Desktop\git\azure_devops\git_to_yaml\reports:/reports gityaml-dev