from rest_framework import serializers
from core.abstract.serializers import AbstractSerializer
from core.post.serializers import PostSerializer
from core.user.serializers import UserSerializer
from core.user.models import User
from core.post.models import Post
from core.comment.models import Comment

class CommentSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset = User.objects.all(),slug_field="public_id")
    post = serializers.SlugRelatedField(queryset = Post.objects.all(),slug_field="public_id")

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # rep["author"] = UserSerializer(User.objects.get_object_by_public_id(rep["author"])).data
        rep["post"] = PostSerializer(Post.objects.get_object_by_public_id(rep["post"])).data
        return rep
    def validate_post(self,value):
        if self.instance:
            return self.instance.post
        return value
    def update(self, instance, validated_data):       
        if not instance.edited:
            validated_data['edited'] = True       
        instance = super().update(instance,validated_data)       
        return instance

    class Meta:
        model = Comment
        fields = ['id','author','post','body','edited','created','updated']
        read_only_fields = ["edited"] 
    
