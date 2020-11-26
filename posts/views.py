"""Posts views."""
from django.http import HttpResponse

""" Utilities """
from datetime import datetime

posts = [
    {
        'name': 'photography section',
        'user': 'Ana Sofia Cruz',
        'timestamp': datetime.now().strftime('%b %dth,%Y - %H:%M hrs'),
        'picture': 'https://scontent.flim16-2.fna.fbcdn.net/v/t1.0-9/67128374_1190958321083796_7480488576019333120_o.jpg?_nc_cat=100&ccb=2&_nc_sid=09cbfe&_nc_eui2=AeG71338UrQsIPdSKjxKl0lyTZwzzvw90mJNnDPO_D3SYsn_jKFamlTY0Fuinm5gfdcabkEOxkJ5nIEFLb8Qj4C_&_nc_ohc=aWHKvctWKl0AX_v3ME1&_nc_ht=scontent.flim16-2.fna&oh=da6487659bf9640b4b9f79e6b94e4ca6&oe=5FE6189B',
    },
    {
        'name': 'nice nature',
        'user': 'Luisa Cardozo',
        'timestamp': datetime.now().strftime('%b %dth,%Y - %H:%M hrs'),
        'picture': 'https://images.unsplash.com/photo-1599186865902-43bde4810e71?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80',
    },
    {
        'name': 'great night with the band',
        'user': 'Roberto Salaverry',
        'timestamp': datetime.now().strftime('%b %dth,%Y - %H:%M hrs'),
        'picture': 'https://images.unsplash.com/photo-1533584592871-abb80e6e4ea2?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80',
    }
]


def list_posts(request):
    """list existing posts."""
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
        """.format(**post))
    
    return HttpResponse('<br>'.join(content))
