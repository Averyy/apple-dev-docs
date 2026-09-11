# addIncludedPoint(_:)

**Framework**: Vision  
**Kind**: method

Refines the mask with a point that is part of the desired segmentation. Throws an error if the total number of added points exceeds the limit. (13 points when seedPoint or seedScribbleBuffer was used, or 11 points when seedBox was used)

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func addIncludedPoint(_ point: NormalizedPoint) throws
```

## See Also

- [func addExcludedPoint(NormalizedPoint) throws](generateiterativesegmentationrequest/addexcludedpoint(_:).md)
  Refines the mask with a point that is excluded from the desired segmentation. Throws an error if the total number of added points exceeds the limit. (13 points when seedPoint or seedScribbleBuffer was used, or 11 points when seedBox was used)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/generateiterativesegmentationrequest/addincludedpoint(_:))*