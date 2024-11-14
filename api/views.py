import io
import json
import os
import shutil
import tempfile
import time

from PIL import Image, ImageFont
# from PIL.ImageFont import ImageFont
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from handright import Template, handwrite
# 导入settings.py中的配置
from TextMorph import settings

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    rgb_tuple = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return rgb_tuple
# Create your views here.
@csrf_exempt
def generate_handwritten_image(request):
    if request.method == 'GET':
        return redirect('index')
    else:
        # 用户上传的文本信息
        text_info = request.POST.get('text_info')
        json_test = request.POST.get('json_data')
        json_data = json.loads(json_test)
        print(json_data)
        is_upload_image = json_data.get('is_upload_image', False)
        is_upload_font = json_data.get('is_upload_font', False)
        custom_paper_size = json_data.get('custom_paper_size', {'w': 2100, 'h': 2970})
        line_spacing = json_data.get('line_spacing', 100)
        word_spacing = json_data.get('word_spacing',4)
        top_margin = json_data.get('top_margin',100)
        bottom_margin = json_data.get('bottom_margin',100)
        left_margin = json_data.get('left_margin',100)
        right_margin = json_data.get('right_margin',100)
        font_size = json_data.get('font_size', 80)
        font_name = json_data.get('font_name','李国夫手写体')
        font_color = json_data.get('font_color',1)
        line_spacing_sigma = json_data.get('line_spacing_sigma', 6)
        font_size_sigma = json_data.get('font_size_sigma',2)
        word_spacing_sigma = json_data.get('word_spacing_sigma',2)
        perturb_x_sigma = json_data.get('perturb_x_sigma',1)
        perturb_y_sigma = json_data.get('perturb_y_sigma',1)
        perturb_theta_sigma = json_data.get('perturb_theta_sigma',0.15)
        ink_depth_sigma = json_data.get('ink_depth_sigma',0.2)
        is_preview = json_data.get('is_preview', False)
        if is_upload_image:
            image_file = request.FILES.get('image')
            # image 是 UploadedFile 的一个实例，它是 Django 提供的用于处理文件上传的类。该类包含与上传文件交互的属性和方法，例如 name、size、content_type、read() 和 chunks()。
            image_data = io.BytesIO(image_file.read())
            image = Image.open(image_data)
            # 将图形转换成GRB格式
            image_data = image_data.getvalue()
        else:
            #创建RGB格式的白色背景图像
            image = Image.new(mode="RGB", size=(custom_paper_size['w'], custom_paper_size['h']), color=(255, 255, 255))

        if is_upload_font:
            font_file = request.FILES.get('font_file')
            font_data = io.BytesIO(font_file.read())
            font = ImageFont.truetype(font_data, size=font_size)
        else:
            font_path = settings.FONT_PATH / settings.FONT_NAME_MAP[font_name]
            print(font_path)
            with open(font_path, 'rb') as f:
                font_data = io.BytesIO(f.read())
            font = ImageFont.truetype(font_data, size=font_size)
        #参数说明
        """
        background: PIL.Image.Image,  # 背景图像，PIL库的Image对象
        font,  # 字体，Pillow库的字体实例
        line_spacing: Optional[int] = None,  # 行间距，可选整数，默认为None
        fill=None,  # 填充颜色，默认为None
        left_margin: int = _DEFAULT_LEFT_MARGIN,  # 左边距，整数，默认值为_DEFAULT_LEFT_MARGIN
        top_margin: int = _DEFAULT_TOP_MARGIN,  # 上边距，整数，默认值为_DEFAULT_TOP_MARGIN
        right_margin: int = _DEFAULT_RIGHT_MARGIN,  # 右边距，整数，默认值为_DEFAULT_RIGHT_MARGIN
        bottom_margin: int = _DEFAULT_BOTTOM_MARGIN,  # 下边距，整数，默认值为_DEFAULT_BOTTOM_MARGIN
        word_spacing: int = _DEFAULT_WORD_SPACING,  # 字间距，整数，默认值为_DEFAULT_WORD_SPACING
        line_spacing_sigma: Optional[float] = None,  # 行间距的标准差，可选浮点数，默认为None
        font_size_sigma: Optional[float] = None,  # 字体大小的标准差，可选浮点数，默认为None
        word_spacing_sigma: Optional[float] = None,  # 字间距的标准差，可选浮点数，默认为None
        start_chars: str = _DEFAULT_START_CHARS,  # 不应放在行尾的字符集合，字符串，默认值为_DEFAULT_START_CHARS
        end_chars: str = _DEFAULT_END_CHARS,  # 不应放在行首的字符集合，字符串，默认值为_DEFAULT_END_CHARS
        perturb_x_sigma: Optional[float] = None,  # 水平位置的标准差，可选浮点数，默认为None
        perturb_y_sigma: Optional[float] = None,  # 垂直位置的标准差，可选浮点数，默认为None
        perturb_theta_sigma: float = _DEFAULT_PERTURB_THETA_SIGMA,  # 旋转角度的标准差，浮点数，默认值为_DEFAULT_PERTURB_THETA_SIGMA
        # strikethrough_length_sigma: Optional[float]=None,  # 删除线长度的标准差，可选浮点数，默认为None
        # strikethrough_angle_sigma: float = _DEFAULT_strikethrough_angle_sigma,  # 删除线角度的标准差，浮点数，默认值为_DEFAULT_strikethrough_angle_sigma
        # strikethrough_width_sigma: Optional[float]=None,  # 删除线宽度的标准差，可选浮点数，默认为None
        # strikethrough_probability: float = _DEFAULT_strikethrough_probability,  # 删除线出现的概率，浮点数，默认值为_DEFAULT_strikethrough_probability
        # strikethrough_width: Optional[float]=None,  # 删除线宽度，可选浮点数，默认为None
        # ink_depth_sigma: Optional[float]=None,  # 墨水深度的标准差，可选浮点数，默认为None
        # features: Set = _DEFAULT_FEATURES,  # 额外特性，集合，默认值为_DEFAULT_FEATURES
        """
        template = Template(
            background=image,
            font=font,
            line_spacing=line_spacing,
            word_spacing=word_spacing,
            top_margin=top_margin,
            bottom_margin=bottom_margin,
            left_margin=left_margin,
            right_margin=right_margin,
            fill=hex_to_rgb(font_color),
            end_chars= settings.END_CHARS,# 防止特定字符因排版算法的自动换行而出现在行首
            start_chars= settings.START_CHARS, # 特定字符提前换行，防止出现在行尾
            line_spacing_sigma=line_spacing_sigma,  # 行间距随机扰动
            font_size_sigma=font_size_sigma,  # 字体大小随机扰动
            word_spacing_sigma=word_spacing_sigma,  # 字间距随机扰动
            ink_depth_sigma=ink_depth_sigma,
            perturb_x_sigma=int(perturb_x_sigma),  # 笔画横向偏移随机扰动
            perturb_y_sigma=int(perturb_y_sigma),  # 笔画纵向偏移随机扰动
            perturb_theta_sigma=float(perturb_theta_sigma) # 笔画旋转偏移随机扰动
        )
        image = handwrite(text_info, template)
        # temp_dir_path = tempfile.mkdtemp()
        username = "test"
        temp_file_name = f'{username}_image' + str(time.time())
        os.mkdir(f'{settings.MEDIA_ROOT}/{temp_file_name}')
        for i, img in enumerate(image):
            media_url = f'{temp_file_name}/{username}_image_{i}.jpg'
            img_path = f'{settings.MEDIA_ROOT}/{media_url}'
            img.save(img_path)
            # del img
            if is_preview:
                #将图片保存到media中并返回url
                res_preview = {
                    'is_preview': True,
                    "img": f'/media/{media_url}'
                }
                print(media_url)
                return JsonResponse(res_preview)

        #将刚刚生成的图片保存后压缩成zip文件
        shutil.make_archive(f'{settings.MEDIA_ROOT}/{temp_file_name}', 'zip', f'{settings.MEDIA_ROOT}/{temp_file_name}')
        zip_file_path = f'{settings.MEDIA_URL}{temp_file_name}.zip'
        res = {
            'is_preview': False,
            "zip": zip_file_path
        }
        return JsonResponse(res)
def get_font_list(request):
    fonts = {'fonts': []}
    for key in settings.FONT_NAME_MAP:
        fonts['fonts'].append(key)
    return JsonResponse(fonts)





