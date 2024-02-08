#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : cuntou0906
# @File    : ReshapeVideo.py
# @Time    : 2022/8/12 16:42

import cv2 as cv
import os


class Reshapevideo():
    def __init__(self, filename, Newfilename, Resize):
        self.filename = filename
        self.Newfilename = Newfilename
        self.Resize = Resize
        pass

    def Process(self):
        cap = cv.VideoCapture(filename)
        # 获取读入视频的参数
        fps = cap.get(cv.CAP_PROP_FPS)
        width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)

        print(width, height)
        intx0 = self.Resize[2]
        intx1 = self.Resize[3]

        inty0 = self.Resize[0]
        inty1 = self.Resize[1]
        wid = range(intx0, intx1)
        hei = range(inty0, inty1)
        size = (int(hei[-1] - hei[0]) + 1, int(wid[-1] - wid[0]) + 1)

        # 创建视频写入对象
        format = self.Newfilename.split('.')
        format = format[len(format)-1]
        print(format)
        if format == 'mp4':
            fourcc = cv.VideoWriter_fourcc(*'mp4v')
        elif format == 'avi':
            fourcc = cv.VideoWriter_fourcc(*'XVID')

        out = cv.VideoWriter(self.Newfilename, fourcc, fps, size)

        # 读取视频帧，然后写入文件并在窗口显示
        success, frame_src = cap.read()
        while success and not cv.waitKey(1) == 27:  # 读完退出或者按下 esc 退出
            frame_target = frame_src[intx0:intx1, inty0:inty1]
            # print(frame_target.shape)

            # 写入视频文件
            out.write(frame_target)

            # 显示裁剪的视频和原视频
            cv.imshow("video", frame_target)
            cv.imshow("Video_src", frame_src)

            # 不断读取
            success, frame_src = cap.read()

        print("视频裁剪完成")
        # 销毁窗口，释放资源
        cv.destroyWindow("video")
        cv.destroyWindow("Video_src")
        cv.destroyAllWindows()
        cap.release()
        out.release()
        pass


if __name__ == "__main__":
    # 参数说明
    # filename 原始文件路径
    # Newfilename 新文件路径，支持mp4和avi
    # ReSize：裁剪尺寸（左，右，上，下） 单位像素点

    path = "D:\CoachAI-Projects-main\CoachAI-Projects-main\ShuttleSet\set"
    for dir in os.listdir(path):
        if os.path.isdir(os.path.join(path, dir)):
            folder = os.path.join(path, dir)
            for file in os.listdir(folder):
                if file.endswith("mp4"):
                    filename = os.path.join(folder, file)
                    Newfilename_A = os.path.join(folder, "A_" + file)
                    Newfilename_B = os.path.join(folder, "B_" + file)
                    print(Newfilename_A, Newfilename_B)
                    Resize_A = (480, 1440, 200, 600)
                    Resize_B = (480, 1440, 500, 1080)
                    ReshapevideoObj_A = Reshapevideo(filename, Newfilename_A, Resize_A)
                    ReshapevideoObj_B = Reshapevideo(filename, Newfilename_B, Resize_B)
                    ReshapevideoObj_A.Process(),
                    ReshapevideoObj_B.Process()

    #ReSize = (0, 1920, 0, 540)
    #ReshapevideoObj = Reshapevideo(filename, Newfilename, ReSize)
    #ReshapevideoObj.Process()
