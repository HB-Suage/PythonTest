pytest
allure generate ./temp -o ./report --clean
Remove-Item -Path ./temp -Recurse -Force