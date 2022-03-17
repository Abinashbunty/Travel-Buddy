#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
source = input()
destination = input()
locations=[chennai,vellore,bangalore]
distance=[[0,100,200],[100,0,300],[200 300 0]]
bfare=500
def dfare(source,destination){
   # for source in locations:
    #    a=locations.index(source)


    for i in range (len(locations)):
        if(locations[i]=source):
            a=i
        else if (locations[i] = destination):
            b=i
    return distance[a][b]*10
}

def demand(total_clicks, total_clicks,bfare){
    return clicks/total_clicks+bfare
}
mfare = bfare + dfare(source,destination) + 

