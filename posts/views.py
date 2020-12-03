"""Posts views."""
#Django
from django.shortcuts import render

#Utilities
from datetime import datetime

posts = [
    {
        'title': 'photography section',
        'user': {
            'name':  'Ana Sofia Cruz',
            'picture': 'https://images.unsplash.com/profile-1587493314442-0b28a91f93aeimage?dpr=1&auto=format&fit=crop&w=150&h=150&q=60&crop=faces&bg=fff'
        },  
        'timestamp': datetime.now().strftime('%b %dth,%Y - %H:%M hrs'),
        'photo': 'https://scontent.flim16-2.fna.fbcdn.net/v/t1.0-9/67128374_1190958321083796_7480488576019333120_o.jpg?_nc_cat=100&ccb=2&_nc_sid=09cbfe&_nc_eui2=AeG71338UrQsIPdSKjxKl0lyTZwzzvw90mJNnDPO_D3SYsn_jKFamlTY0Fuinm5gfdcabkEOxkJ5nIEFLb8Qj4C_&_nc_ohc=aWHKvctWKl0AX_v3ME1&_nc_ht=scontent.flim16-2.fna&oh=da6487659bf9640b4b9f79e6b94e4ca6&oe=5FE6189B',
    },
    {
        'title': 'nice nature',
        'user': {
            'name':'Luisa Cardozo',
            
            'picture':'https://scontent.flim16-3.fna.fbcdn.net/v/t1.0-9/116290960_2949417265338955_600001328163397407_n.jpg?_nc_cat=106&ccb=2&_nc_sid=09cbfe&_nc_eui2=AeGGMT99S-pJTfLPJ3GbkEn0y_tnYGRg89nL-2dgZGDz2SFqoQBsw_3Mh26zwsNDDiD0eWXaMb70y5bTXA1EOYDi&_nc_ohc=X7upsM-XlrYAX83tjRR&_nc_ht=scontent.flim16-3.fna&oh=52548941dea97629803a43276838190f&oe=5FE6E212'

        },
        'timestamp': datetime.now().strftime('%b %dth,%Y - %H:%M hrs'),
        'photo': 'https://images.unsplash.com/photo-1599186865902-43bde4810e71?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80',
    },
    {
        'title': 'great night with the band',
        'user': {
            'name':'Roberto Salaverry',
            'picture':'https://images.unsplash.com/profile-1591695757866-df9c0e4c78a2image?dpr=1&auto=format&fit=crop&w=150&h=150&q=60&crop=faces&bg=fff'
        },  
        'timestamp': datetime.now().strftime('%b %dth,%Y - %H:%M hrs'),
        'photo': 'https://images.unsplash.com/photo-1533584592871-abb80e6e4ea2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80',
    }
]


def list_posts(request):
    """list existing posts."""
    
    
    return render(request, 'posts/feed.html', {'posts': posts})
