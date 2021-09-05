
poetry export -f requirements.txt > requirements.txt --without-hashes
lib-one = {path = "../libs/lib-one" , develop = true}
poetry add ../libs/lib-one  
uvicorn main:app --reload

uvicorn main:app

 "python.venvPath": "~/Library/Caches/pypoetry/virtualenvs",
poetry config virtualenvs.in-project true
The virtualenv will be created inside the project path and vscode will recognize.

If you already have created your project, you need to re-create the virtualenv to make it appear in the correct place:

poetry env list  # shows the name of the current environment
poetry env remove <current environment>
poetry install  # will create a new environment using your updated configuration

https://dev.to/imsazzad/how-to-publish-and-use-your-python-package-in-and-from-private-bitbucket-or-github-3p4c



HANDLER_PATH_PREFIX=src/test_lambda/ ./node_modules/serverless/bin/serverless.js invoke local -f LambdaTest -p ./tests/resources/base_event.yml


functions:
  LambdaTest:
    handler: ${env:HANDLER_PATH_PREFIX, ""}handler.handler
    module: src/test_lambda
    package:
      include:
        - src/test_lambda/**


# python mono repo sample 

## what is this?

This is a sample to implement a multi-project structure in python.  
I am using poetry to manage my dependencies.  

## project setup

you have to install poetry 1.0.8 version

```bash
cd python-monorepo
poetry install
``` 

## generate new project

```bash
cd python-monorepo/projects
poetry new {new project name}
cd {new project name}
poetry add ./../../libs/{project dependency lib module name}
```


## project structure

```
.
├── README.md
├── libs
│   ├── lib-one
│   └── logger
├── poetry.lock
├── projects
│   ├── __init__.py
│   ├── project-one
│   └── project-two
└── pyproject.toml
```

`/projects`

Project code (Python modules) go here.  
Each project has its own dependencies.  

`lib`

Each lib specifies its dependencies.  
Each lib has its own dependencies.  


## reference

https://medium.com/opendoor-labs/our-python-monorepo-d34028f2b6fa
