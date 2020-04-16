from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import TKcVrfcReptdcAdmn, TKjIndiRcmmAdmin
from .forms import TKjIndiRcmmAdminForm, TKcVrfcReptdcAdmnForm
from django.shortcuts import redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from _overlapped import NULL
import math
from _ast import If

# Create your views here.

'''
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
'''
########################################################################
# 사용자 리스트
########################################################################
def admin_list(request):
    posts = TKjIndiRcmmAdmin.objects.all()
    posts = posts.filter().order_by('user_id')
    return render(request, 'admin/admin_list.html', {'posts': posts})

#########################################################################
# 사용자 상세 화면
#########################################################################
def admin_detail(request, user_id):
    post = get_object_or_404(TKjIndiRcmmAdmin, user_id=user_id)
    return render(request, 'admin/admin_detail.html', {'post': post})

########################################################################
# 사용자 저장
########################################################################
def admin_new(request):
    print("!!!!!!!!!!!!!!!!")
    if request.method == "POST":
        form = TKjIndiRcmmAdminForm(request.POST)
        if form.is_valid():
            print("???????????????? ")
            post = form.save(commit=False)
            post.reg_dtm = timezone.now()
            #post.admin_save()
            post.save()
            return redirect('admin_detail', user_id=post.user_id)
            #msg = "등록이 완료되었습니다."
            #post_url = "admin_detail " + post.user_id 
            #return render(request, 'common/alert.html', {'msg': msg, 'post_url':post_url})
    else:
        print("$$$$$$$$$$$$$$$$$$$")
        form = TKjIndiRcmmAdminForm()
    return render(request, 'admin/admin_edit.html', {'form': form})

########################################################################
# 사용자 수정
########################################################################
def admin_edit(request, user_id):
    post = get_object_or_404(TKjIndiRcmmAdmin, user_id=user_id)
    if request.method == "POST":
        form = TKjIndiRcmmAdminForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.last_updt_dtm = timezone.now()
            post.admin_save()
            msg = "수정이 완료되었습니다."
            post_url = "admin_detail " + post.user_id 
            return render(request, 'common/alert.html', {'msg': msg, 'post_url':post_url})
    else:
        form = TKjIndiRcmmAdminForm(instance=post)
    return render(request, 'admin/admin_edit.html', {'form': form})


















########################################################################
# 계량관리 보고서 리스트
########################################################################
def insp_list(request):
    posts = TKcVrfcReptdcAdmn.objects.all()
    posts = posts.filter(reg_dtm__gte='2020-03-19').order_by('reptdc_no')
   
    ################ 페이징 시작 ##############
    paginator = Paginator(posts, 2) 
    
    page = request.GET.get('page')
    
    if page == None:
        page = 1
    
    pages = paginator.get_page(page)
    ################ 페이징 끝 ##############
    
    page_range = 5
    current_block = math.ceil(int(page)/page_range) #해당 페이지가 몇번째 블럭인가
    start_block = (current_block-1) * page_range
    end_block = start_block + page_range
    p_range = paginator.page_range[start_block:end_block]
    
    return render(request, 'kc/insp_list.html', {'pages':pages, 'p_range':p_range})

#########################################################################
# 계량관리 보고서 상세 화면
#########################################################################
def insp_detail(request, mba_cd, reptdc_no):
    post = get_object_or_404(TKcVrfcReptdcAdmn, mba_cd=mba_cd, reptdc_no=reptdc_no)
    return render(request, 'kc/insp_detail.html', {'post': post})

########################################################################
# 계량관리 보고서 저장
########################################################################
def insp_new(request):
    if request.method == "POST":
        form = TKcVrfcReptdcAdmnForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.reg_dtm = timezone.now()
            post.rept_dtm = timezone.now()
            post.reptdc_save()
            
            url_div = "detail"
            msg = "등록이 완료되었습니다."
            return render(request, 'common/alert.html', {'msg': msg, 'post':post, 'url_div':url_div})
    else:
        form = TKcVrfcReptdcAdmnForm()
    return render(request, 'kc/insp_edit.html', {'form': form, 'page_div':'add'})

########################################################################
# 계량관리 보고서 수정
########################################################################
def insp_edit(request, mba_cd, reptdc_no):
    post = get_object_or_404(TKcVrfcReptdcAdmn, mba_cd=mba_cd, reptdc_no=reptdc_no)
    if request.method == "POST":
        form = TKcVrfcReptdcAdmnForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.last_updt_dtm = timezone.now()
            post.reptdc_save()
            
            url_div = "list"
            msg = "수정이 완료되었습니다."
            return render(request, 'common/alert.html', {'msg': msg, 'post':post, 'url_div':url_div})
    else:
        form = TKcVrfcReptdcAdmnForm(instance=post)
    return render(request, 'kc/insp_edit.html', {'form': form, 'page_div':'edit'})

########################################################################
# 계량관리 보고서 삭제
########################################################################
def insp_delete(request, mba_cd, reptdc_no):
    post = get_object_or_404(TKcVrfcReptdcAdmn, mba_cd=mba_cd, reptdc_no=reptdc_no)
    post.delete()
    
    msg = "삭제가 완료되었습니다."
    return render(request, 'common/alert.html', {'msg': msg, 'post':post, 'url_div':'list'})


