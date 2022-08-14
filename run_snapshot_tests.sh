xcodebuild \
  -project $1/$1.xcodeproj \
  -scheme $1Tests \
  -sdk iphonesimulator \
  -destination 'platform=iOS Simulator,name=iPhone 13 Pro,OS=15.5' \
  test