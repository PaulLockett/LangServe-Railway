# LangServe  🦜 🏓 on Railway 🚂


## Deploy on Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/pW9tXP?referralCode=c-aq4K)

## Adding packages
Add the package to your local repo
```bash
# adding packages from 
# https://github.com/langchain-ai/langchain/tree/master/templates
langchain app add $PROJECT_NAME

# adding custom GitHub repo packages
langchain app add --repo $OWNER/$REPO
# or with whole git string (supports other git providers):
# langchain app add git+https://github.com/hwchase17/chain-of-verification

# with a custom api mount point (defaults to `/{package_name}`)
langchain app add $PROJECT_NAME --api_path=/my/custom/path/rag
```

Note: you remove packages by their api path

```bash
langchain app remove my/custom/path/rag
```

After adding the project to your local repo you need to add it to your project's
pyproject.toml

```bash
#
# other packages
$PROJECT_NAME = { path = "packages/$PROJECT_NAME" }
#
#
```

Then redeploy by pushing these changes to your git repo for this railway service.

## Setup LangSmith (Optional)
LangSmith will help us trace, monitor and debug LangChain applications. 
LangSmith is currently in private beta, you can sign up [here](https://smith.langchain.com/). 
If you don't have access, you can skip this section


```shell
# add these to your railway enviromental variables or your local .env
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=<your-api-key>
LANGCHAIN_PROJECT=<your-project>  
# if not specified, defaults to "default"
```