# init(detectedObject:_:frameAnalysisSpacing:)

**Framework**: Vision  
**Kind**: init

Creates an object tracking request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
init(detectedObject: any BoundingBoxProviding & VisionObservation, _ revision: TrackObjectRequest.Revision? = nil, frameAnalysisSpacing: CMTime? = nil)
```

## See Also

- [protocol BoundingBoxProviding](boundingboxproviding.md)
  A protocol for objects that have a bounding box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/trackobjectrequest/init(detectedobject:_:frameanalysisspacing:))*