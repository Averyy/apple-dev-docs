# mainFrameNavigation

**Framework**: WebKit  
**Kind**: property

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var mainFrameNavigation: WKNavigation? { get }
```

#### Discussion

The most recent main frame navigation that took place that encompasses this navigation action.

If this WKNavigationAction represents a request to open a new WKWebView or it represents a frame load that is not in the main frame of an existing WKWebView, then mainFrameNavigation will be nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationaction/mainframenavigation)*