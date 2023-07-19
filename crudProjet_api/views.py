from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from crudProjet_api.models import Author, Book
from crudProjet_api.serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.filter(is_available=True)
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def list(self, request):
        # Récupère la liste des objets.
        _objects = self.queryset.filter(author=request.author)

        # Sérialiser les objets.
        serializer = self.serializer_class(_objects, many=True)

        return Response(serializer.data)

    def create(self, request):
        # Sérialiser les données de la demande.
        serializer = self.serializer_class(data=request.data)
        
        name = request.data.get('name')
        # Vérification si l'auteur existe déjà
        if Author.objects.filter(name=name).exists():
            return Response({"error": "L\'auteur existe déjà."}, status=400)

        # Valider le serializer.
        if serializer.is_valid():
            # Enregistrer l'objet dans la base de données.
            serializer.save()

            # Retourner l'objet sérialisé.
            return Response({"message": "l\'auteur a été crée"},status=201)

        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk):
        # Récupère l'objet.
        _object = self.queryset.get(pk=pk, author=request.author)

        # Sérialiser l'objet.
        serializer = self.serializer_class(_object)
        if serializer.is_valid():
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)
        

    def update(self, request, pk):
        # Récupère l'objet.
        _object = self.queryset.get(pk=pk, author=request.author)

        # Sérialiser les données de la demande.
        serializer = self.serializer_class(_object, data=request.data)

        # Valider le serializer.
        if serializer.is_valid():
            # Mettre à jour l'objet dans la base de données.
            serializer.save()

            # Retourner l'objet sérialisé.
            return Response({"message": "l\'auteur a été mis a jour "}, status=200)

        return Response(serializer.errors, status=400)

    def destroy(self, request, pk):
        # Récupère l'objet.
        _object = self.queryset.get(pk=pk)

        # Supprimer l'objet de la base de données.
        _object.is_available = False
        
        # Vérifie si l'objet a été supprimé avec succès.
        if _object.is_available:
            _object.save()
            # Affiche un message indiquant que la suppression a été effectuée.
            return Response({'message': 'L\'auteur a été supprimé.'}, status=204)
        else:
            # Affiche un message indiquant que la suppression a échoué.
            return Response({'message': 'La suppression a échoué.'}, status=400)
        


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(is_available=True)
    serializer_class = BookSerializer
    permission_classes = permission_classes = [permissions.IsAuthenticated]
    
    def list(self, request):
        # Récupère la liste des objets.
        _objects = self.queryset.filter(book=request.book)

        # Sérialiser les objets.
        serializer = self.serializer_class(_objects, many=True)

        return Response(serializer.data)

    def create(self, request):
        # Sérialiser les données de la demande.
        serializer = self.serializer_class(data=request.data)
        title = request.data.get('title')
                # Vérification si l'auteur existe déjà
        if Author.objects.filter(title=title).exists():
            return Response({"error": "Le livre existe déjà."}, status=400)

        # Valider le serializer.
        if serializer.is_valid():
            # Enregistrer l'objet dans la base de données.
            serializer.save()

            # Retourner l'objet sérialisé.
            return Response({"message": "le livre a été crée"},status=201)

        return Response({"message": " une erreur c\'est produite lors de la creation du livre "},serializer.errors, status=400)

    def retrieve(self, request, pk):
        # Récupère l'objet.
        _object = self.queryset.get(pk=pk, book=request.book)

        # Sérialiser l'objet.
        serializer = self.serializer_class(_object)
        if serializer.is_valid():
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)
        

    def update(self, request, pk):
        # Récupère l'objet.
        _object = self.queryset.get(pk=pk, book=request.book)

        # Sérialiser les données de la demande.
        serializer = self.serializer_class(_object, data=request.data)

        # Valider le serializer.
        if serializer.is_valid():
            # Mettre à jour l'objet dans la base de données.
            serializer.save()

            # Retourner l'objet sérialisé.
            return Response({"message": "le livre a été mis a jour "}, status=200)

        return Response(serializer.errors, status=400)

    def destroy(self, request, pk):
        # Récupère l'objet.
        _object = self.queryset.get(pk=pk, book=request.book)

        # Supprimer l'objet de la base de données.
        _object.is_available= False
        
        # Vérifie si l'objet a été supprimé avec succès.
        if _object.is_available:
            _object.save()
            
            # Affiche un message indiquant que la suppression a été effectuée.
            return Response({'message': 'Le livre a été supprimé.'}, status=204)
        else:
            # Affiche un message indiquant que la suppression a échoué.
            return Response({'message': 'La suppression du livre a échoué.'}, status=400)