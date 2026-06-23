# addExcludedPoint(_:)

**Framework**: Vision  
**Kind**: method

Refines the mask with a point that is excluded from the desired segmentation. Throws an error if the total number of added points exceeded the limitation. (13 points when seedPoint or seedScribbleBuffer were used or 11 points when seedBox was used)

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func addExcludedPoint(_ point: NormalizedPoint) throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generateiterativesegmentationrequest/addexcludedpoint(_:))*