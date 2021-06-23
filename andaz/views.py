from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    temp_name='index.html'
    return render(request,temp_name)

# def blogsingle(request):
#     return render(request,"blog-single'.html")

# def blog(request):
#     return render(request,"blog.html")
# def contact(request):
#     return render(request,"contact.html")
# def features(request):
#     return render(request,"features.html")
# def pricing(request):
#     return render(request,"pricing.html")