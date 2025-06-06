# init(boundingBox:revision:)

**Framework**: Vision  
**Kind**: init

Creates a face observation from its bounding box.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
init(boundingBox: NormalizedRect, revision: DetectFaceRectanglesRequest.Revision? = nil)
```

## Parameters

- `boundingBox`: The bounding box of the detected face.
- `revision`: The revision of the   that provided the bounding box.

## See Also

- [init(VNFaceObservation)](faceobservation/init(_:).md)
  Creates a face observation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/faceobservation/init(boundingbox:revision:))*