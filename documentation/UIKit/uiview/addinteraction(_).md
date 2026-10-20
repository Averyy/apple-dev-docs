# addInteraction(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds an interaction to the view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func addInteraction(_ interaction: any UIInteraction)
```

```objc
- (void) addInteraction:(id<UIInteraction>) interaction;
```

## Parameters

- `interaction`: The interaction object to add to the view.

## See Also

### Adding and removing interactions
- [func removeInteraction(any UIInteraction)](./removeinteraction%28_%29.md)
  Removes an interaction from the view.
- [var interactions: [any UIInteraction]](./interactions.md)
  The array of interactions for the view.
- [protocol UIInteraction](../uiinteraction.md)
  The protocol that an interaction implements to access the view that owns it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/addinteraction(_:))*