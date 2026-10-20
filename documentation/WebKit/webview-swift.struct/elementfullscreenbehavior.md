# WebView.ElementFullscreenBehavior

**Framework**: WebKit  
**Kind**: struct  
**Role**: Structure

The behavior that determines whether a web view can display content full screen.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct ElementFullscreenBehavior
```

## Topics

### Type Properties
- [static let automatic: WebView.ElementFullscreenBehavior](./elementfullscreenbehavior/automatic.md)
  The automatic behavior.
- [static let disabled: WebView.ElementFullscreenBehavior](./elementfullscreenbehavior/disabled.md)
  Element full screen is disabled.
- [static let enabled: WebView.ElementFullscreenBehavior](./elementfullscreenbehavior/enabled.md)
  Element full screen is enabled.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Modifying web interactions
- [WebView.BackForwardNavigationGesturesBehavior](./backforwardnavigationgesturesbehavior.md)
  A type that defines the behavior of how horizontal swipe gestures trigger backward and forward page navigation.
- [WebView.LinkPreviewBehavior](./linkpreviewbehavior.md)
  A type specifying the behavior for the presentation of link previews when pressing a link.
- [WebView.ActivatedElementInfo](./activatedelementinfo.md)
  Contains information about an element the user activated in a webpage, which may be used to configure a context menu for that element.
- [WebView.MagnificationGesturesBehavior](./magnificationgesturesbehavior.md)
  The options for controlling the behavior for how magnification gestures interact with web views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.struct/elementfullscreenbehavior)*