import graphene

from graphene_django import DjangoListField,DjangoObjectType
from .models import Book

class BookTye(DjangoObjectType):
    class Meta:
        model = Book
        fields = "__all__"

class Query(graphene.ObjectType):
    all_books = graphene.List(BookTye)
    book = graphene.Field(BookTye,book_id=graphene.Int())


    def resolve_all_books(self,info,**kwargs):
        return Book.objects.All()

    def resolve_book(self,info,book_id):
        return Book.objects.get(pk=book_id)

class BookInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    author = graphene.String()
    year_published = graphene.String()
    review = graphene.Int()


class CreateBook(graphene.Mutation):
    class Arguments:
        b_data = BookInput(required=True)

    b = graphene.Field(BookTye)

    @staticmethod
    def mutate(root,info,b_data=None):
        b_instance = Book(
            title = b_data.title,
            author = b_data.author,
            year_published = b_data.year_published,
            review = b_data.review
        )
        b_instance.save()
        return CreateBook(b=b_instance)

class UpdateBook(graphene.Mutation):
    class Arguments:
        book_data = BookInput(required=True)

    book = graphene.Field(BookTye)

    @staticmethod
    def mutate(root, info, book_data=None):
        book_instance = Book.objects.get(pk=book_data.id)
        
        if book_instance:
            book_instance.title = book_data.title
            book_instance.author = book_data.author
            book_instance.year_published = book_data.year_published
            book_instance.review = book_data.review
            book_instance.save()
        
            return UpdateBook(book=book_instance)

        return UpdateBook(book=None)

class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    book = graphene.Field(BookTye)

    @staticmethod
    def mutate(root, info, id):
        book_instance = Book.objects.get(pk=id)
        book_instance.delete()

        return None



class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()







schema = graphene.Schema(query=Query,mutation=Mutation)
