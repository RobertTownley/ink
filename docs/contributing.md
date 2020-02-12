# Contributing

Thank you so much for your interest in contributing to Django Ink.  Whether you're
hoping to test out functionality, write documentation, add new features, code out
tests, open issues, or something entirely different, it's greatly appreciated.


## Getting Started
First, read our [code of conduct](code_of_conduct.md).

Next, confirm that you have recent versions of both `docker` and `docker-compose`
installed locally. Try to have `docker` >= 18.09, and `docker-compose` >= 1.23.
You can confirm that these are installed with:
```
docker --version
docker-compose --version
```

Once you have docker installed, clone down this repository and build the required images:
```
mkdir -p ~/Projects/ink/
cd ~/Projects/ink/
git clone git@github.com:RobertTownley/ink.git
docker-compose build
``` 

Run `docker-compose up` and visit `localhost:8000/admin` in your web browser. If you
don't see the Django Admin login page, you may need to wait a few minutes. If it still
doesn't come up, confirm that you don't have any processes running on ports 8000 or 9005.
And if you continue to experience issues, open an issue in GitHub.
