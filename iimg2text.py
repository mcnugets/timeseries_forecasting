import easyocr
import pathlib
from typing import List
from pathlib import Path
import numpy as np

class img2text:
    def __init__(self):
        self.reader = easyocr.Reader(['ru', 'en'], gpu=False)

    def process_images(self, images: List[str]):
        """Rener miltitude of  images"""
        if not isinstance(images, list):
            raise TypeError("process_images expects a list of image paths")
        output_cache = []
        for img in images:
            try:
                rendered_img = self.render_image(img)
                output_cache.append(rendered_img)
            except Exception as e:
             
                output_cache.append({"image": str(img), "error": str(e)})
        return output_cache

    def render_image(self, image: str):
        """Rener single image"""
        try:
            if image is None:
                raise ValueError("image argument is None")
            result = self.reader.readtext(image)
            return result
        except Exception as e:
           
            raise RuntimeError(f"Failed to render image {image}: {e}") from e

    def open_images(self, path: str):
        """Open dir of images."""
        try:
            the_path = pathlib.Path(path)
            img_list = [str(item) for item in the_path.iterdir() if item.is_file()]
            return img_list
        except Exception as e:
            raise RuntimeError(f"Failed to open images at {path}: {e}") from e

        
    def convert_numpy(self, obj):
        """Recursively convert NumPy types to Python types."""
        if isinstance(obj, np.ndarray):
            return obj.tolist()

        if isinstance(obj, np.generic):
            try:
                return obj.item()
            except Exception:
                
                if isinstance(obj, (np.integer,)):
                    return int(obj)
                if isinstance(obj, (np.floating,)):
                    return float(obj)
        if isinstance(obj, dict):
            return {k: self.convert_numpy(v) for k, v in obj.items()}
        if isinstance(obj, (list, tuple)):
            return [self.convert_numpy(item) for item in obj]
        return obj

    def run_ocr(self, path: str):
        """
        Runs ocr to extract characters

        Parameters
        ----------
        :param path: directory for all the images to process
        :type path: str
        """
        try:
            img_list = self.open_images(path)
            result = self.process_images(img_list)
            return self.convert_numpy(result)
        except Exception as e:
            raise RuntimeError(f"Failed to process images: {e}")
