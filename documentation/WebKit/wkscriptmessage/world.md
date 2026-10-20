# world

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The namespace in which the JavaScript code executes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var world: WKContentWorld { get }
```

```objc
@property (nonatomic, readonly) WKContentWorld * world;
```

#### Discussion

For more information about content worlds, see [`WKContentWorld`](../wkcontentworld.md).

## See Also

### Getting Message-Related Information
- [var frameInfo: WKFrameInfo](./frameinfo.md)
  The frame that sent the message.
- [var webView: WKWebView?](./webview.md)
  The web view that sent the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkscriptmessage/world)*