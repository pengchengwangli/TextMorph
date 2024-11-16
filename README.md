# TextMorph

TextMorph 是一个用于文本生成手写字体的Web应用。

## 介绍

TextMorph 提供了一个简洁的界面，允许用户输入文本并生成模拟手写风格的图像。用户可以自定义字体、颜色、间距等参数，以生成个性化的手写效果。
前端基本是ChatGPT做的，使用了一个handright库[https://github.com/Gsllchb/Handright] ,还借鉴(我就是抄袭)了这个兄弟的写的[14790897/handwriting-web: 将文本转为模拟手写文字的网页版 (github.com)]

![image-20241117002536257](https://github.com/pengchengwangli/TextMorph/blob/master/imgs/image-20241117002536257.png)

![image-20241117002614239](.\imgs\image-20241117002614239.png)

![image-20241117002843234](.\imgs\image-20241117002843234.png)

![image-20241117002746452](.\imgs\image-20241117002746452.png)

![image-20241117002808132](.\imgs\image-20241117002808132.png)

## 功能

生成手写风格的文本图像
支持自定义字体和颜色
支持自定义纸张尺寸和边距

- `text_info`: 要生成的文本内容 (字符串)

- ```
  json_data
  ```

  : 包含以下可选参数的JSON对象:

  - `is_upload_image`: 是否上传背景图像 (布尔值)
  - `is_upload_font`: 是否上传自定义字体 (布尔值)
  - `custom_paper_size`: 自定义纸张尺寸，包含`w`和`h`属性 (对象)
  - `line_spacing`: 行间距 (整数)
  - `word_spacing`: 字间距 (整数)
  - `top_margin`: 上边距 (整数)
  - `bottom_margin`: 下边距 (整数)
  - `left_margin`: 左边距 (整数)
  - `right_margin`: 右边距 (整数)
  - `font_size`: 字体大小 (整数)
  - `font_name`: 字体名称，如'李国夫手写体' (字符串)
  - `font_color`: 字体颜色 (字符串，十六进制颜色值)
  - `line_spacing_sigma`: 行间距的标准差 (浮点数)
  - `font_size_sigma`: 字体大小的标准差 (浮点数)
  - `word_spacing_sigma`: 字间距的标准差 (浮点数)
  - `perturb_x_sigma`: 笔画横向偏移的标准差 (整数)
  - `perturb_y_sigma`: 笔画纵向偏移的标准差 (整数)
  - `perturb_theta_sigma`: 笔画旋转偏移的标准差 (浮点数)
  - `ink_depth_sigma`: 墨水深度的标准差 (浮点数)
  - `is_preview`: 是否生成预览图像 (布尔值)

支持预览功能

支持用户登录和下载历史记录

## 安装

1. 克隆仓库



```bash
git clone https://github.com/pengchengwangli/TextMorph.git
```

1. 进入项目目录



```bash
cd TextMorph
```

1. 创建虚拟环境并激活

bash

```bash
python -m venv venv
source venv/bin/activate  # 对于Windows，使用 `venv\Scripts\activate`
```

1. 安装依赖



```bash
pip install -r requirements.txt
```

1. 进行数据库迁移



```bash
python manage.py migrate
```

1. 启动开发服务器



```bash
python manage.py runserver
```

1. 在浏览器中打开 [http://localhost:8000](http://localhost:8000/)







