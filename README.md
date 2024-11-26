# WIP

## Build and run the docker image
```
docker build -t <my-container> .
docker run <my-container>
```

## Install Flask
```
py -3 -m venv .venv
.venv\Scripts\activate
pip install Flask
```

If execution policy is restricted, run the following on an elevated Powershell:
```
Set-ExecutionPolicy -ExecutionPolicy Unrestricted
Get-ExecutionPolicy
```