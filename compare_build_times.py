# Importing packages
import time
import subprocess
import matplotlib.pyplot as plt
from multiprocessing import Pool

def measure(type):
    start_time = time.time()
    output = subprocess.getoutput("./compile_assets.sh " + type)
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

number_of_iterations = 4

svg_build_times = []
pdf_build_times = []
png_build_times = []

if __name__ == "__main__":
    ## we have 3 asset types to measure for now
    # pool = Pool(number_of_iterations * 3)
    # poolList = ([measure_svg] * number_of_iterations) + ([measure_pdf] * number_of_iterations) + ([measure_png] * number_of_iterations)
    # svgResult = pool.map(fmap, poolList)
    # splitResult = np.array_split(svgResult, 3)
    # svg_build_times = splitResult[0]
    # pdf_build_times = splitResult[1]
    # png_build_times = splitResult[2]

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

    iteration = range(1, number_of_iterations + 1)
    plt.suptitle('Build time for different asset types', fontsize=18)
    plt.xlabel('Iteration', fontsize=18)
    plt.ylabel('Build time', fontsize=18)

    plt.xticks(iteration)
    plt.plot(iteration, pdf_build_times, 'r', label='PDF')
    plt.plot(iteration, svg_build_times, 'g', label='SVG')
    plt.plot(iteration, png_build_times, 'b', label='PNG')

    plt.legend()
    plt.show()

