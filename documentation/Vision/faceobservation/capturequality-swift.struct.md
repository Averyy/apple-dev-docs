# FaceObservation.CaptureQuality

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

An indicator of the quality of a face capture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
struct CaptureQuality
```

## Topics

### Getting the score
- [let score: Float](./capturequality-swift.struct/score.md)
  A value that indicates the quality of the face capture.
### Accessing the originating descriptor
- [let originatingRequestDescriptor: RequestDescriptor?](./capturequality-swift.struct/originatingrequestdescriptor.md)
  The descriptor of the request that produced the capture quality.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the capture quality
- [var captureQuality: FaceObservation.CaptureQuality?](./capturequality-swift.property.md)
  The quality of the face capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/faceobservation/capturequality-swift.struct)*