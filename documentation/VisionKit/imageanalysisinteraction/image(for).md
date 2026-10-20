# image(for:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

Provides an image asynchronously that contains the given subjects with the background removed.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
final func image(for subjects: Set<ImageAnalysisInteraction.Subject>) async throws -> UIImage
```

#### Discussion

If one or more subjects fail to produce an image, the method throws [`ImageAnalysisInteraction.SubjectUnavailable.imageUnavailable`](./subjectunavailable/imageunavailable.md).

## Parameters

- `subjects`: An array of subjects to include in the image.

## See Also

### Accessing image subjects
- [var subjects: Set<ImageAnalysisInteraction.Subject>](./subjects.md)
  The set of all subjects the framework identifies in an image.
- [ImageAnalysisInteraction.Subject](./subject.md)
  An area of interest in an image that the framework identifies as a primary focal point.
- [func subject(at: CGPoint) async -> ImageAnalysisInteraction.Subject?](./subject%28at%29.md)
  Returns the subject at the given point within the interaction’s image, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/image(for:))*