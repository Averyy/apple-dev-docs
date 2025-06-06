# addInteraction(_:)

**Framework**: UIKit  
**Kind**: method

Adds an interaction to the view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addInteraction(_ interaction: any UIInteraction)
```

## Parameters

- `interaction`: The interaction object to add to the view.

## See Also

- [func removeInteraction(any UIInteraction)](uiview/removeinteraction(_:).md)
  Removes an interaction from the view.
- [var interactions: [any UIInteraction]](uiview/interactions.md)
  The array of interactions for the view.
- [protocol UIInteraction](uiinteraction.md)
  The protocol that an interaction implements to access the view that owns it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/addinteraction(_:))*