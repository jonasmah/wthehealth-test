from django.db import connection
from django.shortcuts import render
from .models import Doctor, Hospital, Review
import json
import pprint

from django.db import connection
import time
from collections import defaultdict

def retrieve_data(request):
    #Assess the current SQL query usage
    start_time = time.time()
    queries_before = len(connection.queries)

    queryset_hosp = Hospital.objects.all()
    queryset_review = Review.objects.all()
    # queryset_doctor = Doctor.objects.all()

    # Output Check
    # print(queryset_hosp.first().hospitalname)

    if request.GET.get('search'):
        search = request.GET.get('search')

        queryset_hosp = queryset_hosp.filter(hospitalname__icontains=search)
        # queryset_doctor = queryset_doctor.filter(name__icontains=search)

    # Array - Hospital Dropdown Listing  
    # hospitals_by_state = {}
    # for hosp in Hospital.objects.all():
    #     if hosp.state not in hospitals_by_state:
    #         hospitals_by_state[hosp.state] = []
    #     hospitals_by_state[hosp.state].append(hosp.hospitalname)

    # Array - Hospital Dropdown Listing (backup)
    # hospitals_by_state = {
    # hosp.hospitalname: hosp.state 
    # for hosp in Hospital.objects.all()
    # }

    # Output Check
    # print(">>> Hospitals by State \n")
    # for key, value in hospitals_by_state.items():
    #     print(f"{key}: {value}\n")
    # print(">>> Hospitals by State \n")
    # for key, value in hospitals_by_state.items():
    #     print(f"{key}: {value}\n")


    # Dictionary - Review Table - Group reviews by state (based on hospital location)
    # reviews_by_state = defaultdict(list)
    # for review in Review.objects.all():          # ← or .filter(...) if you need
    #     state = hospitals_by_state.get(review.hospname)
    #     if state:
    #         reviews_by_state[state].append({
    #             'hospname': review.hospname,
    #             'reviewtext': review.reviewtext,
    #             'rating': review.rating,
    #             'datePublished': review.reviewdatetime.strftime('%Y-%m-%d') if review.reviewdatetime else None,
    #             'author': review.author
    #         })


    # Dictionary (backup) - Review Table - Group reviews by state (based on hospital location)
    # reviews_by_state = {}
    # for hosp in Hospital.objects.all():
    #     if hosp.state not in reviews_by_state:
    #         reviews_by_state[hosp.state] = []
        
    #     # Get reviews for this hospital
    #     reviews = Review.objects.filter(hospname=hosp.hospitalname)

    #     for review in reviews:
    #         reviews_by_state[hosp.state].append({
    #             'hospname': review.hospname,
    #             'reviewtext': review.reviewtext,
    #             'rating': review.rating,
    #             'datePublished': review.reviewdatetime.strftime('%Y-%m-%d') if review.reviewdatetime else None,
    #             'author': review.author
    #         })
    
    # Output Check
    # print(">>> Reviews by State \n")
    # for key, value in reviews_by_state.items():
    #     print(f"{key}: {value}\n")
        
    
    # context = {
    #     'hospital':queryset_hosp,
    #     'hospitals_by_state_json': json.dumps(hospitals_by_state),
    #     #'reviews_by_state_json': json.dumps(reviews_by_state),
    #     'review':queryset_review,
    #     # 'doctor':queryset_doctor
    #     }

    print("Queries executed:", len(connection.queries) - queries_before)
    print("Total time:", round(time.time() - start_time, 2), "seconds")

    return render(request, 'index_TEST.html')
    # return render(request, 'index.html', context)


# def home(request):
#     return render(request,'index.html')
#     return render(request,'retrieve_data.html')


def average(request):
    query = "SELECT HospName, AVG(Rating) AS AvgRating FROM Review WHERE HospName IS NOT NULL AND Doctor IS NULL AND Specialty IS NULL GROUP BY HospName ORDER BY AvgRating DESC, HospName"
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        # Fetch all rows as dictionaries
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]

    return render(request,'average.html',{'data': data})
