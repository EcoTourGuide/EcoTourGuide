from django.shortcuts import render, HttpResponse
from EcoTourGuide.firebase_config import db, auth, storage


def login(request):

    # test code.
    users_ref = db.collection('User')
    docs = users_ref.stream()

    users = [doc.to_dict() for doc in docs]

    return HttpResponse(f"Users: {users}")
    # return render(request, '', {})
