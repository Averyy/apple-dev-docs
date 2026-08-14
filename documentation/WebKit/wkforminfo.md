# WKFormInfo

**Framework**: WebKit  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
class WKFormInfo
```

#### Overview

A WKFormInfo object contains information about an in-progress form submission happening in a WKWebView

An instance of this class is a transient, data-only object; it does not uniquely identify a form across multiple delegate method calls.

## Topics

### Instance Properties
- [var formValues: [String : String]](wkforminfo/formvalues.md)
- [var httpMethod: String](wkforminfo/httpmethod.md)
- [var sourceFrame: WKFrameInfo](wkforminfo/sourceframe.md)
- [var submissionURL: URL](wkforminfo/submissionurl.md)
- [var targetFrame: WKFrameInfo](wkforminfo/targetframe.md)

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
- [class WKNavigation](wknavigation.md)
  An object that tracks the loading progress of a webpage.
- [class WKNavigationAction](wknavigationaction.md)
  An object that contains information about an action that causes navigation to occur.
- [class WKNavigationResponse](wknavigationresponse.md)
  An object that contains the response to a navigation request, and which you use to make navigation-related policy decisions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkforminfo)*