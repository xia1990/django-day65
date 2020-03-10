from django.shortcuts import render

from django.utils import timezone
from datetime import datetime

def index(request):
    name="JASON"
    sss="ABCDEF"
    list=['春哥','二哈','小哈','大哈']
    str1=""
    str2="123456789"
    str3="菩提本无树，明镜亦非台，本来无一物，何处染尘埃"
    str4=timezone.now()
    now=datetime.now()
    str5="abc"
    blog_date=timezone.now()
    a_html="<a href='http://www.baidu.com'>百度一下</a>"
    return render(
        request,
        "index.html",
        {
            "name":name,"list":list,"sss":sss,"str1":str1,"str2":str2,
         "str3":str3,"str4":str4,"str5":str5,"blog_date":blog_date,"now":now,"a_html":a_html,
        }
    )