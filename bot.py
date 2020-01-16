from fastapi import FastAPI
from pydantic import BaseModel
from utils import message_utils as mu


class Message(BaseModel):
    user_id: str
    message: str


app = FastAPI()


@app.post('/message')
def post_message(message: Message):
    if not message.user_id:
        return {"lol kek usera net"}
    if not message.message:
        return {"lol kek messaga net"}
    return mu.process_message(message.user_id, message.message)


@app.get('/history')
def post_message(user_id):
    return mu.get_history(user_id)
