from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .models import User, Comment, Post
from channels.db import database_sync_to_async
import json

class CommConsumer(AsyncJsonWebsocketConsumer):
    
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['post_id']
        self.room_group_name = 'table_%s' % self.room_name
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        print('connection successful')

    async def disconnect(self, close_code):
            self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def myfunc(self, event):
        print('$'*40)        
        content = {
            'type': 'websocket.send',
            'text': json.dumps(event['text']),
        }
        await self.send_json(content)

    async def receive(self, text_data):
        # print(text_data)
        # print(type(text_data))
        text_data_json = json.loads(text_data)
        # print(type(text_data_json))
        # print('message recieved by server')
        # print(text_data_json)

        if text_data_json['llama'] == 'comment':
            comment = text_data_json['commText']
            user = User.objects.get(id=text_data_json['userID'])
            post = Post.objects.get(id=text_data_json['postID'])
            await database_sync_to_async(self.save_comment)(comment, user, post)
            data = {
                'llama': 'comment',
                'message':text_data_json['commText'],
                'user':user.username,
                'userID':user.id,
                'comment':comment,
            }
            event = {
                'type': 'myfunc',
                'text': data,
            }
            await self.channel_layer.group_send(
                self.room_group_name,
                event,
                )
        elif text_data_json['llama'] == 'alteration':
            # print(text_data_json['userID'])
            data = {
                'llama': 'alteration',
                'userID': text_data_json['userID'],
                'message': text_data_json['whiteboard'],
            }
            event = {
                'type': 'myfunc',
                'text': data,
                }
            # print(type(data),'\n',data)
            await self.channel_layer.group_send(
                self.room_group_name,
                event
                )
        elif text_data_json['llama'] == 'saveAlter':
            postID = text_data_json['postID']
            whiteboard = text_data_json['whiteboard']
            await database_sync_to_async(self.save_alteration) (whiteboard, postID)
    
    def save_comment(self, comment, user, post):
        comment_object = Comment.objects.create(user=user, post=post, text=comment)
        comment_object.save()
    
    def save_alteration(self, whiteboard, postID):
        print(whiteboard)
        post = Post.objects.get(id=postID)
        post.text = whiteboard
        post.save()

        