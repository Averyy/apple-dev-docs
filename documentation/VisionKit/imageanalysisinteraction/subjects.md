# subjects

**Framework**: Visionkit  
**Kind**: property

The set of all subjects the framework identifies in an image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
final var subjects: Set<ImageAnalysisInteraction.Subject> { get async }
```

## See Also

- [ImageAnalysisInteraction.Subject](imageanalysisinteraction/subject.md)
  An area of interest in an image that the framework identifies as a primary focal point.
- [func image(for: Set<ImageAnalysisInteraction.Subject>) async throws -> UIImage](imageanalysisinteraction/image(for:).md)
  Provides an image asynchronously that contains the given subjects with the background removed.
- [func subject(at: CGPoint) async -> ImageAnalysisInteraction.Subject?](imageanalysisinteraction/subject(at:).md)
  Returns the subject at the given point within the interaction’s image, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/subjects)*