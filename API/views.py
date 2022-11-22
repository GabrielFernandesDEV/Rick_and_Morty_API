from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests


def personagem(request):
    #pull data from third party rest api
    response = requests.get('https://rickandmortyapi.com/api/character')
    #convert reponse data into json
    personagem_json = response.json()
    return JsonResponse(personagem_json)
    pass



def localizacao(request):
    #pull data from third party rest api
    response = requests.get('https://rickandmortyapi.com/api/location')
    #convert reponse data into json
    personagem_json = response.json()
    return JsonResponse(personagem_json)
    pass

def episodios(request):
    #pull data from third party rest api
    response = requests.get('https://rickandmortyapi.com/api/episode')
    #convert reponse data into json
    personagem_json = response.json()
    return JsonResponse(personagem_json)
    pass