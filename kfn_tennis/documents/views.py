from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Category, Document

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'documents/categories.html', {'categories': categories})


def document_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    documents = Document.objects.filter(category=category)

    query = request.GET.get('q')
    if query:
        documents = documents.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    paginator = Paginator(documents, 15)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    return render(request, 'documents/documents.html', {
        'category': category,
        'documents': page_obj,
        'query': query
    })
