import vapoursynth as vs
from PIL import Image
import cv2
import numpy as np

core = vs.core

try:
    core.std.LoadPlugin(r"D:\Python Stuff\BHDStudio-Upload-Tool\runtime\apps\image_comparison\ffms2.dll")
except vs.Error:
    pass

try:
    core.std.LoadPlugin(r"D:\Python Stuff\BHDStudio-Upload-Tool\runtime\apps\image_comparison\libvslsmashsource.dll")
except vs.Error:
    pass


# source_file = core.lsmas.LWLibavSource(r"C:\Users\jlw_4\Desktop\rugrats test\The.Rugrats.Movie.1998.1080p.BluRay.REMUX.AVC.TrueHD.5.1.mkv")
source_file = core.ffms2.Source(r"\\JLW-UNRAID\dl_share\downloads\FUTURAMA_MOVIE\Futurama.Bender's.Big.Score.2007.NTSC.DVD.Remux.DD.5.1.SacReD\Futurama.Bender's.Big.Score.2007.NTSC.DVD.Remux.DD.5.1.SacReD.mkv")
# source_file = source_file.resize.Spline16(format=vs.RGB24, matrix_in_s="470bg")
#
# VS_DTYPE_MAP = {
#     "RGB24": np.int8,
#     "RGB27": np.int16,
#     "RGB30": np.int16,
#     "RGB36": np.int16,
#     "RGB42": np.int16,
#     "RGB48": np.int16,
#     "RGBH": np.float16,
#     "RGBS": np.float32,
#     "GRAY8": np.int8,
#     "GRAY9": np.int16,
#     "GRAY10": np.int16,
#     "GRAY12": np.int16,
#     "GRAY14": np.int16,
#     "GRAY16": np.int16,
#     "GRAY32": np.int32,
#     "GRAYH": np.float16,
#     "GRAYS": np.float32,
#     "YUV410P8": np.int8,
#     "YUV411P8": np.int8,
#     "YUV420P8": np.int8,
#     "YUV420P9": np.int16,
#     "YUV420P10": np.int16,
#     "YUV420P12": np.int16,
#     "YUV420P14": np.int16,
#     "YUV420P16": np.int16,
#     "YUV422P8": np.int8,
#     "YUV422P9": np.int16,
#     "YUV422P10": np.int16,
#     "YUV422P12": np.int16,
#     "YUV422P14": np.int16,
#     "YUV422P16": np.int16,
#     "YUV440P8": np.int8,
#     "YUV444P8": np.int8,
#     "YUV444P9": np.int16,
#     "YUV444P10": np.int16,
#     "YUV444P12": np.int16,
#     "YUV444P14": np.int16,
#     "YUV444P16": np.int16,
#     "YUV444PH": np.float16,
#     "YUV444PS": np.float32
# }
#
# def get_frame_plane(f: vs.VideoFrame, n: int) -> np.array:
#   """
#   Get VapourSynth Frame's Plane as a Numpy Array.
#   For example, RGB frames would have three planes (Red, Green, Blue).
#   n of 0 would be RED plane assuming the plane order is RGB and not BGR.
#   """
#   return np.asarray(f[n], dtype=VS_DTYPE_MAP[f.format.name])
#
# def frame_to_array(f: vs.VideoFrame) -> np.stack:
#   """Convert a VapourSynth VideoFrame into a Numpy Array."""
#   return np.stack([
#     get_frame_plane(f, plane)
#     for plane in range(f.format.num_planes)
#   ])
#
# frame_array = frame_to_array(source_file.get_frame(123))
# print(frame_array)
# new_img = Image.fromarray(frame_array, "P").save(r"C:\Users\jlw_4\Desktop\test\testting.png")
import cv2
# import numpy as np
#
# clip = core.lsmas.LWLibavSource(r"C:\Users\jlw_4\Desktop\rugrats test\The.Rugrats.Movie.1998.1080p.BluRay.REMUX.AVC.TrueHD.5.1.mkv")
#
#
# def format_shuffles(n,f):
#     npArray = np.dstack([np.asarray(f[p]) for p in range(3)]) #latest vs: f[p] instead of f.get_read_array(p)
#     print(npArray)
#     #work here with npArray image
#     #hsv = cv2.cvtColor(npArray, cv2.COLOR_BGR2HSV)
#     PIL_img = Image.fromarray(npArray, 'RGB').save(r"C:\Users\jlw_4\Desktop\test\testting1.png")
#     #or work with PIL image than convert it back to np array
#     #npArray = np.array(PIL_img)
#     # f_out = f.copy()
#     # [np.copyto(np.asarray(f_out.get_write_array(p)), npArray[:, :, p]) for p in range(3)]
#     # return f_out
#
# clip = clip.resize.Point(format=vs.RGB24, matrix_in_s = '709')
# format_shuffles(0, clip.get_frame(20000))
# clip.set_output(0)


# for f in rgb.frames():
#     print(f)
#     img = np.dstack([np.asarray(f[p]) for p in [2,1,0]]) #or f[p] ...
#     print(img)
#     quit()
#     cv2.imshow('movie', img)
#     cv2.waitKey(1)

def frame_to_pil_via_numpy(f: vs.VideoFrame) -> Image:
    """Convert a VapourSynth Frame to a Pillow Image using Numpy."""
    if f.format.id not in (vs.RGB24, vs.GRAY8):
        raise ValueError("PIL only supports 8-bit-depth Grayscale or RGB input.")
    array = np.dstack([
        np.asarray(f[p])
        for p in range(f.format.num_planes)
    ])
    image = Image.fromarray(array, "RGB")
    return image


frame = source_file
frame = frame.resize.Point(format=vs.RGB24, matrix_in_s = '709').get_frame(15000)
frame_to_pil_via_numpy(frame).save(r"C:\Users\jlw_4\Desktop\test\testting2.png")