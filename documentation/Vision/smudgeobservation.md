# SmudgeObservation

**Framework**: Vision  
**Kind**: struct

An observation that provides an overall score of the presence of a smudge in an image or video frame capture.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct SmudgeObservation
```

## Topics

### Inspecting an observation
- [let confidence: Float](smudgeobservation/confidence.md)
  The level of confidence in the observation’s accuracy of smudge detection on a lens.
- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
### Instance Properties
- [var description: String](smudgeobservation/description.md)
  A textual representation of this instance.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VisionObservation](visionobservation.md)

## See Also

- [Classifying images for categorization and search](classifying-images-for-categorization-and-search.md)
  Analyze and label images using a Vision classification request.
- [struct ClassifyImageRequest](classifyimagerequest.md)
  A request to classify an image.
- [protocol ImageProcessingRequest](imageprocessingrequest.md)
  A type for image-analysis requests that focus on a specific part of an image.
- [class ImageRequestHandler](imagerequesthandler.md)
  An object that processes one or more image-analysis requests pertaining to a single image.
- [protocol VisionRequest](visionrequest.md)
  A type for image-analysis requests.
- [protocol VisionObservation](visionobservation.md)
  A type for objects produced by image-analysis requests.
- [struct DetectLensSmudgeRequest](detectlenssmudgerequest.md)
  A request that detects a smudge on a lens from an image or video frame capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/smudgeobservation)*