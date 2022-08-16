import subprocess
import matplotlib.pyplot as plt
from multiprocessing import Pool
import numpy as np
import json
from pathlib import Path
import sys

def calculate_sizes(jsonString):
    jsonData = json.loads(jsonString)
    # Not interested in Appearances{} therefore we skip first element
    image_sizes = []
    vector_sizes = []
    total_image_size = 0
    total_vector_size = 0
    for item in jsonData[1:]:    
        if item["AssetType"] == "Image":
            sizeOnDisk = item["SizeOnDisk"]
            total_image_size += sizeOnDisk
            image_sizes.append(sizeOnDisk)
        elif item["AssetType"] == "Vector":
            sizeOnDisk = item["SizeOnDisk"]
            total_vector_size += sizeOnDisk
            vector_sizes.append(sizeOnDisk)

    return (total_image_size / len(image_sizes), total_vector_size / len(vector_sizes) if (len(vector_sizes) > 0) else 0, total_image_size, total_vector_size)

def get_asset_info(path):
    command = f"""
    assetutil -I {path}/Assets.car
    """
    output = subprocess.getoutput(command)
    return output

def measure_svg():
    return calculate_sizes(get_asset_info("SVG"))

def measure_png():
    return calculate_sizes(get_asset_info("PNG"))

def measure_pdf():
    return calculate_sizes(get_asset_info("PDF"))

def plot(
    svgResults_image,
    pdfResults_image,
    pngResults_image,
    svgResults_vector,
    pdfResults_vector,
    pngResults_vector,
    yLabel,
    title):
    labels = ["SVG", "PDF", "PNG"]
    image = [svgResults_image, pdfResults_image, pngResults_image]
    vector = [svgResults_vector, pdfResults_vector, pngResults_vector]

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, image, width, label='Image', color="blue")
    rects2 = ax.bar(x + width/2, vector, width, label='Vector',color="green")

    ax.set_ylabel(yLabel)
    ax.set_title(title)
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()

if __name__ == "__main__":
    svgResults = measure_svg()
    pdfResults = measure_pdf()
    pngResults = measure_png()

    print("svg", svgResults)
    print("pdf", pdfResults)
    print("png", pngResults)

    if sys.argv[1] == "avg":
        plot(
        svgResults_image=svgResults[0],
        svgResults_vector=svgResults[1],
        pdfResults_image=pdfResults[0],
        pdfResults_vector=pdfResults[1],
        pngResults_image=pngResults[0],
        pngResults_vector=pngResults[1],
        title="Average size in disk",
        yLabel="Size in disk"
    )
    elif sys.argv[1] == "total":
        plot(
        svgResults_image=svgResults[2],
        svgResults_vector=svgResults[3],
        pdfResults_image=pdfResults[2],
        pdfResults_vector=pdfResults[3],
        pngResults_image=pngResults[2],
        pngResults_vector=pngResults[3],
        title="Total size in disk",
        yLabel="Size in disk"
    )