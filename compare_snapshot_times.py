from email import iterators
import subprocess
import matplotlib.pyplot as plt
from multiprocessing import Pool
import re
import json
from datetime import datetime

def snapshot(type):
    command = f"""
    xcodebuild \
    -project {type}/{type}.xcodeproj \
    -scheme {type}Tests \
    -sdk iphonesimulator \
    -destination 'platform=iOS Simulator,name=iPhone 13 Pro,OS=15.5' \
    test
    """
    output = subprocess.getoutput(command)
    return output

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

number_of_iterations = 5

svg_snapshot_times = []
pdf_snapshot_times = []
png_snapshot_times = []

if __name__ == "__main__":

    for _ in range(number_of_iterations):
        svg_snapshot_times.append(snapshot_svg())
        pdf_snapshot_times.append(snapshot_pdf())
        png_snapshot_times.append(snapshot_png())

    print("svg", svg_snapshot_times)
    print("pdf", pdf_snapshot_times)
    print("png", png_snapshot_times)

    x = ["SVG", "PDF", "PNG"]
    snapshot_times = [
        sum(svg_snapshot_times) / len(svg_snapshot_times),
        sum(pdf_snapshot_times) / len(pdf_snapshot_times), 
        sum(png_snapshot_times) / len(png_snapshot_times)
    ]

    x_pos = [i for i, _ in enumerate(x)]

    plt.bar(x_pos, snapshot_times, width=0.35, color='green')
    plt.ylabel("Time in seconds")
    plt.title(f"Average snapshot time ({number_of_iterations} iterations)")

    plt.xticks(x_pos, x)

    plt.show()

