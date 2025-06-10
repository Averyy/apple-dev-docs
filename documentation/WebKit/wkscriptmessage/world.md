# world

**Framework**: WebKit  
**Kind**: property

The namespace in which the JavaScript code executes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var world: WKContentWorld { get }
```

#### Discussion

For more information about content worlds, see [`WKContentWorld`](wkcontentworld.md).

## See Also

- [var frameInfo: WKFrameInfo](wkscriptmessage/frameinfo.md)
  The frame that sent the message.
- [var webView: WKWebView?](wkscriptmessage/webview.md)
  The web view that sent the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkscriptmessage/world)*