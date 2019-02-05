from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { 
    "my_list" : [
    	{
    		'restaurant_name': 'properslider',
    		'food_type': 'american'
    },
    {
    		'restaurant_name': 'melenzane',
    		'food_type': 'italian'
    },
    {		'restaurant_name': 'maki',
    		'food_type': 'japanies'
    }


    ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object" : 
    {
    'restaurant_name': 'maki',
    'food_type': 'japanies'
    }


    
    }
    return render(request, 'detail.html', context)
