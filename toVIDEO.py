""" 
This library will be used for conversion into video
A class per file type will be defined
"""

# No 3go, no webm
import mainFunctions as mf
import os
from datetime import datetime as dt
from toAUDIO import a_convert as alc
from toIMG import ModifyToImg as mit
from moviepy.video.tools.drawing import color_gradient as cg
import moviepy.video.fx as mvf
from moviepy import concatenate_videoclips as cvc, convert_to_seconds as cts
import moviepy as mvp

TEMPCACHES = "tempcaches"

cts
def list_fonts():
    font_dirs = [r"C:\Windows\Fonts"]
    fonts = []
    for font_dir in font_dirs:
        for root, dirs, files in os.walk(font_dir):
            type(dirs)
            for file in files:
                if file.lower().endswith(('.ttf', '.otf')):
                    fonts.append(os.path.join(root, file))
    return fonts


FONTDIR = list_fonts()
FONTS = [os.path.splitext(os.path.basename(ww))[0] for ww in FONTDIR]
FONTDICT = {FONTS[ww]: FONTDIR[ww] for ww in range(len(FONTS))}




def v_convert(pathF, pathT=None,):
    if not pathT:pathT = f"{TEMPCACHES}/tc-{dt.now()}.mp4".replace(":", "")
    video = mvp.VideoFileClip(pathF)
    video.write_videofile(pathT, codec="libx264", audio_codec="aac")


def v_acceldecel(video, param={}):
    """
    :param1 duration = float|None,1 to video.duration -> total duration of video;
    :param2 abruptness = float|1, 0 to infinite -> speed of acceleration
    :param3 soonness: float|1, 0 to video.duration -> IDK
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.AccelDecel(param.get("duration", None), param.get("abruptness", 1), param.get("soonness", 1)).apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_bg(video, param={}):
    """ 
    :param size = any|None, (width, height) -> set the size of background;
    :param color = tuple|(0, 0, 0), (r, g, b) -> set the color of background;
    :param pos = any|None, (x, y) -> set the position of background;
    :param opacity = any|None, from 0 to 1 -> set the opacity
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = v[xx][1].with_background_color(param.get("size", None),
                                       param.get("color", (0, 0, 0)),
                                        param.get("pos", None),
                                        param.get("opacity", None)) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_blackandwhite(video, param={}):
    """
    :param RGB = str|None, (R, G, B) -> idk
    :param luminosity = bool|True, (False) -> considere luminosity or not
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.BlackAndWhite(param.get("rgb", None), param.get("luminosity", True)).apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_blink(video, param={}):
    """ 
    :param on = float;
    :param off= float;
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.Blink(param.get("on", 1), param.get("off", 1)).apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_crop(video, param={}):
    """ 
    :param x1 = int|None;
    :param y1 = int|None;
    :param x2 = int|None;
    :param y2 = int|None;
    :param width = int|None;
    :param height = int|None;
    :param x_center = int|None;
    :param y_center = int|None;
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.Crop(param.get("x1", None), param.get("y1", None), param.get("x2", None), param.get("y2", None),
                    param.get("width", None), param.get("height", None), param.get("x_center", None),
                    param.get("y_center", None)).apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_crossfadein(video, param={}):
    """
    :param duration = float|1, from x>0 to video.duration -> the duration of fade;
    :param initial_color = tuple|None, (R, G, B) -> the initial color of fade
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.CrossFadeIn(param.get("duration", 1)).apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_crossfadeout(video, param={}):
    """
    :param duration = float|1, from x>0 to video.duration -> the duration of fade;
    :param final_color = tuple|None, (R, G, B) -> the initial color of fade
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.CrossFadeOut(param.get("duration", 1)).apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_duration(video, param={}):
    """
    :param duration = float|video.duration, from x>0 to video.duration -> set the max duration of video
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = v[xx][1].with_duration(param.get("duration", v[xx][1].duration)) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_evensize(video, param={}):
    """Resize the video with a valid format"""
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.EvenSize().apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_fadein(video, param={}):
    """
    :param duration = float|1, from x>0 to video.duration -> the duration of fade;
    :param initial_color = tuple|None, (R, G, B) -> the initial color of fade
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.FadeIn(param.get("duration", 1), param.get("initial_color", None)).apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_fadeout(video, param={}):
    """
    :param duration = float|1, from x>0 to video.duration -> the duration of fade;
    :param final_color = tuple|None, (R, G, B) -> the initial color of fade
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.FadeOut(param.get("duration", 1), param.get("initial_color", None)).apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_fps(video, param={}):
    """
    :param fps = int|video.fps, from 1 to infinity -> the fps of video
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = v[xx][1].with_fps(param.get("fps", v[xx][1].fps)) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_freeze(video, param={}):
    """ 
    :param t = float|0, 0 to video.duration -> where the freeze start;
    :param duration = float|None, from 0 to videro.duration-t -> duration of freeze
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.Freeze(param.get("time", 0), param.get("duration", None)).apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_freezeregion(video, param={}):
    """ 
    :param time = float|0, from 0 to video.duration;
    :param region = tuple|None, (x1, y1, x2, y2) -> the region that will be freezed
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.FreezeRegion(param.get("time", 0), param.get("region", None)).apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_gamma(video, param={}):
    """ 
    :param gamma = float, from -infinity to +infinity -> more gamma = less color
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.GammaCorrection(param.get("gamma", 1)).apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_invertcolor(video, param={}):
    """Inverte colors"""
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.InvertColors().apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_loop(video, param={}):
    """
    :param n = int|None, from 1 to infinity -> number of time the video will be repeated;
    :param duration = float|None, from 0 to video.duration -> the duration of the part which will be repeated
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.Loop(param.get("n", None), param.get("duration", None)).apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_lumcontrast(video, param={}):
    """ 
    :param lum = float|0, from -220 to 220 -> the luminosity
    :param contrast = float|0, from -220 to 220 -> the contrast
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.LumContrast(param.get("lum", 0), param.get("contrast", 0)).apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_makeloopable(video, param={}):
    """
    :param overlap = float, from 0 to video.duration -> make the video loopable (idk how to explain)
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.MakeLoopable(param.get("overlap", 0)).apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_margin(video, param={}):
    """
    :param margin = int|None, from 0 to infinity -> margin for all side in px;
    :param left = int|0, from 0 to infinity -> margin for left side;
    :param right = int|0, from 0 to infinity -> margin for right side;
    :param top = int|0, from 0 to infinity -> margin for top side;
    :param bottom = int|0, from 0 to infinity -> margin for bottom side;
    :param color = tuple|(0,0,0), (r, g, b) -> color of margin;
    :param opacity = float|1, from 0 to 1 -> opacity of margin
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.Margin(param.get("margin", None), param.get("left", 0), param.get("right", 0),
                      param.get("top", 0), param.get("bottom", 0), param.get("color", (0, 0, 0)),
                      param.get("opacity", 1)).apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_mirrorx(video, param={}):
    """Return the xmirror"""
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.MirrorX().apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_mirrory(video, param={}):
    """Return the ymirror"""
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.MirrorY().apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_multiplycolor(video, param={}):
    """
    :param factor = float, from -infinity to +infity -> Multiply the color
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.MultiplyColor(param.get("factor", 1)).apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_multiplyspeed(video, param={}):
    """ 
    :param factor: float|None, from x>0 to 64 -> multiply the speed of video
    :param duration: float|None, from .1 to video.duration*1000 -> the speed will depend on the total final_duration
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.MultiplySpeed(param.get("factor", None), param.get("duration", None)).apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_opacity(video, param={}):
    """
    :param opacity = float|1, from 0 to 1 -> set the opacity
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = v[xx][1].with_opacity(param.get("opacity", 1)) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_painting(video, param={}):
    """ 
    :param saturation = float|1.4, from -infinity to +infinity -> more saturation = less color;
    :param black = float|.006, from -infinity to +infinity -> more black = more black line
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.Painting(param.get("saturation", 1.4), param.get("black", .006)).apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_position(video, param={}):
    """
    :param position = tuple, (x, y) -> set the position of video
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = v[xx][1].with_position(param.get("position", None)) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_rotate(video, param={}):
    """ 
    :param angle = float, from -infinity to +infinity -> rotate video by angle;
    :param expand = bool|True, False -> expand the video or not;
    :param center = tuple|None, (x, y) -> set the center of rotation;
    :param bg = tuple|None, (r, g, b) -> set the background
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.Rotate(param.get("angle", 0), "deg", "bicubic", param.get("expand", True),
                      param.get("center", None), None, param.get("bg", None)).apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_scroll(video, param={}):
    """ 
    :param w = int|None, from -video.w to video.w -> width;
    :param h = int|None, from -video.h to video.h -> height;
    :param x_speed = int|0, from -infinity to +infinity -> idk;
    :param x_speed = int|0, from -infinity to +infinity -> idk;
    :param x_start = int|0, from -infinity to +infinity -> the origine x point;
    :param y_start = int|0, from -infinity to +infinity -> the origine y point
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.Scroll(param.get("w", None), param.get("h", None), param.get("x_speed", 0),
                      param.get("y_speed", 0), param.get("x_start", 0), param.get("y_start", 0)).apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_slidein(video, param={}):
    """ 
    :param duration = int, from 0 to video.duration -> the duration of slide;
    :param side = str, left, top, right, bottom -> comes from the direction;
    !!!cannot be combined with slideout!!!
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.SlideIn(param.get("duration", 1), param.get("side", "left")).apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_slideout(video, param={}):
    """ 
    :param duration = int, from 0 to video.duration -> the duration of slide;
    :param side = str, left, top, right, bottom -> comes from the direction;
    !!!cannot be combined with slidein!!!
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.SlideOut(param.get("duration", 1), param.get("side", "right")).apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_subclipped(video, param={}):
    """
    :param start = float|0, from 0 to x<ideo.duration -> when it starts;
    :param en = float|video.duration, from x>0 to video.duration -> when it stops
    """
    return video.subclipped(param.get("start", 0), param.get("end", video.duration))


def v_supersample(video, param={}):
    """ 
    :param d = float, from x>0 to infinity -> idk;
    :param n = int, from 1 to 10 -> idk
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = mvf.SuperSample(param.get("d", 1), param.get("n", 1)).apply(v[xx][1]) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_time(video, param={}):
    """
    :param mirror = bool|False, True -> to reverse the video;
    :param symetry = bool|False, True -> to make a reverse symetry
    """
    v1 = mvp.ColorClip(size=(video.w, video.h), duration=1.8, color=(0, 0, 0))
    v2 = mvp.ColorClip(size=(video.w, video.h), duration=1.8, color=(0, 0, 0))
    video = mvp.concatenate_videoclips([v1, video, v2])
    temp = f"{TEMPCACHES}/tc-{dt.now()}.mp4".replace(":", "")
    video.write_videofile(temp)
    video = mvp.VideoFileClip(temp)
    video = video.subclipped(2, video.duration - 2)
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        if param.get("mirror", False):v[xx][1] = mvf.TimeMirror().apply(v[xx][1]) if v[xx][0] else v[xx][1]
        if param.get("symetry", False):v[xx][1] = mvf.TimeSymmetrize().apply(v[xx][1]) if v[xx][0] else v[xx][1]
        v[xx] = v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


def v_volume(video, param={}):
    """ 
    :param factor = float|1, from 0 to 100 -> set the volumne;
    :param start = float|None, from 0 to video.duration -> when the volume changed starts;
    :param end = float|None, from 0 to video.duration -> when the volume changed stops;
    """
    start, end = param.get("interval", [0, video.duration])
    v = []
    if start != 0:v.append([None, video.subclipped(0, start)])
    v.append([True, video.subclipped(start, end)])
    if end < video.duration:v.append([None, video.subclipped(end, video.duration)])
    for xx, ww in enumerate(v):
        v[xx] = v[xx][1].with_volume_scaled(param.get("factor", 1),
                                          param.get("start", None),
                                          param.get("end", None)) if v[xx][0] else v[xx][1]
    video = v[0]
    if len(v) > 1:
        for ww in v[1:]:
            video += ww
    return video


class Gradient:

    def __init__(self, size, p1, p2, vector=None, radius=None, col1=0, col2=0, shape="linear", offset=0, duration=None):
        """
        :param size = any, (width, height -> the total dimension);
        :param p1 = tuple, (x1, y2) -> starting point;
        :param p2 = tuple, (x2, y2) -> ending point;
        :param vector = tuple|None, (a, b) -> center;
        :param radius = any|None, tuple(x, y) or int -> the radius of gradient;
        :param col1 = tuple|0, (R, G, B) -> the first color;
        :param col2 = tuple|0, (R, G, B) -> the second color;
        :param shape = str|linear, bilinear, radial -> the type of gradient;
        :param offset = int|0, from 0 to 1 -> idk
        :param duration = int|None, from x>0 to infinity -> set the duration
        """
        self.size = size
        self.p1 = p1
        self.p2 = p2
        self.vector = vector
        self.radius = radius
        self.col1 = col1
        self.col2 = col2
        self.shape = shape
        self.offset = offset
        self.duration = duration
        
    def set(self, size=None, p1=None, p2=None, vector=None, radius=None, col1=None, col2=None, shape=None, offset=None, duration=None):
        self.size = size if size else self.size
        self.p1 = p1 if p1 else self.p1
        self.p2 = p2 if p2 else self.p2
        self.vector = vector if vector else self.vector
        self.radius = radius if radius else self.radius
        self.col1 = col1 if col1 else self.col1
        self.col2 = col2 if col2 else self.col2
        self.shape = shape if shape else self.shape
        self.offset = offset if offset else None
        self.duration = duration if duration != None else self.duration
        return self

    def writeImage(self, path):
        name = mf.Return(mf.getName(path)).getValues(0)
        ext = mf.Return(mf.getExtension(path)).getValues(0)
        return mvp.VideoClip(lambda t: cg(self.size, self.p1, self.p2, self.vector,
                                        self.radius, self.col1, self.col2, self.shape,
                                        self.offset), duration=1).write_images_sequence(f"{name}%03d.{ext}", fps=1)[0]

    def writeImageSequence(self, path, fps=24):
        name = mf.Return(mf.getName(path)).getValues(0)
        ext = mf.Return(mf.getExtension(path)).getValues(0)
        return mvp.VideoClip(lambda t: cg(self.size, self.p1, self.p2, self.vector,
                                        self.radius, self.col1, self.col2, self.shape,
                                        self.offset), duration=self.duration).write_images_sequence(f"{name}%03d.{ext}", fps=fps)

    def get(self):
        return mvp.VideoClip(lambda t: cg(self.size, self.p1, self.p2, self.vector,
                                          self.radius, self.col1, self.col2, self.shape,
                                          self.offset), duration=self.duration)   


def mv_text(font=FONTDIR[0], text="TEXT", filename=None, font_size=11,
          size=(None, None), margin=(0, 0), fg=None, bg=None,
          stroke_bg=None, stroke_width=1, method="label",
          text_align="center", horizontal_align="center",
          vertical_align="center", interline=4, transparent=True,
          duration=1):
    """
    :param font = str|FONTDIR[0], path of font -> text font;
    :param text = str|None, any -> text;
    :param filename = str|None, path of text file -> text;
    :param font_size = int|11, from 1 to infinity -> size of text;
    :param size = tuple|(None, None), (width, height) -> dimension of text;
    :param margin = tuple|(0, 0), (horizontal, vertical) or (left, top, right, bottom) -> the margin of text;
    :param fg = tuple|None, (R, G, B, A 0-500) -> the color of text;
    :param bg = tuple|None, (R, G, B, A 0-500) -> the background of text;
    :param stroke_bg = tuple|None, (R, G, B, A 0-500) -> color of strone. None = No stroke;
    :param stroke_width = int|1, from -infinity to +infinity -> width of stroke;
    :param method = str|label, caption -> idk;
    :param text_align = str|center, left, right -> text align;
    :param horozontal_align = str|center, left right -> the horizontal align of text by a center;
    :param vertical_align = str|center, top bottom -> the vertical align of text by a center;
    :param interline = int|4, from -infinity to +infinity -> the  spacement between lines;
    :param transparent = bool|True, False -> allows the transparent or not;
    :param duration = int|1, from x>0 to infinity -> set the duration;
    """
    return mvp.TextClip(font, text, filename, font_size, size, margin,
                        fg, bg, stroke_bg, stroke_width, method,
                        text_align, horizontal_align, vertical_align,
                        interline, transparent, duration)


def mv_color(size=(0, 0), color=None, mask=False, duration=1):
    """ 
    :param size = tuple|(0,0), (width, height) -> size of color;
    :param color = tuple|None, (R, G, B, A 0-500) -> color;
    :param mask = bool|False, True -> idk -> keep it false;
    :param duration = float|1, from x>0 to infinity -> the duration
    """
    return mvp.ColorClip(size, color, mask, duration)


class VideoToVideo:

    def __init__(self, file):
        self.file = file if type(file) == list else [file]
        self.stop = False
        self.toKill = None
        self.progressShow = None

    def toVIDEO(self, path):
        path = path if type(path) == list else [path]
        _ = list()
        for xx, ww in enumerate(self.file):
            if not self.stop:
                try:
                    self.toKill = mvp.VideoFileClip(ww)
                    self.toKill.write_videofile(path[xx], codec="libx264", audio_codec="aac")
                    _.append(mf.setReturn(True, [type(path[xx])], [path[xx]]))
                except Exception as e:
                    _.append(mf.setReturn(False, [type(e)], [e]))
                if self.progressShow:
                    self.progressShow(int(xx * 100 / len(path[xx])))
            else:
                for i in _:
                    try:
                        os.remove(mf.Return(i).getValues(0))
                    except Exception as e:
                        print(e)
                _=[]
                break
        if self.progressShow:
            self.progressShow(100, True, self.stop, _)
        return _

    def kill(self):
        self.stop = True
        if self.toKill:
            try:
                self.toKill.close()
            except Exception as e:
                print(e)


def v_apply(t, path, param={}):
    if t == "video":
        video = mvp.VideoFileClip(path)
    elif t == "img":
        temp = f"{TEMPCACHES}/tc-{dt.now()}.png".replace(":", "")
        temp=mf.Return(mit("").Convert(path, [], param.get("p_convert", {}))[0]).getValues(0)
        video = mvp.ImageClip(temp, duration=param.get("duration", 1))
    elif t == "imgseq":
        temp=[]
        for ww  in mit("").Convert(path, [], param):
            if mf.Return(ww).getSucced():
                temp.append(mf.Return(ww).getValues(0))
        video = mvp.ImageSequenceClip(temp, param.get("fps", 24), param.get("duration"))
    elif t == "text":
        video = mv_text(param.get("font", FONTDIR[0]), "", path, param.get("font_size", 11),
                      param.get("size", (None, None)), param.get("margin", (0, 0)), param.get("fg", None),
                      param.get("bg", None), param.get("stroke_bg", None), param.get("stroke_width", 1),
                      param.get("method", "label"), param.get("text_align", "center"),
                      param.get("horizontal_align", "center"), param.get("vertical_align", "center"),
                      param.get("interline", 4), param.get("transparent", True), param.get("duration", 1))
    elif t == "string":
        video = mv_text(param.get("font", FONTDIR[0]), path, None, param.get("font_size", 11),
                      param.get("size", (None, None)), param.get("margin", (0, 0)), param.get("fg", None),
                      param.get("bg", None), param.get("stroke_bg", None), param.get("stroke_width", 1),
                      param.get("method", "label"), param.get("text_align", "center"),
                      param.get("horizontal_align", "center"), param.get("vertical_align", "center"),
                      param.get("interline", 4), param.get("transparent", True), param.get("duration", 1))
    elif t == "color":
        video = mv_color(param.get("size", (0, 0)), param.get("color", None),
                       param.get("mask", False), param.get("duration", 1))
    elif t == "gradient":
        video = Gradient(param["size"], param["p1"], param["p2"], param.get("vector", None), param.get("radius", None),
                       param.get("col1", 0), param.get("col2", 0), param.get("shape", "linear"), param.get("offset", 0),
                       param.get("duration", 1)).get()
    elif t == "audio":
        video = mv_color((1, 1))
        audio = mvp.AudioFileClip(path)
        video.duration = audio.duration
        video.audio = audio
    else:video = path
    if param.get("v_subclipped"):
        video = v_subclipped(video, param["v_subclipped"])
    if param.get("v_bg"):
        video = v_bg(video, param["v_bg"])
    if param.get("v_blackwhite"):
        video = v_blackandwhite(video, param["v_blackandwhite"])
    if param.get("v_blink"):
        video = v_blink(video, param["v_blink"])
    if param.get("v_crop"):
        video = v_crop(video, param["v_crop"])
    if param.get("v_crossfadein"):
        video = v_crossfadein(video, param["v_crossfadein"])
    if param.get("v_crossfadeout"):
        video = v_crossfadeout(video, param["v_crossfadeout"])
    if param.get("v_duration"):
        video = v_duration(video, param["v_duration"])
    if param.get("v_evensize"):
        video = v_evensize(video, param["v_evensize"])
    if param.get("v_fadein"):
        video = v_fadein(video, param["v_fadein"])
    if param.get("v_fadeout"):
        video = v_fadeout(video, param["v_fadeout"])
    if param.get("v_fps"):
        video = v_fps(video, param["v_fps"])
    if param.get("v_freeze"):
        video = v_freeze(video, param["v_freeze"])
    if param.get("v_freezeregion"):
        video = v_freezeregion(video, param["v_freezeregion"])
    if param.get("v_gamma"):
        video = v_gamma(video, param["v_gamma"])
    if param.get("v_invertcolor"):
        video = v_invertcolor(video, param["v_invertcolor"])
    if param.get("v_loop"):
        video = v_loop(video, param["v_loop"])
    if param.get("v_lumcontrast"):
        video = v_lumcontrast(video, param["v_lumcontrast"])
    if param.get("v_makeloopable"):
        video = v_makeloopable(video, param["v_makeloopable"])
    if param.get("v_margin"):
        video = v_margin(video, param["v_margin"])
    if param.get("v_mirrox"):
        video = v_mirrorx(video, param["v_mirrorx"])
    if param.get("v_mirrory"):
        video = v_mirrory(video, param["v_mirrory"])
    if param.get("v_multiplycolor"):
        video = v_multiplycolor(video, param["v_multiplycolor"])
    if param.get("v_multipyspeed"):
        video = v_multiplyspeed(video, param["v_multiplyspeed"])
    if param.get("v_painting"):
        video = v_painting(video, param["v_painting"])
    if param.get("v_opacity"):
        video = v_opacity(video, param["v_opacity"])
    if param.get("v_position"):
        video = v_position(video, param["v_position"])
    if param.get("v_rotate"):
        video = v_rotate(video, ["v_rotate"])
    if param.get("v_slidein"):
        video = v_slidein(video, param["v_slidein"])
    if param.get("v_slideout"):
        video = v_slideout(video, param["v_slideout"])
    if param.get("v_scroll"):
        video = v_scroll(video, param["v_scroll"])
    if param.get("v_supersample"):
        video = v_supersample(video, param["v_supersample"])
    if param.get("v_time"):
        video = v_time(video, param["v_time"])
    if param.get("v_volume"):
        video = v_volume(video, param["v_volume"])
    if param.get("a_config"):
        ap = f"{TEMPCACHES}/tc-{dt.now()}.wav".replace(":", "")
        video.audio.write_audiofile(ap)
        video.audio = mvp.AudioFileClip(alc(ap, modify=param["a_config"]))
    return video


class MixedToVideo:

    def __init__(self, *file):
        self.file = [*file]
        self.progressShow = None

    def toVIDEO(self, path):
        path = path if type(path) == list else [path]
        _ = list()
        for xx, ww in enumerate(self.file):
            if self.progressShow:
                self.progressShow(int(xx * 100 / len(self.file)), 0)
            lctv = []
            lcbv = []
            for yy, zz in enumerate(ww["concatenat"]):
                lcbv.append(v_apply(zz[0], zz[1], zz[2]))
                if self.progressShow:
                    self.progressShow(int(xx * 100 / len(self.file)), int(yy * 100 / len(ww["concatenat"])))
            lcbv = cvc(lcbv, method=ww.get("concatenat_method", "chain"))
            maxDuration = lcbv.duration
            if ww.get("superposition"):
                for yy, zz in enumerate(ww["superposition"]):
                    lctv.append(v_apply(zz[0], zz[1], zz[2]))
                    lctv[-1] = lctv[-1].with_start(zz[2].get("with_start", 0))
                    if zz[2].get("with_end", maxDuration) - zz[2].get("with_start", 0) >= maxDuration:
                        mama = lctv[-1].duration if lctv[-1].duration - zz[2].get("with_start", 0) < maxDuration else maxDuration
                        lctv[-1] = lctv[-1].with_end(mama - zz[2].get("with_start", 0))
                    else:lctv[-1] = lctv[-1].with_end(zz[2].get("with_end", 0))
                    print(zz)
                    lctv[-1] = lctv[-1].resized(zz[2].get("dimension", (lctv[-1].w, lctv[-1].h)))
                    if self.progressShow:
                        self.progressShow(int(xx * 100 / len(self.file)), int(yy * 100 / len(ww["superposition"])))
            lctv.insert(0, lcbv)
            video = mvp.CompositeVideoClip(lctv)
            video.write_videofile(path[xx], codec="libx264", audio_codec="aac")
            print(path[xx])
        if self.progressShow:
            self.progressShow(100, 100, True)



