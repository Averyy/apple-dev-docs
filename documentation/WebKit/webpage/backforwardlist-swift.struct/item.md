# WebPage.BackForwardList.Item

**Framework**: WebKit  
**Kind**: struct

A representation of a resource that a webpage previously visited.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
struct Item
```

#### Overview

Two items with equal titles, urls, and initial urls may not necessarily be equal to one another.

## Topics

### Instance Properties
- [let id: WebPage.BackForwardList.Item.ID](webpage/backforwardlist-swift.struct/item/id.md)
  The unique identifier for the item.
- [let initialURL: URL](webpage/backforwardlist-swift.struct/item/initialurl.md)
  The source URL that originally asked to load the resource
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/backforwardlist-swift.struct/item)*