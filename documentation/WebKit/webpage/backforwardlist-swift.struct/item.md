# WebPage.BackForwardList.Item

**Framework**: WebKit  
**Kind**: struct

A representation of a resource that a webpage previously visited.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Item
```

#### Overview

Two items with equal titles, urls, and initial urls may not necessarily be equal to one another.

## Topics

### Structures
- [WebPage.BackForwardList.Item.ID](webpage/backforwardlist-swift.struct/item/id-swift.struct.md)
  An opaque type representing the identifier for an item.
### Instance Properties
- [let id: WebPage.BackForwardList.Item.ID](webpage/backforwardlist-swift.struct/item/id-swift.property.md)
  The unique identifier for the item.
- [let initialURL: URL](webpage/backforwardlist-swift.struct/item/initialurl.md)
  The source URL that originally asked to load the resource.
- [let title: String?](webpage/backforwardlist-swift.struct/item/title.md)
  The title of the page this item represents.
- [let url: URL](webpage/backforwardlist-swift.struct/item/url.md)
  The url of the page this item represents, after having resolved all redirects.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [WebPage.BackForwardList](webpage/backforwardlist-swift.struct.md)
  An observable representation of a webpage’s previously loaded resources.
- [WebPage.NavigationEvent](webpage/navigationevent.md)
  A particular state that occurs during the progression of a navigation.
- [WebPage.BackForwardList.Item.ID](webpage/backforwardlist-swift.struct/item/id-swift.struct.md)
  An opaque type representing the identifier for an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/backforwardlist-swift.struct/item)*