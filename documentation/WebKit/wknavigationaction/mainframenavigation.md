# mainFrameNavigation

**Framework**: WebKit  
**Kind**: property

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var mainFrameNavigation: WKNavigation? { get }
```

#### Discussion

The most recent main frame navigation that took place that encompasses this navigation action.

If this WKNavigationAction represents a request to open a new WKWebView or it represents a frame load that is not in the main frame of an existing WKWebView, then mainFrameNavigation will be nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationaction/mainframenavigation)*