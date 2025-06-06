# subject(at:)

**Framework**: Visionkit  
**Kind**: method

Returns the subject at the given point within the overlay view’s image, if one exists.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
final func subject(at point: CGPoint) async -> ImageAnalysisOverlayView.Subject?
```

#### Return Value

The subject that resides at `point`; or, `nil`, if no subject resides at `point`.

#### Discussion

This method works for interaction types that include [`imageSubject`](imageanalysisoverlayview/interactiontypes/imagesubject.md).

The following code retrieves a subject image given a screen point, for instance, where a person clicks:

```swift
let configuration = ImageAnalyzer.Configuration()
...
overlayView.preferredInteractionTypes = [.imageSubject]
...
let viewPoint = /* A point in view coordinates */
if let subjectObject = try await overlayView.subject(at: viewPoint) {
    if let image = subjectObject.image {
        // Do something with the subject image.
    }
}
```

## Parameters

- `point`: A point in view coordinates at which to select a subject.

## See Also

- [var subjects: Set<ImageAnalysisOverlayView.Subject>](imageanalysisoverlayview/subjects.md)
  The set of all subjects the framework identifies in an image.
- [ImageAnalysisOverlayView.Subject](imageanalysisoverlayview/subject.md)
  An area of interest in an image that the framework identifies as a primary focal point.
- [func image(for: Set<ImageAnalysisOverlayView.Subject>) async throws -> NSImage](imageanalysisoverlayview/image(for:).md)
  Provides an image asynchronously that contains the given subjects with the background removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/subject(at:))*