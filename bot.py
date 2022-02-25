from vkbottle.user import User, Message
from config import token, trigger, ans

session = User(token=token)


@session.on.message(text=trigger)
async def answer(event: Message):
    event.ctx_api.messages.send(peer_id=event.peer_id, text=ans)

session.run_forever()
