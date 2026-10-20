# subjects

**Framework**: VisionKit  
**Kind**: property  
**Role**: Instance Property

The set of all subjects the framework identifies in an image.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
final var subjects: Set<ImageAnalysisOverlayView.Subject> { get async }
```

## See Also

### Accessing image subjects
- [ImageAnalysisOverlayView.Subject](./subject.md)
  An area of interest in an image that the framework identifies as a primary focal point.
- [func image(for: Set<ImageAnalysisOverlayView.Subject>) async throws -> NSImage](./image%28for%29.md)
  Provides an image asynchronously that contains the given subjects with the background removed.
- [func subject(at: CGPoint) async -> ImageAnalysisOverlayView.Subject?](./subject%28at%29.md)
  Returns the subject at the given point within the overlay view’s image, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/subjects)*