import cv2
import os

def k(x):
    return int(x.split('.')[0])

# 设置输入图片文件夹路径和输出视频文件名
image_folder = 'output'
video_name = 'output_video.avi'
frame_duration = 30  # 每帧持续时间（单位：毫秒）

# 获取图片文件夹下所有图片文件名并按顺序排序
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
images.sort(key=k)

# 读取第一张图片，获取图片尺
frame = cv2.imread(os.path.join(image_folder, images[0]), cv2.IMREAD_UNCHANGED)
height, width = frame.shape[:2]

# 创建视频写入对象
video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'XVID'), 30, (width,height), isColor=True)

# 遍历图片列表，将每张图片写入
for image in images:
    img = cv2.imread(os.path.join(image_folder, image))
    
    # 写入指定持续时间的
    for _ in range(frame_duration):
        video.write(img)

# 释放资源
cv2.destroyAllWindows()
video.release()