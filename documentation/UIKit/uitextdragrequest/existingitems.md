# existingItems

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The array of drag items present in a drag session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var existingItems: [UIDragItem] { get }
```

```objc
@property (nonatomic, readonly) NSArray<UIDragItem *> * existingItems;
```

## See Also

### Getting the drag items
- [var suggestedItems: [UIDragItem]](./suggesteditems.md)
  An array of drag items that the system provides when the text drag delegate doesn’t provide custom drag items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdragrequest/existingitems)*