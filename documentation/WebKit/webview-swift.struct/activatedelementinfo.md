# WebView.ActivatedElementInfo

**Framework**: WebKit  
**Kind**: struct

Contains information about an element the user activated in a webpage, which may be used to configure a context menu for that element.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct ActivatedElementInfo
```

#### Overview

For links, the information contains the URL that is linked to.

## Topics

### Instance Properties
- [let linkURL: URL?](webview-swift.struct/activatedelementinfo/linkurl.md)
  The URL of the link that the user clicked.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [WebView.BackForwardNavigationGesturesBehavior](webview-swift.struct/backforwardnavigationgesturesbehavior.md)
  A type that defines the behavior of how horizontal swipe gestures trigger backward and forward page navigation.
- [WebView.LinkPreviewBehavior](webview-swift.struct/linkpreviewbehavior.md)
  A type specifying the behavior for the presentation of link previews when pressing a link.
- [WebView.ElementFullscreenBehavior](webview-swift.struct/elementfullscreenbehavior.md)
  The behavior that determines whether a web view can display content full screen.
- [WebView.MagnificationGesturesBehavior](webview-swift.struct/magnificationgesturesbehavior.md)
  The options for controlling the behavior for how magnification gestures interact with web views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.struct/activatedelementinfo)*