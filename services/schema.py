import graphene 

from graphene_django.types import DjangoObjectType

from services.models import PlayMusic, SearchMusic

class PlayMusicType(DjangoObjectType):
    class Meta:
        model = PlayMusic

class SearchMusicType(DjangoObjectType):
    class Meta:
        model = SearchMusic

class Query(object):
    playmusic = graphene.Field(PlayMusicType,
                                id=graphene.Int(),
                                name=graphene.String(),
                                music_type=graphene.String()
        )
    all_playmusic = graphene.List(PlayMusicType)
    all_searchmusic = graphene.List(SearchMusicType)

    def resolve_playmusic(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
        musictype = kwargs.get('music_type')

        if id is not None:
            return PlayMusic.objects.get(pk=id)

        if name is not None:
            return PlayMusic.objects.get(name=name)

        if musictype is not None:
            return PlayMusic.objects.get(musictype=musictype)

        return None


    def resolve_all_playmusic(self, info, **kwargs):
        return PlayMusic.objects.all()
    
    def resolve_all_searchmusic(self, info, **kwargs):
        return SearchMusic.objects.all()

