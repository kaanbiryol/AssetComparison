# Importing packages
import subprocess
import matplotlib.pyplot as plt
from multiprocessing import Pool
import re
import json
from datetime import datetime

def snapshot(type):
    return subprocess.getoutput("./run_snapshot_tests.sh " + type)

def snapshot_svg():
    return calculate_time_elapsed(snapshot("SVG"))

def snapshot_png():
    return calculate_time_elapsed(snapshot("PNG"))

def snapshot_pdf():
    return calculate_time_elapsed(snapshot("PDF"))

def calculate_time_elapsed(terminalOutput):
    xcResultPathRegex = re.search(r".+?(?=.xcresult)", terminalOutput)
    xcResultPath = xcResultPathRegex.group() + ".xcresult"
    xcResultJSON = subprocess.getoutput("xcrun xcresulttool get --path" + xcResultPath + " --format json")
    data = json.loads(xcResultJSON)
    startDateString = data["actions"]["_values"][0]["startedTime"]["_value"]
    endDateString = data["actions"]["_values"][0]["endedTime"]["_value"]
    startDate = datetime.strptime(startDateString, "%Y-%m-%dT%H:%M:%S.%f%z")
    endDate = datetime.strptime(endDateString, "%Y-%m-%dT%H:%M:%S.%f%z")
    return (endDate-startDate).total_seconds()

def fmap(f):
    return f()

number_of_iterations = 2

svg_snapshot_times = []
pdf_snapshot_times = []
png_snapshot_times = []

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
    svgList = [snapshot_svg] * number_of_iterations
    svgResult = svgPool.map(fmap, svgList)
    svg_build_times = svgResult

    pdfPool = Pool(number_of_iterations)
    pdfList = [snapshot_pdf] * number_of_iterations
    pdfResult = pdfPool.map(fmap, pdfList)
    pdf_build_times = pdfResult

    pngPool = Pool(number_of_iterations)
    pngList = [snapshot_png] * number_of_iterations
    pngResult = pngPool.map(fmap, pngList)
    png_build_times = pngResult

    print("svg", svg_build_times)
    print("pdf", pdf_build_times)
    print("png", png_build_times)

    iteration = range(1, number_of_iterations + 1)
    plt.suptitle('Snapshot times', fontsize=18)
    plt.xlabel('Iteration', fontsize=18)
    plt.ylabel('Build time', fontsize=18)

    plt.xticks(iteration)
    plt.plot(iteration, pdf_build_times, 'r', label='PDF')
    plt.plot(iteration, svg_build_times, 'g', label='SVG')
    plt.plot(iteration, png_build_times, 'b', label='PNG')

    plt.legend()
    plt.show()

