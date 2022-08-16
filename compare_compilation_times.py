from distutils.command.build import build
import time
from unittest import result
import matplotlib.pyplot as plt
from multiprocessing import Pool
import numpy as np
from compile_assets import *

def measure(type):
    start_time = time.time()
    output = compile_assets(type)
    end_time = time.time()
    time_elapsed = format(end_time - start_time, ".2f")
    return float(time_elapsed)

def measure_svg():
    return measure("SVG")

def measure_png():
    return measure("PNG")

def measure_pdf():
    return measure("PDF")

def fmap(f):
    return f()

number_of_iterations = 5

svg_build_times = []
pdf_build_times = []
png_build_times = []

if __name__ == "__main__":
    svgPool = Pool(number_of_iterations)
    svgList = [measure_svg] * number_of_iterations
    svgResult = svgPool.map(fmap, svgList)
    svg_build_times = svgResult

    pdfPool = Pool(number_of_iterations)
    pdfList = [measure_pdf] * number_of_iterations
    pdfResult = pdfPool.map(fmap, pdfList)
    pdf_build_times = pdfResult

    pngPool = Pool(number_of_iterations)
    pngList = [measure_png] * number_of_iterations
    pngResult = pngPool.map(fmap, pngList)
    png_build_times = pngResult

    print("svg", svg_build_times)
    print("pdf", pdf_build_times)
    print("png", png_build_times)

    x = ["SVG", "PDF", "PNG"]
    build_times = [
        sum(svg_build_times) / len(svg_build_times),
        sum(pdf_build_times) / len(pdf_build_times), 
        sum(png_build_times) / len(png_build_times)
    ]

    x_pos = [i for i, _ in enumerate(x)]

    plt.bar(x_pos, build_times, width=0.35, color='green')
    plt.ylabel("Time in seconds")
    plt.title(f"Average compilation time ({number_of_iterations} iterations)")

    plt.xticks(x_pos, x)

    plt.show()