from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from crudProjet_api.models import Author, Book
from crudProjet_api.serializers import AuthorSerializer, BookSerializer

#section import pour les tokens
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import MyTokenObtainPairSerializer


#viewsets
""" 
Actions CRUD prédéfinies : Les ViewSets fournissent des actions prédéfinies pour effectuer les opérations CRUD (Create, Retrieve, Update, Delete) sur un modèle. 
Les actions telles que list(), create(), retrieve(), update(), partial_update(), et destroy() sont déjà implémentées et peuvent être utilisées directement.

Routage automatique : Les ViewSets sont conçus pour fonctionner avec les routeurs de Django REST Framework.
Les routes URL pour chaque action du ViewSet (par exemple, list(), retrieve(), etc.) sont automatiquement générées par le routeur.
Cela facilite la gestion des URL et les associe automatiquement aux actions appropriées. et plus d'autres.....


"""



class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    #affiche tous les object dont la variable is_available est definit a True, pas encore supprimé
    queryset = Author.objects.filter(is_available=True)
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        # Récupère la liste des objets.
        _objects = self.filter_queryset(self.get_queryset())

        # Sérialiser les objets.
        serializer = self.serializer_class(_objects, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # Sérialiser les données de la demande.
        serializer = self.serializer_class(data=request.data)
        
        name = request.data.get('name')
        # Vérification si l'auteur existe déjà
        if Author.objects.filter(name=name).exists():
            return Response({"error": "L\'auteur existe déjà."}, status=400)

        # Valider le serializer.
        if serializer.is_valid():

            # Associer l'utilisateur actuel à la modification
            serializer.created_by = request.user 
            # Enregistrer l'objet dans la base de données.
            serializer.save()

            # Retourner l'objet sérialisé.
            return Response({"message": "l\'auteur a été crée"},status=201)

        return Response(serializer.errors, status=400)

    def retrieve(self, request, *args, **kwargs):
        # Récupère l'objet.
        _object = self.get_object()

        # Sérialiser l'objet.
        serializer = self.serializer_class(_object)
        if serializer.is_valid():
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)
        

    def update(self, request, *args, **kwargs):
        # Récupère l'objet.
        _object = self.get_object()

        # Associer l'utilisateur actuel à la modification
        _object.modified_by = request.user  

        # Sérialiser les données de la demande.
        serializer = self.serializer_class(_object, data=request.data)

        # Valider le serializer.
        if serializer.is_valid():

            # Mettre à jour l'objet dans la base de données.
            serializer.save()

            # Retourner l'objet sérialisé.
            return Response({"message": "l\'auteur a été mis a jour "}, status=200)

        return Response(serializer.errors, status=400)

    def destroy(self, request, *args, **kwargs):
        # Récupère l'objet.
        _object = self.get_object()

        # Vérifie si l'objet existe.
        if _object:
        # Supprimer l'objet de la base de données.
            _object.is_available = False
            _object.save()
            # Affiche un message indiquant que la suppression a été effectuée.
            return Response({'message': 'L\'auteur a été supprimé.'}, status=204)
        else:
            # Affiche un message indiquant que la suppression a échoué.
            return Response({'message': 'La suppression a échoué ou l\'objet n\'existe pas.'}, status=400)
        


class BookViewSet(viewsets.ModelViewSet):
    #affiche tous les object dont la variable is_available est definit a True, pas encore supprimée
    queryset = Book.objects.filter(is_available=True)
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        # Récupère la liste des objets.
        _objects =  self.filter_queryset(self.get_queryset())

        # Sérialiser les objets.
        serializer = self.serializer_class(_objects, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # Sérialiser les données de la demande.
        serializer = self.serializer_class(data=request.data)
        title = request.data.get('title')
                # Vérification si l'auteur existe déjà
        if Author.objects.filter(title=title).exists():
            return Response({"error": "Le livre existe déjà."}, status=400)

        # Valider le serializer.
        if serializer.is_valid():

             # Associer l'utilisateur actuel à la modification
            serializer.created_by = request.user 
            # Enregistrer l'objet dans la base de données.
            serializer.save()

            # Retourner l'objet sérialisé.
            return Response({"message": "le livre a été crée"},status=201)

        return Response({"message": " une erreur c\'est produite lors de la creation du livre "},serializer.errors, status=400)

    def retrieve(self, request, *args, **kwargs):
        # Récupère l'objet.
        _object = self.get_object()

        # Sérialiser l'objet.
        serializer = self.serializer_class(_object)
        if serializer.is_valid():
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)
        

    def update(self, request, *args, **kwargs):
        # Récupère l'objet.
        _object = self.get_object()

        # Associer l'utilisateur actuel à la modification
        _object.modified_by = request.user  

        # Sérialiser les données de la demande.
        serializer = self.serializer_class(_object, data=request.data)

        # Valider le serializer.
        if serializer.is_valid():

            # Mettre à jour l'objet dans la base de données.
            serializer.save()

            # Retourner l'objet sérialisé.
            return Response({"message": "le livre a été mis a jour "}, status=200)

        return Response(serializer.errors, status=400)

    def destroy(self, request, *args, **kwargs):
        # Récupère l'objet.
        _object = self.get_object()

        # Vérifie si l'objet existe.
        if _object:

             # Supprimer l'objet de la base de données.
            _object.is_available = False

            # Associer l'utilisateur actuel à la modification
            _object.modified_by = request.user 
            
            _object.save()
        
            # Affiche un message indiquant que la suppression a été effectuée.
            return Response({'message': 'Le livre a été supprimé.'}, status=204)
        else:
            # Affiche un message indiquant que la suppression a échoué.
            return Response({'message': 'La suppression du livre a échoué.'}, status=400)