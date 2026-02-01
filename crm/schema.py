import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from crm.models import Product

from .models import Customer


class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
        fields = ("id", "name", "email", "phone")


class Query(graphene.ObjectType):
    all_customers = graphene.List(CustomerType)

    def resolve_all_customers(self, info):
        return Customer.objects.all()


class CreateCustomer(graphene.Mutation):
    customer = graphene.Field(CustomerType)

    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String(required=True)

    def mutate(self, info, name, email, phone):
        if Customer.objects.filter(email=email).exists():
            raise GraphQLError("Email already exists")

        customer = Customer.objects.create(
            name=name,
            email=email,
            phone=phone
        )
        return CreateCustomer(customer=customer)

class UpdateLowStockProducts(graphene.Mutation):
    products = graphene.List(lambda: ProductType)
    message = graphene.String()

    def mutate(self, info):
        products = Product.objects.filter(stock__lt=10)

        for p in products:
            p.stock += 10
            p.save()

        return UpdateLowStockProducts(products=products, message="updated")


class Mutation(graphene.ObjectType):
    create_customer = CreateCustomer.Field()
    update_low_stock_products = UpdateLowStockProducts.Field()


