from fastapi import FastAPI
from langserve import add_routes
from pirate_speak.chain import chain as pirate_speak_chain


app = FastAPI()

add_routes(app, pirate_speak_chain, path="/pirate-speak")


@app.get("/")
def root():
    return {
        "message": "Welcome to the langserve server! More information and routes can be found at /docs. 🦜 🏓",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
