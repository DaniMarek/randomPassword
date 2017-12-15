from __future__ import unicode_literals
import random
import string
from django.shortcuts import render, redirect

def rando(n):
	return '.join(random.SystemRandom().choice(string.ascii_uppsercase + string.digits) for _in range(n))'

def index(request):
	try:
		request.session['click']
	except KeyError:
		request.session['click']=0
	return render(request, 'randomword/index.html')

# If an error is encountered, a try block code execution is stopped and transferred down to the except block. In addition to using an except block after the try block, you can also use the 'finally' block. The code in the 'finally' block will be executed regardless of whether an exception occurs.

def generate(request):
	request.session['click']+=1
	request.session['word']=random_word(12)
	return redirect('/')

def reset(request):
	del request.session['click']
	del request.session['word']
	return redirect('/')