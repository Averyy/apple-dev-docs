# WKFormInfo

**Framework**: WebKit  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
class WKFormInfo
```

```objc
@interface WKFormInfo : NSObject
```

#### Overview

A WKFormInfo object contains information about an in-progress form submission happening in a WKWebView

An instance of this class is a transient, data-only object; it does not uniquely identify a form across multiple delegate method calls.

## Topics

### Instance Properties
- [var formValues: [String : String]](./wkforminfo/formvalues.md)
- [var httpMethod: String](./wkforminfo/httpmethod.md)
- [var sourceFrame: WKFrameInfo](./wkforminfo/sourceframe.md)
- [var submissionURL: URL](./wkforminfo/submissionurl.md)
- [var targetFrame: WKFrameInfo](./wkforminfo/targetframe.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Navigation
- [protocol WKNavigationDelegate](./wknavigationdelegate.md)
  Methods for accepting or rejecting navigation changes, and for tracking the progress of navigation requests.
- [class WKBackForwardList](./wkbackforwardlist.md)
  An object that manages the list of previously loaded webpages, which the web view uses for forward and backward navigation.
- [class WKBackForwardListItem](./wkbackforwardlistitem.md)
  A representation of a webpage that the web view previously visited.
- [class WKNavigation](./wknavigation.md)
  An object that tracks the loading progress of a webpage.
- [class WKNavigationAction](./wknavigationaction.md)
  An object that contains information about an action that causes navigation to occur.
- [class WKNavigationResponse](./wknavigationresponse.md)
  An object that contains the response to a navigation request, and which you use to make navigation-related policy decisions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkforminfo)*