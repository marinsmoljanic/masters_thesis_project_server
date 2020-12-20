# server/schema.py
import graphene
from graphene_django import DjangoObjectType
from graphene import Argument

from server.evidencija.models import Person, PersonRole, Project, Role


class PersonType(DjangoObjectType):
    class Meta:
        model = Person


class PersonRoleType(DjangoObjectType):
    class Meta:
        model = PersonRole


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project


class RoleType(DjangoObjectType):
    class Meta:
        model = Role


class Query(graphene.ObjectType):
    person_by_id = graphene.Field(PersonType, id=graphene.ID())
    all_person = graphene.List(PersonType)

    person_role_by_id = graphene.Field(PersonRoleType, id=graphene.ID())
    person_role_by_personid = graphene.Field(PersonRoleType, personid=graphene.String(required=True))
    all_person_role = graphene.List(PersonRoleType)

    project_by_id = graphene.Field(ProjectType, id=graphene.ID())
    all_project = graphene.List(ProjectType)

    role_by_id = graphene.Field(RoleType, id=graphene.ID())
    all_role = graphene.List(RoleType)


    def resolve_all_person(self, info, **kwargs):
        return Person.objects.all()
    def resolve_person(self, info, id):
        return Person.objects.get(pk=id)

    def resolve_all_person_role(self, info, **kwargs):
        return PersonRole.objects.all()
    def resolve_person_role(self, info, id):
        return PersonRole.objects.get(pk=id)
    def resolve_person_role_by_personid(self, info, personid):
        try:
            return PersonRole.objects.get(PersonId=personid)
        except PersonRole.DoesNotExist:
            return None

    def resolve_all_project(self, info, **kwargs):
        return Project.objects.all()
    def resolve_project(self, info, id):
        return Project.objects.get(pk=id)

    def resolve_all_role(self, info, **kwargs):
        return Role.objects.all()
    def resolve_role(self, info, id):
        return Role.objects.get(pk=id)


# ******************* CREATE - MUTATIONS ************************* #

class CreatePerson(graphene.Mutation):
    class Arguments:
        LastName = graphene.String()
        FirstName = graphene.String()
        PersonalId = graphene.String()

    person = graphene.Field(PersonType)

    def mutate(self, info, LastName, FirstName, PersonalId):
        person = Person.objects.create(
            LastName=LastName,
            FirstName=FirstName,
            PersonalId=PersonalId
        )
        return CreatePerson(
            person=person
        )


class CreatePersonRole(graphene.Mutation):
    class Arguments:
        ProjectCode = graphene.String()
        PersonId = graphene.String()
        RoleId = graphene.String()
        AssignmentDate = graphene.String()

    personrole = graphene.Field(PersonRoleType)

    def mutate(self, info, ProjectCode, PersonId, RoleId, AssignmentDate):
        personrole = PersonRole.objects.create(
            ProjectCode=ProjectCode,
            PersonId=PersonId,
            RoleId=RoleId,
            AssignmentDate=AssignmentDate
        )
        return CreatePersonRole(
            personrole=personrole
        )


class CreateProject(graphene.Mutation):
    class Arguments:
        Name = graphene.String()
        Description = graphene.String()
        StartDate = graphene.String()
        EndDate = graphene.String()

    project = graphene.Field(ProjectType)

    def mutate(self, info, Name, Description, StartDate, EndDate):
        project = Project.objects.create(
            Name=Name,
            Description=Description,
            StartDate=StartDate,
            EndDate=EndDate
        )
        return CreateProject(
            project=project
        )


class CreateRole(graphene.Mutation):
    class Arguments:
        Name = graphene.String()

    role = graphene.Field(RoleType)

    def mutate(self, info, Name):
        role = Role.objects.create(
            Name=Name
        )
        return CreateRole(
            role=role
        )

# ******************* END OF CREATE - MUTATIONS ************************* #



# ******************* UPDATE - MUTATIONS ************************* #

class UpdatePerson(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        LastName = graphene.String()
        FirstName = graphene.String()
        PersonalId = graphene.String()

    person = graphene.Field(PersonType)

    def mutate(self, info, id, LastName, FirstName, PersonalId):
        person = Person.objects.get(pk=id)
        person.LastName = LastName if LastName is not None else person.LastName
        person.FirstName = FirstName if FirstName is not None else person.FirstName
        person.PersonalId = PersonalId if PersonalId is not None else person.PersonalId

        person.save()
        return UpdatePerson(person=person)

class UpdateProject(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        Name = graphene.String()
        Description = graphene.String()
        StartDate = graphene.String()
        EndDate = graphene.String()

    project = graphene.Field(ProjectType)

    def mutate(self, info, id, Name, Description, StartDate, EndDate):
        project = Project.objects.get(pk=id)
        project.Name = Name
        project.Description = Description
        project.StartDate = StartDate
        project.EndDate = EndDate

        project.save()
        return UpdateProject(project=project)

class UpdateRole(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        Name = graphene.String()

    role = graphene.Field(RoleType)

    def mutate(self, info, id, Name):
        role = Role.objects.get(pk=id)
        role.Name = Name

        role.save()
        return UpdateRole(role=role)

# ******************* END OF UPDATE - MUTATIONS ************************* #


# ******************* DELETE - MUTATIONS ************************* #

class DeletePerson(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    person = graphene.Field(PersonType)

    def mutate(self, info, id):
        person = Person.objects.get(pk=id)
        if person is not None:
            person.delete()
        return DeletePerson(person=person)


class DeletePersonRole(graphene.Mutation):
    class Arguments:
        # person = graphene.String()
        IdOsobe = graphene.String()
        SifProjekta = graphene.String()
        IdUloge = graphene.String()
        AssignmentDate = graphene.String()

    personRole = graphene.Field(PersonRoleType)
    person = graphene.Field(PersonType)

    def mutate(self, info, IdOsobe, SifProjekta, IdUloge):
        person = Person.objects.get(id=IdOsobe)
        personRole = PersonRole.objects.get(AssignmentDate=AssignmentDate)

        print("Person ---------------> %s" % person)
        print("PersonRole ---------------> %s" % personRole)
        print("IdUloge ---------------> %s" % IdUloge)


class DeleteProject(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    project = graphene.Field(ProjectType)

    def mutate(self, info, id):
        project = Project.objects.get(pk=id)
        if project is not None:
            project.delete()
        return DeleteProject(project=project)


class DeleteRole(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    role = graphene.Field(RoleType)

    def mutate(self, info, id):
        role = Role.objects.get(pk=id)
        if role is not None:
            role.delete()
        return DeleteRole(role=role)


# ******************* END OF DELETE - MUTATIONS ************************* #


class Mutation(graphene.ObjectType):
    create_person = CreatePerson.Field()
    update_person = UpdatePerson.Field()
    delete_person = DeletePerson.Field()

    create_person_role = CreatePersonRole.Field()
    delete_person_role = DeletePersonRole.Field()

    create_project = CreateProject.Field()
    update_project = UpdateProject.Field()
    delete_project = DeleteProject.Field()

    create_role = CreateRole.Field()
    update_role = UpdateRole.Field()
    delete_role = DeleteRole.Field()




schema = graphene.Schema(query=Query, mutation=Mutation)