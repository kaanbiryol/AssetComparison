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
--compile $1/ \
$1/Assets.xcassets


# Original command
# /Applications/Xcode.app/Contents/Developer/usr/bin/actool \
# --output-format human-readable-text \
# --notices \
# --warnings \
# --export-dependency-info /Users/kaanbiryol/Library/Developer/Xcode/DerivedData/Untitled-dfnlvpxbetjskrdgyibrwllfmrpz/Build/Intermediates.noindex/SVG.build/Debug-iphonesimulator/SVG.build/assetcatalog_dependencies \
# --output-partial-info-plist /Users/kaanbiryol/Library/Developer/Xcode/DerivedData/Untitled-dfnlvpxbetjskrdgyibrwllfmrpz/Build/Intermediates.noindex/SVG.build/Debug-iphonesimulator/SVG.build/assetcatalog_generated_info.plist \
# --compress-pngs \
# --enable-on-demand-resources NO \
# --filter-for-device-model iPhone14,2 \
# --filter-for-device-os-version 15.5 \
# --development-region en \
# --target-device iphone \
# --target-device ipad \
# --minimum-deployment-target 15.5 \
# --platform iphonesimulator \
# --compile . \
# Assets.xcassets
