import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from handright import Template, handwrite


# Create your views here.
@csrf_exempt
def generate_handwritten_image(request):
    if request.method == 'GET':
        return render(request, 'test_01.html')
    else:

        json_test = request.POST.get('json_data')
        json_data = json.loads(json_test)
        #是否上传了图片布尔值变量名
        is_upload_image = json_data['is_upload_image']
        # 是否上传了自定义字体文件
        is_upload_font = json_data['is_upload_font']
        #纸张大小
        paper_size = json_data['paper_size']
        #自定义纸张长宽
        custom_paper_size = json_data['custom_paper_size']
        #行距
        line_spacing = json_data['line_spacing']
        #列距
        column_spacing = json_data['column_spacing']
        #上边距
        top_margin = json_data['top_margin']
        #下边距
        bottom_margin = json_data['bottom_margin']
        #左边距
        left_margin = json_data['left_margin']
        #右边距
        right_margin = json_data['right_margin']
        #字体大小
        font_size = json_data['font_size']
        #字体
        font = json_data['font']
        #字体颜色
        font_color = json_data['font_color']
        # 行间距随机扰动
        line_spacing_sigma = json_data['line_spacing_sigma']
        # 字体大小随机扰动
        font_size_sigma = json_data['font_size_sigma']
        # 字间距随机扰动
        word_spacing_sigma = json_data['word_spacing_sigma']
        start_chars = "“（[<{‘"
        end_chars = ",.!?;:，。！？；：”）]>}"
        # 笔画横向偏移随机扰动
        perturb_x_sigma = json_data['perturb_x_sigma']
        # 笔画纵向偏移随机扰动
        perturb_y_sigma = json_data['perturb_y_sigma']
        # 笔画旋转偏移随机扰动
        perturb_theta_sigma = json_data['perturb_theta_sigma']
        if is_upload_image:
            image = request.FILES.get('image')
            #gitgen



