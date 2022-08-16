import subprocess

# --optimization space / time
def compile_assets(type):
    command = f"""
    /Applications/Xcode.app/Contents/Developer/usr/bin/actool \
    --output-format human-readable-text \
    --notices \
    --warnings \
    --compress-pngs \
    --enable-on-demand-resources NO \
    --filter-for-device-model iPhone14,2 \
    --filter-for-device-os-version 15.5 \
    --development-region en \
    --target-device iphone \
    --target-device ipad \
    --minimum-deployment-target 15.5 \
    --platform iphonesimulator \
    --compile {type}/ \
    {type}/Assets.xcassets
    """
    output = subprocess.getoutput(command)
    return output


if __name__ == "__main__":
    compile_assets("SVG")
    compile_assets("PDF")
    compile_assets("PNG")