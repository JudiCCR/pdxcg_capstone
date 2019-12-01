from channels.generic.websocket import WebsocketConsumer
from .models import User, Comment, Post
import json

class CommConsumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()
        print('connection successful')

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)

        if text_data_json['type'] == 'comment':
            comment = text_data_json['commText']
            user = User.objects.get(id=text_data_json['userID'])
            post = Post.objects.get(id=text_data_json['postID'])
            comment_object = Comment.objects.create(user=user, post=post, text=comment)
            comment_object.save()
            self.send(text_data=json.dumps({
                'type': 'comment',
                'message':text_data_json['commText'],
                'user':user.username,
                'comment':comment,
            }))
        
        elif text_data_json['type'] == 'alteration':
            self.send(text_data=json.dumps({
                'type': 'alteration',
                'userID': text_data_json['userID'],
                'whiteboard': text_data_json['whiteboard'],
            }))    
        
        