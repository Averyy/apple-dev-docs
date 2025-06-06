# suggestedItems

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

An array of drag items that the system provides when the text drag delegate doesn’t provide custom drag items.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var suggestedItems: [UIDragItem] { get }
```

#### Discussion

The [`suggestedItems`](uitextdragrequest/suggesteditems.md) property is always an empty array if the text drag delegate doesn’t implement the [`textDraggableView(_:itemsForDrag:)`](uitextdragdelegate/textdraggableview(_:itemsfordrag:).md) method.

## See Also

- [var existingItems: [UIDragItem]](uitextdragrequest/existingitems.md)
  The array of drag items present in a drag session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdragrequest/suggesteditems)*