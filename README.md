# Road POV KM Marker Generator

这是一个用于生成道路公里桩标识图片的小工具。

## 项目简介

该项目通过 `km.py` 读取背景图片并渲染公里数、百米标、路线编号等文本，生成用于道路视角（road POV）公里标的 PNG 图片。

## 目录结构

- `km.py`：主脚本。清空 `output/` 目录并生成图片。
- `resources/`
  - `bg.png`：图片背景模板。
  - `B_PIL.ttf`：用于渲染文本的字体文件。
- `output/`：生成的 PNG 图片输出目录。
- `utils/font_size.py`：用于计算文本宽度的辅助模块。

## 运行环境

- Python 3.x
- Pillow

## 安装依赖

```bash
pip install pillow
```

## 使用说明

直接运行主脚本：

```bash
python km.py
```

运行后会：

1. 检查 `output/` 目录
2. 如果存在则删除其中所有文件，否则创建该目录
3. 读取 `resources/bg.png`
4. 生成从 `km_start` 到 `km_end` 的公里图片
5. 在每个公里内生成 10 张百米标记图片，保存到 `output/` 目录中

## 参数说明

`km.py` 中可根据需要修改以下变量：

- `seq`：路线编号，例如 `G15`
- `sub_seq`：子编号，例如 `23`
- `km_start`：开始公里数
- `km_end`：结束公里数

## 输出结果

生成的图片保存在 `output/` 目录，文件名为数字序号（如 `0.png`、`1.png`）。

## 注意事项

- 请确保 `resources/B_PIL.ttf` 字体文件存在且路径正确。
- `resources/bg.png` 应为合适尺寸的背景图片。
- 若需修改字体、颜色或位置，可在 `km.py` 中调整对应常量。
