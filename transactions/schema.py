import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import workmodel, Parties, ProgramType, Programs
from django.http import request

class workmodelType(DjangoObjectType):
    class Meta:
        model = workmodel
        fields = '__all__'

class PartiesType(DjangoObjectType):
    class Meta:
        model = Parties
        fields = '__all__'

class ProgramtypeType(DjangoObjectType):
    class Meta:
        model = ProgramType
        fields = '__all__'

class ProgramsType(DjangoObjectType):
    class Meta:
        model = Programs
        fields = '__all__'

class Query(graphene.ObjectType):
    all_workmodel = DjangoListField(workmodelType)
    all_parties = DjangoListField(PartiesType)
    all_programtypes = DjangoListField(ProgramtypeType)
    all_programs = DjangoListField(ProgramsType)

class workmodelInput(graphene.InputObjectType):
    id = graphene.ID()
    description = graphene.String(required=True)
    workflow = graphene.Boolean(required=True)

class workmodelType_create(graphene.Mutation):
    class Arguments:
        _model = workmodelInput(required=True)
    
    workmodel1 = graphene.Field(workmodelType)

    @classmethod
    def mutate(cls, root, info, _model=None):
        _workmodel1 = workmodel.objects.create(**_model)
        return workmodelType_create(workmodel1=_workmodel1)

class workmodelType_update(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        description = graphene.String()
        workflow = graphene.Boolean()
    
    workmodel1 = graphene.Field(workmodelType)

    @classmethod
    def mutate(cls, root, info, description, workflow, id):
        workmodel1 = workmodel.objects.get(id=id)
        workmodel1.description = description
        workmodel1.workflow = workflow
        workmodel1.save()
        return workmodelType_update(workmodel1=workmodel1)

class workmodelType_delete(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    workmodel1 = graphene.Field(workmodelType)

    @classmethod
    def mutate(cls, root, info, id):
        workmodel1 = workmodel.objects.get(id=id)
        workmodel1.delete()
        return workmodelType_delete(workmodel1=workmodel1)

class PartiesType_create(graphene.Mutation):
    class Arguments:
        model_id = graphene.Int()
        customer_id = graphene.String(required=True)
        account_number = graphene.String(required=True)
        name = graphene.String(required=True)
        base_currency = graphene.String(required=True)
        address_line_1 = graphene.String(required=True)
        address_line_2 = graphene.String(required=True)
        city = graphene.String(required=True)
        state = graphene.String(required=True)
        zipcode = graphene.String(required=True)
        country_code = graphene.String(required=True)
        customer = graphene.Boolean(required=True)

    parties = graphene.Field(PartiesType)

    def mutate(self, root, model_id, customer_id, account_number, name, base_currency, address_line_1, address_line_2, city, state, zipcode, country_code, customer):

        _model = workmodel.objects.get(id=model_id)

        if not _model:
            raise Exception('Invalid Model')
        
        _party = Parties.objects.create(model_type=_model,customer_id=customer_id, account_number=account_number, name=name, base_currency=base_currency, address_line_1=address_line_1, address_line_2=address_line_2, city=city, state=state, zipcode=zipcode, country_code=country_code, customer=customer)
        
        return PartiesType_create(parties=_party)

class PartiesType_update(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        model_id = graphene.Int()
        customer_id = graphene.String()
        account_number = graphene.String()
        name = graphene.String()
        base_currency = graphene.String()
        address_line_1 = graphene.String()
        address_line_2 = graphene.String()
        city = graphene.String()
        state = graphene.String()
        zipcode = graphene.String()
        country_code = graphene.String()
        customer = graphene.Boolean()

    parties = graphene.Field(PartiesType)

    def mutate(self, root, id, model_id, customer_id, account_number, name, base_currency, address_line_1, address_line_2, city, state, zipcode, country_code, customer):

        _model = workmodel.objects.get(id=model_id)

        if not _model:
            raise Exception("Invalid Model")
        
        _party = Parties.objects.get(id=id)
        _party.model_type = _model
        _party.customer_id = customer_id
        _party.account_number = account_number
        _party.name = name
        _party.base_currency = base_currency
        _party.address_line_1 = address_line_1
        _party.address_line_2 = address_line_2
        _party.city = city
        _party.state = state
        _party.zipcode = zipcode
        _party.country_code = country_code
        _party.customer = customer
        _party.save()
        return PartiesType_update(parties=_party)

class PartiesType_delete(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    parties = graphene.Field(PartiesType)

    def mutate(self, root, id):
        _party = Parties.objects.get(id=id)
        _party.delete()
        return PartiesType_delete(parties=_party)

class Mutation(graphene.ObjectType):
    create_workmodel = workmodelType_create.Field()
    update_workmodel = workmodelType_update.Field()
    delete_workmodel = workmodelType_delete.Field()

    create_parties = PartiesType_create.Field()
    update_parties = PartiesType_update.Field()
    delete_parties = PartiesType_delete.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)