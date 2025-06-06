# subject(at:)

**Framework**: Visionkit  
**Kind**: method

Returns the subject at the given point within the interaction’s image, if one exists.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
final func subject(at point: CGPoint) async -> ImageAnalysisInteraction.Subject?
```

#### Return Value

The subject that resides at `point`; or, `nil`, if no subject resides at `point`.

#### Discussion

This method works for interaction types that include [`imageSubject`](imageanalysisinteraction/interactiontypes/imagesubject.md).

The following code retrieves a subject image given a screen point, for instance, where a person taps:

```swift
let configuration = ImageAnalyzer.Configuration()
...
interaction.preferredInteractionTypes = [.imageSubject]
...
let viewPoint = /* A point in view coordinates */
if let subjectObject = try await interaction.subject(at: viewPoint) {
    if let image = subjectObject.image {
        // Do something with the subject image.
    }
}
```

## Parameters

- `point`: A point in view coordinates at which to select a subject.

## See Also

- [var subjects: Set<ImageAnalysisInteraction.Subject>](imageanalysisinteraction/subjects.md)
  The set of all subjects the framework identifies in an image.
- [ImageAnalysisInteraction.Subject](imageanalysisinteraction/subject.md)
  An area of interest in an image that the framework identifies as a primary focal point.
- [func image(for: Set<ImageAnalysisInteraction.Subject>) async throws -> UIImage](imageanalysisinteraction/image(for:).md)
  Provides an image asynchronously that contains the given subjects with the background removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/subject(at:))*