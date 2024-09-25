import os
from wand.color import Color
from wand.image import Image

def swap_file_ext(filepath: str, newExt: str) -> str:
  splitpath = filepath.split('.')
  splitpath.pop(len(splitpath) - 1)
  return '.'.join(splitpath) + '.' + newExt

def convert_svg_to_png(filepath: str, outputdir: str) -> str:
  os.makedirs(outputdir, exist_ok=True)
  filename = os.path.basename(filepath)
  updatedFilepath = os.path.join(outputdir, swap_file_ext(filename, "png"))
  with Image(filename=filepath, background=Color("transparent"), resolution=144) as img:
    img.format = 'png'
    img.save(filename=updatedFilepath)
  return updatedFilepath

def convert_svgs_to_pngs(filepaths: list[str], outputdir: str) -> list[str]:
  pngpaths = []
  for filepath in filepaths:
    pngpath = convert_svg_to_png(filepath, outputdir)
    pngpaths.append(pngpath)
  return pngpaths

def get_filepaths_by_extension(dir: str, ext: str) -> list[str]:
  svgpaths: list[str] = []
  for subdir, dirs, files in os.walk(dir):
    for file in files:
      filepath: str = os.path.join(subdir, file)
      if (filepath.lower().endswith(ext)):
        svgpaths.append(filepath)
  return svgpaths
