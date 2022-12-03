import graphene

from graphene_django import DjangoObjectType,DjangoListField
from .models import Article,Person


class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        fields = "__all__"
# class BookTye(DjangoObjectType):
#     class Meta:
#         model = Book
#         fields = "__all__"
        
class AuthorType(DjangoObjectType):
    class Meta:
        model = Person
        fields = "__all__"


class Query(graphene.ObjectType):
    all_articles = graphene.List(ArticleType)
    author = graphene.Field(AuthorType,person_name = graphene.String())

    def resolve_all_articles(root,info,**kwargs):
        return Article.objects.all()

    def resolve_author(root,info,person_name):
        return Person.objects.get(name=person_name)


schema = graphene.Schema(query=Query)