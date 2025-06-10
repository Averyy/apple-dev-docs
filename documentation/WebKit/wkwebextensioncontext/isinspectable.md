# isInspectable

**Framework**: WebKit  
**Kind**: property

Determines whether Web Inspector can inspect the [`WKWebView`](wkwebview.md) instances for this context.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var isInspectable: Bool { get set }
```

#### Discussion

A context can control multiple [`WKWebView`](wkwebview.md) instances, from the background content, to the popover.

You should set this to `YES` when needed for debugging purposes. The default value is `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/isinspectable)*