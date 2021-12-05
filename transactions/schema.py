import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import workmodel, Parties, ProgramType, Programs

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
        description = graphene.String(required=True)
    
    workmodel1 = graphene.Field(workmodelType)

    @classmethod
    def mutate(cls, root, info, description, id):
        workmodel1 = workmodel.objects.get(id=id)
        workmodel1.description = description
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

class PartiesInput(graphene.InputObjectType):
    model_type = graphene.Field(workmodelInput)
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

class PartiesType_create(graphene.Mutation):
    parties = graphene.Field(PartiesType)

    class Arguments:
        party_data = PartiesInput(required=True)

    @classmethod
    def mutate(cls, root, info, party_data = None):
        _parties = Parties.objects.create(**party_data)
        return PartiesType_create(parties=_parties)

class Mutation(graphene.ObjectType):
    create_workmodel = workmodelType_create.Field()
    update_workmodel = workmodelType_update.Field()
    delete_workmodel = workmodelType_delete.Field()

    create_parties = PartiesType_create.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)