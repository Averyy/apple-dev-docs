# WKBackForwardListItem

**Framework**: WebKit  
**Kind**: class

A representation of a webpage that the web view previously visited.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKBackForwardListItem
```

#### Overview

Use a [`WKBackForwardListItem`](wkbackforwardlistitem.md) object to get information about previously visited webpages. This object identifies the page’s title and URL. It also identifes the URL that requested the webpage.

You don’t create [`WKBackForwardListItem`](wkbackforwardlistitem.md) objects directly. Instead, a [`WKBackForwardList`](wkbackforwardlist.md) object creates them in conjunction with its associated web view when the web view loads new pages.

## Topics

### Getting the Page-Specific Information
- [var title: String?](wkbackforwardlistitem/title.md)
  The title of the webpage this item represents.
- [var url: URL](wkbackforwardlistitem/url.md)
  The URL of the webpage this item represents.
### Getting the Requesting Page
- [var initialURL: URL](wkbackforwardlistitem/initialurl.md)
  The source URL that originally asked the web view to load this page.

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
- [class WKBackForwardList](wkbackforwardlist.md)
  An object that manages the list of previously loaded webpages, which the web view uses for forward and backward navigation.
- [class WKNavigation](wknavigation.md)
  An object that tracks the loading progress of a webpage.
- [class WKNavigationAction](wknavigationaction.md)
  An object that contains information about an action that causes navigation to occur.
- [class WKNavigationResponse](wknavigationresponse.md)
  An object that contains the response to a navigation request, and which you use to make navigation-related policy decisions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkbackforwardlistitem)*