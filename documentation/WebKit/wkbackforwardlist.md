# WKBackForwardList

**Framework**: WebKit  
**Kind**: class

An object that manages the list of previously loaded webpages, which the web view uses for forward and backward navigation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKBackForwardList
```

#### Overview

Use a [`WKBackForwardList`](wkbackforwardlist.md) object to retrieve a web view’s previously loaded pages. Typically, you don’t create [`WKBackForwardList`](wkbackforwardlist.md) objects directly. Each web view creates one automatically and uses it to store the history of all loaded pages. Fetch this object from your web view’s [`backForwardList`](wkwebview/backforwardlist.md) property and use its contents to facilitate programmatic navigation.

## Topics

### Getting the Most Recent Items
- [var backItem: WKBackForwardListItem?](wkbackforwardlist/backitem.md)
  The item immediately preceding the current item, if any.
- [var currentItem: WKBackForwardListItem?](wkbackforwardlist/currentitem.md)
  The current item.
- [var forwardItem: WKBackForwardListItem?](wkbackforwardlist/forwarditem.md)
  The item immediately following the current item, if any.
### Getting Specific Items in the List
- [func item(at: Int) -> WKBackForwardListItem?](wkbackforwardlist/item(at:).md)
  Returns the item at the relative offset from the current item.
### Getting Sublists
- [var backList: [WKBackForwardListItem]](wkbackforwardlist/backlist.md)
  The array of items that precede the current item.
- [var forwardList: [WKBackForwardListItem]](wkbackforwardlist/forwardlist.md)
  The array of items that follow the current item.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol WKNavigationDelegate](wknavigationdelegate.md)
  Methods for accepting or rejecting navigation changes, and for tracking the progress of navigation requests.
- [class WKBackForwardListItem](wkbackforwardlistitem.md)
  A representation of a webpage that the web view previously visited.
- [class WKNavigation](wknavigation.md)
  An object that tracks the loading progress of a webpage.
- [class WKNavigationAction](wknavigationaction.md)
  An object that contains information about an action that causes navigation to occur.
- [class WKNavigationResponse](wknavigationresponse.md)
  An object that contains the response to a navigation request, and which you use to make navigation-related policy decisions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkbackforwardlist)*