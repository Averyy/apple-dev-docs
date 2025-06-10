# WebPage.NavigationAction

**Framework**: WebKit  
**Kind**: struct

An object that contains information about an action that causes navigation to occur.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
struct NavigationAction
```

#### Overview

A `NavigationAction` value is intended to be used to make policy decisions about whether to allow navigation within a web page via a `NavigationDeciding`.

## Topics

### Instance Properties
- [var buttonNumber: Int](webpage/navigationaction/buttonnumber-29qsu.md)
  The number of the mouse button that caused the navigation request.
- [var buttonNumber: UIEvent.ButtonMask](webpage/navigationaction/buttonnumber-4sg9k.md)
  The number of the mouse button that caused the navigation request.
- [var modifierFlags: EventModifiers](webpage/navigationaction/modifierflags.md)
  The modifier keys that were pressed at the time of the navigation request.
- [var navigationType: WKNavigationType](webpage/navigationaction/navigationtype.md)
  The type of action that triggered the navigation.
- [var request: URLRequest](webpage/navigationaction/request.md)
  The URL request object associated with the navigation action.
- [var shouldPerformDownload: Bool](webpage/navigationaction/shouldperformdownload.md)
  Indicates whether the web content provided an attribute that indicates a download.
- [var source: WebPage.FrameInfo](webpage/navigationaction/source.md)
  The frame that requested the navigation.
- [var target: WebPage.FrameInfo?](webpage/navigationaction/target.md)
  The frame in which to display the new content.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol NavigationDeciding](webpage/navigationdeciding.md)
  Allows providing custom behavior to handle navigation changes and to coordinate these changes for the web page’s main page.
- [WebPage.NavigationResponse](webpage/navigationresponse.md)
  An object that contains the response to a navigation request, and which you use to make navigation-related policy decisions.
- [WebPage.NavigationPreferences](webpage/navigationpreferences.md)
  A type that specifies the behaviors to use when loading and rendering page content.
- [WebPage.FrameInfo](webpage/frameinfo.md)
  A type that contains information about a frame on a webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationaction)*