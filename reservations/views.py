from django.shortcuts import render
from .models import Rental, Reservations


def All_Reservation(request):

    reservations = Reservations.objects.all()
    rental_names = Rental.objects.values_list('name')

    ValueSet = []

    for i in sort_by_rental_name(rental_names):
        ValueSet += i

    mapped = zip(ValueSet,reservations)
    print(dict(mapped))
    
    context = {
        'reservations': reservations,
        'values': ValueSet
    }

    return render(request, "reservations.html", context)


def sort_by_rental_name(r:any) -> list:

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

          
