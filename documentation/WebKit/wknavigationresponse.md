# WKNavigationResponse

**Framework**: WebKit  
**Kind**: class

An object that contains the response to a navigation request, and which you use to make navigation-related policy decisions.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKNavigationResponse
```

#### Overview

Use a [`WKNavigationResponse`](wknavigationresponse.md) object to make policy decisions about whether to allow navigation within your app’s web view. You don’t create [`WKNavigationResponse`](wknavigationresponse.md) objects directly. Instead, the web view creates them and delivers them to the appropriate delegate objects. Use the methods of your delegate to analyze the response and determine whether to allow the resulting navigation to occur.

## Topics

### Getting the Response Details
- [var response: URLResponse](wknavigationresponse/response.md)
  The frame’s response.
### Getting Additional Response Information
- [var canShowMIMEType: Bool](wknavigationresponse/canshowmimetype.md)
  A Boolean value that indicates whether WebKit is capable of displaying the response’s MIME type natively.
- [var isForMainFrame: Bool](wknavigationresponse/isformainframe.md)
  A Boolean value that indicates whether the response targets the web view’s main frame.

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
- [class WKBackForwardListItem](wkbackforwardlistitem.md)
  A representation of a webpage that the web view previously visited.
- [class WKNavigation](wknavigation.md)
  An object that tracks the loading progress of a webpage.
- [class WKNavigationAction](wknavigationaction.md)
  An object that contains information about an action that causes navigation to occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationresponse)*