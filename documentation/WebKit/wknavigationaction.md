# WKNavigationAction

**Framework**: WebKit  
**Kind**: class

An object that contains information about an action that causes navigation to occur.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKNavigationAction
```

#### Overview

Use a [`WKNavigationAction`](wknavigationaction.md) object to make policy decisions about whether to allow navigation within your app’s web view. You don’t create [`WKNavigationAction`](wknavigationaction.md) objects directly. Instead, the web view creates them and delivers them to the appropriate delegate objects. Use the methods of your delegate to analyze the action and determine whether to allow the resulting navigation to occur.

## Topics

### Getting the navigation type
- [var navigationType: WKNavigationType](wknavigationaction/navigationtype.md)
  The type of action that triggered the navigation.
- [enum WKNavigationType](wknavigationtype.md)
  The type of action that triggered the navigation.
### Inspecting navigation information
- [var request: URLRequest](wknavigationaction/request.md)
  The URL request object associated with the navigation action.
- [var sourceFrame: WKFrameInfo](wknavigationaction/sourceframe.md)
  The frame that requested the navigation.
- [var targetFrame: WKFrameInfo?](wknavigationaction/targetframe.md)
  The frame in which to display the new content.
- [var shouldPerformDownload: Bool](wknavigationaction/shouldperformdownload.md)
  A Boolean value that indicates whether the web content provided an attribute that indicates a download.
### Inspecting user actions
- [var buttonNumber: UIEvent.ButtonMask](wknavigationaction/buttonnumber.md)
  The number of the mouse button that caused the navigation request.
- [var modifierFlags: UIKeyModifierFlags](wknavigationaction/modifierflags.md)
  The modifier keys that were pressed at the time of the navigation request.

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
- [class WKNavigationResponse](wknavigationresponse.md)
  An object that contains the response to a navigation request, and which you use to make navigation-related policy decisions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationaction)*