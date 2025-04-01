from fastapi import FastAPI
import logfire
logfire.configure(
    send_to_logfire=True,
    token="pylf_v1_us_4X7CrfGRqNLwFLQCGjVBNZHF041vvKTZYP7FH4hkBQHw",
    service_name="starter-project"
)
app = FastAPI()


@app.get("/")
def read_root():
    logfire.info("Processing hello world request")
    with logfire.span("greeting-preparation"):
        logfire.info("Prepare greeting Message")
        greeting = "Hello World!"

    logfire.info("Sending response", message=greeting)
    return {"message": greeting}


if __name__ == "__main__":
    logfire.info("starting hello world application")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
