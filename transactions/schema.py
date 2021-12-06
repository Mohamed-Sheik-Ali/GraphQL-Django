import graphene
from graphene.types import decimal
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

class Program_Type(DjangoObjectType):
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
    all_programtypes = DjangoListField(Program_Type)
    all_programs = DjangoListField(ProgramsType)

class workmodelInput(graphene.InputObjectType):
    id = graphene.ID()
    description = graphene.String(required=True)
    workflow = graphene.Boolean(required=True)

class workmodelType_create(graphene.Mutation):
    class Arguments:
        _model = workmodelInput(required=True)
    
    workmodel1 = graphene.Field(workmodelType)

    def mutate(self, root, _model=None):
        _workmodel1 = workmodel.objects.create(**_model)
        return workmodelType_create(workmodel1=_workmodel1)

class workmodelType_update(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        description = graphene.String()
        workflow = graphene.Boolean()
    
    workmodel1 = graphene.Field(workmodelType)

    
    def mutate(self, root, description, workflow, id):
        workmodel1 = workmodel.objects.get(id=id)
        workmodel1.description = description
        workmodel1.workflow = workflow
        workmodel1.save()
        return workmodelType_update(workmodel1=workmodel1)

class workmodelType_delete(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    workmodel1 = graphene.Field(workmodelType)

    def mutate(self, root, id):
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

class createProgramType(graphene.Mutation):
    class Arguments:
        description = graphene.String(required=True)
    
    _program_type = graphene.Field(Program_Type)

    def mutate(self, root, description):
        _programtype = ProgramType.objects.create(description=description)
        return createProgramType(_program_type=_programtype)

class updateProgramType(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        description = graphene.String(required=True)
    
    _program_type = graphene.Field(Program_Type)

    def mutate(self, root, id, description):
        _programtype = ProgramType.objects.get(id=id)
        _programtype.description = description
        _programtype.save()
        return updateProgramType(_program_type=_programtype)

class deleteProgramType(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    _program_type = graphene.Field(Program_Type)

    def mutate(self, root, id):
        _programtype = ProgramType.objects.get(id=id)
        _programtype.delete()
        return deleteProgramType(_program_type=_programtype)

class createPrograms(graphene.Mutation):
    class Arguments:
        model_id = graphene.Int()
        party_id = graphene.Int()
        programtype_id = graphene.Int()
        finance_request_type = graphene.Boolean(required=True)
        currency = graphene.String(required=True)
        max_total_limit = graphene.Int(required=True)
        expiry = graphene.Date(required=True)
        max_finance_percentage = graphene.Int(required=True)
        max_age_for_repayment = graphene.Int()
        minimum_period = graphene.Int()
        maximum_period = graphene.Int()
        minimum_amount_currency = graphene.String(required=True)
        minimum_amount = graphene.Int(required=True)
        financed_amount = graphene.Int(required=True)
        balance_amount = graphene.Int(required=True)
        grace_period = graphene.Int()
        interest_type = graphene.Boolean(required=True)
        interest_rate = graphene.Int(required=True)
        margin = graphene.Int(required=True)

    _programs = graphene.Field(ProgramsType)

    def mutate(self, root, model_id, party_id, programtype_id, finance_request_type, currency, max_total_limit, expiry, max_finance_percentage, max_age_for_repayment, minimum_period, maximum_period,
    minimum_amount_currency, minimum_amount, financed_amount, balance_amount, grace_period, interest_type, interest_rate, margin):
        model = workmodel.objects.get(id=model_id)
        party = Parties.objects.get(id=party_id)
        programtype = ProgramType.objects.get(id=programtype_id)

        if not model and not party and not programtype:
            raise Exception("Invalid Details")
        
        _program = Programs.objects.create(model=model, party=party, program_model=programtype, finance_request_type=finance_request_type, currency=currency, max_total_limit=max_total_limit, expiry=expiry, max_finance_percentage=max_finance_percentage, max_age_for_repayment=max_age_for_repayment, minimum_period=minimum_period, maximum_period=maximum_period, minimum_amount_currency=minimum_amount_currency, minimum_amount=minimum_amount, financed_amount=financed_amount, balance_amount=balance_amount, grace_period=grace_period, interest_type=interest_type, interest_rate=interest_rate, margin=margin)
        return createPrograms(_programs = _program)

class updatePrograms(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        model_id = graphene.Int()
        party_id = graphene.Int()
        programtype_id = graphene.Int()
        finance_request_type = graphene.Boolean(required=True)
        currency = graphene.String(required=True)
        max_total_limit = graphene.Int(required=True)
        expiry = graphene.Date(required=True)
        max_finance_percentage = graphene.Int(required=True)
        max_age_for_repayment = graphene.Int()
        minimum_period = graphene.Int()
        maximum_period = graphene.Int()
        minimum_amount_currency = graphene.String(required=True)
        minimum_amount = graphene.Int(required=True)
        financed_amount = graphene.Int(required=True)
        balance_amount = graphene.Int(required=True)
        grace_period = graphene.Int()
        interest_type = graphene.Boolean(required=True)
        interest_rate = graphene.Int(required=True)
        margin = graphene.Int(required=True)

    _programs = graphene.Field(ProgramsType)

    def mutate(self, root, id, model_id, party_id, programtype_id, finance_request_type, currency, max_total_limit, expiry, max_finance_percentage, max_age_for_repayment, minimum_period, maximum_period,
    minimum_amount_currency, minimum_amount, financed_amount, balance_amount, grace_period, interest_type, interest_rate, margin):
        model = workmodel.objects.get(id=model_id)
        party = Parties.objects.get(id=party_id)
        programtype = ProgramType.objects.get(id=programtype_id)

        _program = Programs.objects.get(id=id)
        _program.model = model
        _program.party = party
        _program.program_model = programtype
        _program.finance_request_type = finance_request_type
        _program.currency = currency
        _program.max_total_limit = max_total_limit
        _program.expiry = expiry
        _program.max_finance_percentage = max_finance_percentage
        _program.max_age_for_repayment = max_age_for_repayment
        _program.minimum_period = minimum_period
        _program.maximum_period = maximum_period
        _program.minimum_amount_currency = minimum_amount_currency
        _program.minimum_amount = minimum_amount
        _program.financed_amount = financed_amount
        _program.balance_amount = balance_amount
        _program.grace_period = grace_period
        _program.interest_type = interest_type
        _program.interest_rate = interest_rate
        _program.margin = margin

        _program.save()
        return updatePrograms(_programs = _program)

class deletePrograms(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    _programs = graphene.Field(ProgramsType)

    def mutate(self, root, id): 
        _program = Programs.objects.get(id=id)
        _program.delete()
        return deletePrograms(_programs=_program)

class Mutation(graphene.ObjectType):
    create_workmodel = workmodelType_create.Field()
    update_workmodel = workmodelType_update.Field()
    delete_workmodel = workmodelType_delete.Field()

    create_parties = PartiesType_create.Field()
    update_parties = PartiesType_update.Field()
    delete_parties = PartiesType_delete.Field()

    create_programtype = createProgramType.Field()
    update_programtype = updateProgramType.Field()
    delete_programtype = deleteProgramType.Field()

    create_program = createPrograms.Field()
    update_program = updatePrograms.Field()
    delete_program = deletePrograms.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)