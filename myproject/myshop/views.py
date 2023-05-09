from django.shortcuts import render
from myshop.models import Actor

# Create your views here.
def index(request):
    pass

def my_actor(request):
    rows = Actor.objects.all().using('default')
    return render(request, 'myactor.html', {'rows':rows})

import MySQLdb
def my_dbconn(request):
    #  ("Hostname","dbusername","password","dbname")
    conn = MySQLdb.connect( 'localhost', 'host', '1q2w3e4r!', 'myproject')

    cur = conn.cursor()
    cur.execute("select * from actor")
    rows = cur.fetchall()
    conn.close()
    return render(request, 'myactor_1.html', {'rows': rows})
