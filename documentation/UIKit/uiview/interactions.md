# interactions

**Framework**: UIKit  
**Kind**: property

The array of interactions for the view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var interactions: [any UIInteraction] { get set }
```

## Mentions

- [Making a view into a drop destination](making-a-view-into-a-drop-destination.md)
- [Making a view into a drag source](making-a-view-into-a-drag-source.md)

## See Also

- [func addInteraction(any UIInteraction)](uiview/addinteraction(_:).md)
  Adds an interaction to the view.
- [func removeInteraction(any UIInteraction)](uiview/removeinteraction(_:).md)
  Removes an interaction from the view.
- [protocol UIInteraction](uiinteraction.md)
  The protocol that an interaction implements to access the view that owns it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/interactions)*