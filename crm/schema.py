import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay
from graphene_django import DjangoObjectType
from .models import Customer

class CustomerNode(DjangoObjectType):
    class Meta:
        model = Customer
        interfaces = (relay.Node,)
        fields = ("id", "name", "email", "phone")

class Query(graphene.ObjectType):
    all_customers = DjangoFilterConnectionField(CustomerNode)

    def resolve_all_customers(root, info):
        return Customer.objects.all()

class Mutation(graphene.ObjectType):
    create_customer = CreateCustomer.Field()

class CreateCustomer(graphene.Mutation):
    customer = graphene.Field(CustomerType)

    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String(required=True)

    def mutate(self, info, name, email, phone):
        customer = Customer(name=name, email=email, phone=phone)
        customer.save()
        return CreateCustomer(customer=customer)
