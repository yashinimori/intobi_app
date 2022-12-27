from django.db.models import Sum

from intobi_app.vote.models import Vote


def get_top_menu(menus):
    top_rating = 0
    result = 0
    for item in menus:
        if Vote.objects.filter(menu=item).aggregate(Sum("rating")).get("rating__sum"):
            rating_sum = (
                Vote.objects.filter(menu=item)
                .aggregate(Sum("rating"))
                .get("rating__sum")
            )
        print(rating_sum)
        print(type(rating_sum))
        if rating_sum > top_rating:
            top_rating = rating_sum
            result = item
    return result
