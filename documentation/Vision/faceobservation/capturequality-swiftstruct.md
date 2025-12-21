# FaceObservation.CaptureQuality

**Framework**: Vision  
**Kind**: struct

An indicator of the quality of a face capture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct CaptureQuality
```

## Topics

### Getting the score
- [let score: Float](faceobservation/capturequality-swift.struct/score.md)
  A value that indicates the quality of the face capture.
### Accessing the originating descriptor
- [let originatingRequestDescriptor: RequestDescriptor?](faceobservation/capturequality-swift.struct/originatingrequestdescriptor.md)
  The descriptor of the request that produced the capture quality.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var captureQuality: FaceObservation.CaptureQuality?](faceobservation/capturequality-swift.property.md)
  The quality of the face capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/faceobservation/capturequality-swift.struct)*