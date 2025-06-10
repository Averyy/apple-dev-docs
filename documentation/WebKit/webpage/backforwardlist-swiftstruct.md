# WebPage.BackForwardList

**Framework**: WebKit  
**Kind**: struct

An observable representation of a webpage’s navigations.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
struct BackForwardList
```

#### Overview

This type can be used to facilitate navigating to prior or subsequent loaded resources and for observing when new entries get added or removed.

## Topics

### Structures
- [WebPage.BackForwardList.Item](webpage/backforwardlist-swift.struct/item.md)
  A representation of a resource that a webpage previously visited.
### Instance Properties
- [var backList: [WebPage.BackForwardList.Item]](webpage/backforwardlist-swift.struct/backlist.md)
  The array of items that precede the current item.
- [var currentItem: WebPage.BackForwardList.Item?](webpage/backforwardlist-swift.struct/currentitem.md)
  The current item.
- [var forwardList: [WebPage.BackForwardList.Item]](webpage/backforwardlist-swift.struct/forwardlist.md)
  The array of items that follow the current item.
### Subscripts
- [subscript(Int) -> WebPage.BackForwardList.Item?](webpage/backforwardlist-swift.struct/subscript(_:).md)
  Accesses the item at the relative offset from the current item.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [WebPage.NavigationID](webpage/navigationid.md)
  An opaque identifier which can be used to uniquely identify a load request for a web page.
- [WebPage.NavigationEvent](webpage/navigationevent.md)
  A particular state that occurs during the progression of a navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/backforwardlist-swift.struct)*