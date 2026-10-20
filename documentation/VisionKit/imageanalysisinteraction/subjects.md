# subjects

**Framework**: VisionKit  
**Kind**: property  
**Role**: Instance Property

The set of all subjects the framework identifies in an image.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
final var subjects: Set<ImageAnalysisInteraction.Subject> { get async }
```

## See Also

### Accessing image subjects
- [ImageAnalysisInteraction.Subject](./subject.md)
  An area of interest in an image that the framework identifies as a primary focal point.
- [func image(for: Set<ImageAnalysisInteraction.Subject>) async throws -> UIImage](./image%28for%29.md)
  Provides an image asynchronously that contains the given subjects with the background removed.
- [func subject(at: CGPoint) async -> ImageAnalysisInteraction.Subject?](./subject%28at%29.md)
  Returns the subject at the given point within the interaction’s image, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/subjects)*