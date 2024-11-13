import io
import json

from PIL import Image, ImageFont
# from PIL.ImageFont import ImageFont
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from handright import Template, handwrite
# 导入settings.py中的配置
from TextMorph import settings


# Create your views here.
@csrf_exempt
def generate_handwritten_image(request):
    if request.method == 'GET':
        return render(request, 'test_01.html')
    else:

        json_test = request.POST.get('json_data')
        json_data = json.loads(json_test)
        # 是否上传了图片布尔值变量名
        is_upload_image = json_data['is_upload_image']
        # 是否上传了自定义字体文件
        is_upload_font = json_data['is_upload_font']
        # 纸张大小
        paper_size = json_data['paper_size']
        # 自定义纸张长宽
        custom_paper_size = json_data['custom_paper_size']
        # 行距
        line_spacing = json_data['line_spacing']
        # 列距
        column_spacing = json_data['column_spacing']
        # 上边距
        top_margin = json_data['top_margin']
        # 下边距
        bottom_margin = json_data['bottom_margin']
        # 左边距
        left_margin = json_data['left_margin']
        # 右边距
        right_margin = json_data['right_margin']
        # 字体大小
        font_size = json_data['font_size']
        # 字体
        font_name = json_data['font']
        # 字体颜色
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
        #删除线出现的概率
        strikethrough_probability = json_data['strikethrough_probability']
        #墨水深度的标准差
        ink_depth_sigma = json_data['ink_depth_sigma']
        if is_upload_image:
            image_file = request.FILES.get('image')
            # image 是 UploadedFile 的一个实例，它是 Django 提供的用于处理文件上传的类。该类包含与上传文件交互的属性和方法，例如 name、size、content_type、read() 和 chunks()。
            image_data = io.BytesIO(image_file.read())
            image = Image.open(image_data)
            # 将图形转换成GRB格式
            # image_data = image_data.getvalue()
        else:
            image = Image.new(mode="1", size=(custom_paper_size['w'], custom_paper_size['h']), color=1)
        if is_upload_font:
            font_file = request.FILES.get('font_file')
            font_data = io.BytesIO(font_file.read())
            font = ImageFont.truetype(font_data, size=font_size)
        else:
            font_path = settings.FONT_PATH / settings.FONT_NAME_MAP[font_name]
            with open(font_path, 'rb') as f:
                font_data = io.BytesIO(f.read())
            font = ImageFont.truetype(font_data, size=font_size)
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
        strikethrough_length_sigma: Optional[float]=None,  # 删除线长度的标准差，可选浮点数，默认为None
        strikethrough_angle_sigma: float = _DEFAULT_strikethrough_angle_sigma,  # 删除线角度的标准差，浮点数，默认值为_DEFAULT_strikethrough_angle_sigma
        strikethrough_width_sigma: Optional[float]=None,  # 删除线宽度的标准差，可选浮点数，默认为None
        strikethrough_probability: float = _DEFAULT_strikethrough_probability,  # 删除线出现的概率，浮点数，默认值为_DEFAULT_strikethrough_probability
        strikethrough_width: Optional[float]=None,  # 删除线宽度，可选浮点数，默认为None
        ink_depth_sigma: Optional[float]=None,  # 墨水深度的标准差，可选浮点数，默认为None
        features: Set = _DEFAULT_FEATURES,  # 额外特性，集合，默认值为_DEFAULT_FEATURES
        """
        template = Template(
            background=image,
            font=font,
            line_spacing=line_spacing,
            fill=font_color,  # 字体“颜色”
            left_margin=left_margin,
            top_margin=top_margin,
            right_margin=right_margin,
            bottom_margin=bottom_margin,
            word_spacing=word_spacing_sigma,
            line_spacing_sigma=line_spacing_sigma,  # 行间距随机扰动
            font_size_sigma=font_size_sigma,  # 字体大小随机扰动
            word_spacing_sigma=word_spacing_sigma,  # 字间距随机扰动
            start_chars=start_chars,  # 特定字符提前换行，防止出现在行尾
            end_chars=end_chars,  # 防止特定字符因排版算法的自动换行而出现在行首
            perturb_x_sigma=perturb_x_sigma,  # 笔画横向偏移随机扰动
            perturb_y_sigma=perturb_y_sigma,  # 笔画纵向偏移随机扰动
            perturb_theta_sigma=perturb_theta_sigma,  # 笔画旋转偏移随机扰动
            strikethrough_probability=strikethrough_probability,  # 删除线出现的概率
            ink_depth_sigma = ink_depth_sigma
        )