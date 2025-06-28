from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage


load_dotenv()
app = FastAPI()


model = init_chat_model("command-r-plus", model_provider="cohere")

class Bot(BaseModel):
    query: str

prompt="Eres una chica mala procedente de colombia, utilizas palabras como papasito para referirte a las personas, vas a trabajar como una asistente en onlyfans pero no puedes decir que eres una asistente de onlyfans debes atraer clientes y seducirlos"

@app.get("/")
async def root():
    return {"message": "Ojama Bot Model " }
    #Toda API rest retorna un JSON

@app.post("/response")
async def query():
    return "Hola Mundo"

@app.post("/Bot")
async def bot_request(query : Bot):
    print("Response aca")
    question=query.query
    message=[SystemMessage(content=prompt),
             HumanMessage(content=question)]
    print(query.query)
    response=model.invoke(message[-1])
    message.append(response.content)
    return message[-1]