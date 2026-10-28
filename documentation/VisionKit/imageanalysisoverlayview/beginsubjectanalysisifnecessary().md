# beginSubjectAnalysisIfNecessary()

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

Begins subject analysis on the overlay view’s image.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
final func beginSubjectAnalysisIfNecessary()
```

## Discussion

Subject analysis begins automatically without calling this method moments after the overlay view’s image displays onscreen. The framework ignores calls to this method if subject analysis is already in progress or complete.

> **Note**: For subject analysis to begin, [`preferredInteractionTypes`](./preferredinteractiontypes.md) needs to contain a subject-related option, such as [`automatic`](./interactiontypes/automatic.md), [`imageSubject`](./interactiontypes/imagesubject.md), or [`visualLookUp`](./interactiontypes/visuallookup.md).

## See Also

### Managing image subjects
- [var highlightedSubjects: Set<ImageAnalysisOverlayView.Subject>](./highlightedsubjects.md)
  All highlighted subjects in the overlay view’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/beginsubjectanalysisifnecessary())*