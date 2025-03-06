from django.shortcuts import render
from .models import VectorProduct as Product
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
import time
# Create your views here.

def vector_search_home(request):

    start = time.perf_counter()
    products = Product.objects.all()
    search = request.GET.get('search')

    if search:
        query = SearchQuery(search)
        vector = SearchVector('title', 'description', 'category')

        results = products.annotate(
            rank=SearchRank(vector, query)
        ).filter(rank__gte=0.01).order_by('-rank')
    else:
        results = products

    end = time.perf_counter()
    total_time = round(end - start, 6)

    context = {
        "products": results,
        "total_products": results.count(),
        "search": search,
        "total_time": total_time
    }

    return render(request, template_name="index.html", context=context)