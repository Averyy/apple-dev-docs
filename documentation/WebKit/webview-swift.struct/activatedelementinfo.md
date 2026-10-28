# WebView.ActivatedElementInfo

**Framework**: WebKit  
**Kind**: struct  
**Role**: Structure

Contains information about an element the user activated in a webpage, which may be used to configure a context menu for that element.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct ActivatedElementInfo
```

## Overview

For links, the information contains the URL that is linked to.

## Topics

### Instance Properties
- [let linkURL: URL?](./activatedelementinfo/linkurl.md)
  The URL of the link that the user clicked.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Modifying web interactions
- [WebView.BackForwardNavigationGesturesBehavior](./backforwardnavigationgesturesbehavior.md)
  A type that defines the behavior of how horizontal swipe gestures trigger backward and forward page navigation.
- [WebView.LinkPreviewBehavior](./linkpreviewbehavior.md)
  A type specifying the behavior for the presentation of link previews when pressing a link.
- [WebView.ElementFullscreenBehavior](./elementfullscreenbehavior.md)
  The behavior that determines whether a web view can display content full screen.
- [WebView.MagnificationGesturesBehavior](./magnificationgesturesbehavior.md)
  The options for controlling the behavior for how magnification gestures interact with web views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.struct/activatedelementinfo)*