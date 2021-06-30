from django.shortcuts import render
from django.http import HttpResponse
import random
#from transformers import AutoModelForCausalLM, AutoTokenizer
# Create your views here.
def index(request):

    return render(request,"index.html")