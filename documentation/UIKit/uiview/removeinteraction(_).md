# removeInteraction(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Removes an interaction from the view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func removeInteraction(_ interaction: any UIInteraction)
```

```objc
- (void) removeInteraction:(id<UIInteraction>) interaction;
```

## Parameters

- `interaction`: The interaction object to remove from the view.

## See Also

### Adding and removing interactions
- [func addInteraction(any UIInteraction)](./addinteraction%28_%29.md)
  Adds an interaction to the view.
- [var interactions: [any UIInteraction]](./interactions.md)
  The array of interactions for the view.
- [protocol UIInteraction](../uiinteraction.md)
  The protocol that an interaction implements to access the view that owns it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/removeinteraction(_:))*