# WKNavigation

**Framework**: WebKit  
**Kind**: class

An object that tracks the loading progress of a webpage.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKNavigation
```

#### Overview

A [`WKNavigation`](wknavigation.md) object uniquely identifies a load request for a webpage. When you ask a web view to load content or navigate to a page, the web view returns a [`WKNavigation`](wknavigation.md) object that identifies your request. As the load operation progresses, the web view reports progress of that operation to various methods of its navigation delegate, passing them the matching [`WKNavigation`](wknavigation.md) object.

## Topics

### Getting the Content Mode
- [var effectiveContentMode: WKWebpagePreferences.ContentMode](wknavigation/effectivecontentmode.md)
  The content mode WebKit uses to load the webpage.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)

## See Also

- [protocol WKNavigationDelegate](wknavigationdelegate.md)
  Methods for accepting or rejecting navigation changes, and for tracking the progress of navigation requests.
- [class WKBackForwardList](wkbackforwardlist.md)
  An object that manages the list of previously loaded webpages, which the web view uses for forward and backward navigation.
- [class WKBackForwardListItem](wkbackforwardlistitem.md)
  A representation of a webpage that the web view previously visited.
- [class WKNavigationAction](wknavigationaction.md)
  An object that contains information about an action that causes navigation to occur.
- [class WKNavigationResponse](wknavigationresponse.md)
  An object that contains the response to a navigation request, and which you use to make navigation-related policy decisions.
- [class WKFormInfo](wkforminfo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigation)*