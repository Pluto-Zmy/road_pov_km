# Road POV KM Marker Generator

道路公里标帧图片生成器 —— 批量生成公里桩标记 PNG 帧，并合成为透明背景视频，用于道路 POV（第一人称视角）视频叠加。

## 功能特性

- 🖼️ **帧生成**：按公里范围批量生成 PNG 帧图片，每公里 10 帧（百米桩 0–9）
- 🎬 **视频合成**：通过 ffmpeg 将所有帧合成为 `.mov` 视频，支持透明通道（RGBA）
- 📊 **进度显示**：使用 tqdm 实时显示生成进度
- 🧹 **自动清理**：视频合成后自动删除中间帧和 output 目录

## 目录结构

```
.
├── km.py                 # 主脚本：生成帧图片并合成视频
├── resources/
│   ├── bg.png            # 背景模板图片
│   └── B_PIL.ttf         # 渲染用字体文件
├── utils/
│   └── font_size.py      # 文字宽度计算辅助模块
└── output/               # 生成输出目录（运行后自动创建和清理）
```

## 环境依赖

| 依赖 | 用途 | 安装方式 |
|------|------|----------|
| Python 3.x | 运行环境 | — |
| Pillow | 图像处理 / 文字渲染 | `pip install pillow` |
| tqdm | 进度条显示 | `pip install tqdm` |
| ffmpeg | PNG 帧合成视频 | `brew install ffmpeg`（macOS） |

## 安装

```bash
# 安装 Python 依赖
pip install pillow tqdm

# macOS 安装 ffmpeg
brew install ffmpeg

# 其他系统请参考 https://ffmpeg.org/download.html
```

## 使用方法

### 基本运行

```bash
python km.py
```

### 可配置参数

在 `km.py` 的 `__main__` 部分修改以下变量：

| 参数 | 说明 | 示例值 |
|------|------|--------|
| `seq` | 路线编号 | `'G10'` |
| `sub_seq` | 子编号（可空） | `''` 或 `'23'` |
| `km_start` | 起始公里数 | `0` |
| `km_end` | 结束公里数 | `346` |

### 布局与样式

可在文件顶部修改以下常量来调整样式：

| 常量 | 说明 |
|------|------|
| `LEFT_CENTER_X` / `RIGHT_CENTER_X` | 左右文字区域水平中心坐标 |
| `TOP_CENTER_Y` / `MID_CENTER_Y` / `BOTTOM_CENTER_Y` | 上/中/下文字区域垂直中心坐标 |
| `KM_LARGE_FONT_SIZE` / `KM_SMALL_FONT_SIZE` | 大/小公里数字体大小 |
| `HM_FONT_SIZE` | 百米桩字体大小 |
| `SEQ_FONT_SIZE` / `SUB_SEQ_FONT_SIZE` | 路线编号 / 子编号字体大小 |
| `WHITE` / `GREEN` | 文字颜色（RGB 元组） |

## 运行流程

1. 清空或创建 `output/` 目录
2. 加载 `resources/bg.png` 背景模板
3. 遍历 `km_start` 到 `km_end`，每公里生成 10 帧百米标图片（`0.png`, `1.png`, …）
4. 通过 ffmpeg 将所有 PNG 帧合成为 `km_{seq}{sub_seq}_K{km_start}-K{km_end}.mov`
5. 清理 output 目录及中间文件

## 输出说明

- **中间帧**：`output/` 目录下的数字序号 PNG 文件（视频合成后自动删除）
- **最终视频**：项目根目录下的 `.mov` 文件，命名格式如 `km_G10_K0-K346.mov`
- **视频规格**：透明通道（RGBA）、PNG 编码、默认 30fps

### 自定义视频参数

在调用 `compose_video()` 时可调整：

```python
compose_video(output_dir, video_name, fps=30)  # 修改 fps 改变帧率
```

## 注意事项

- 确保 `resources/B_PIL.ttf` 字体文件和 `resources/bg.png` 背景图片存在且路径正确
- 视频合成需要系统已安装 ffmpeg 命令行工具
- 生成大量帧时（如 0–346 公里 × 10 = 3470 帧），建议预留足够磁盘空间
- 视频文件使用 PNG 编码以保留透明通道，文件体积可能较大
