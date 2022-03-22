# # from django.core import serializer

# class ProfsSerializer(serializer.ModelSerializer):
#     full_name = serializer.CharField("Professor's full name",max_length=20)
#     name_code = serializer.CharField("Proffessor's abbreviated name", max_length=5)
  


# class ModulesSerializer(serializer.ModelSerializer):
#     code_by =   serializer.CharField("Module abbreviation", max_length=10)
#     full_name = serializer.CharField("Module's full name", max_length=20)
#     semester =  serializer.IntegerField("Semester this module is being taught")
#     year =      serializer.IntegerField("Year module is taught")
#     prof =      ProfsSerializer()


# class RatingsSeliazer(serializer.ModelSerializer):
#     profs = ProfsSerializer()
#     modules=ModulesSerializer()
#     rating =serializer.SmallIntegerField()

    