from django.shortcuts import render
from .models import Rental, Reservations
from django.views import View


def All_Reservation(request):

    # create sublist of reservation details for all reservation records
    reservations = [[res.rental_id.name, res.id, res.checkin, res.checkout] for res in Reservations.objects.all()]
    rental_names = Rental.objects.values_list('name')

    ValueSet = []

    # get res-id or - for each reservation using it's rental name
    for i in sort_by_rental_name(rental_names):
        ValueSet += i

    mapped = list(zip(ValueSet,reservations))

    context = {
        "maps": mapped,
    }

    return render(request, "reservations.html", context)


def sort_by_rental_name(r:any) -> list:

    '''
        filter and define value for each reservation record, in reservation table
        using the rental_name

        this function is a generator that returns a values list
        i.e  ("-" or the previous Reservation id) of the record before.
    '''

    for i in r:
        Qset = Reservations.objects.filter(rental_id__name=i[0])
        QsetLs = list(Qset)
        objects_value_ls = []

        for i in QsetLs:

            if i.id is min([k.id for k in QsetLs]):
                objects_value_ls.append("-")

            objects_value_ls.append(QsetLs[QsetLs.index(i)-1].id)

        objects_value_ls.remove(objects_value_ls[1])

        yield objects_value_ls

          
