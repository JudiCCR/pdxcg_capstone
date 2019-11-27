from channels.generic.websocket import WebsocketConsumer
import json

class CommConsumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()
        print('connection successful')

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        

        self.send(text_data=json.dumps({
            'message':message
        }))