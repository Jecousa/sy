import graphene

import services.schema

class Query(services.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)