from django.db import models

# Create your models here.

#Modelcreated to put Animals into categories of type
class Animal_Type(models.Model):
    #An ID field is automatically added to all Django models
    #Attribute in the model to label the name of the Animal type
    type_name = models.CharField(max_length=100)

#Modelcreated to store animal name and identifer to Animal group including how the datat behaves
class Animal(models.Model):
    #An ID field is automatically added to all Django models
    #Attribute in the model to label the name of the Animal
    animal_name = models.CharField(max_length=100)
    #Attribute into the model that 
    animal_type = models.ForeignKey(Animal_Type, on_delete=models.CASCADE)
#Modelcreated to store animal name and identifer to Animal group including how the datat behaves
class Animal_Species(models.Model):
    #An ID field is automatically added to all Django models
    #Attribute in the model to identify the name of the Animal
    species_name = models.CharField(max_length=100)
    #Attribute in the model to identify the name of the Animal
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE)

#Modelcreated to store animal name and identifer to Animal group including how the datat behaves
class Source(models.Model):
    #An ID field is automatically added to all Django models
    #Attribute into the model that identifies the type of animal
    species_id = models.ForeignKey(Animal_Species, on_delete=models.CASCADE)
    #Attribute in the model to identify the name of the Animal
    source_name = models.CharField(max_length=100)
    #Attribute in the model to identify the name of the Animal
    source_url = models.CharField(max_length=150)
    #Attribute into the model that labels the description of the source
    source_description = models.CharField(max_length=250)

