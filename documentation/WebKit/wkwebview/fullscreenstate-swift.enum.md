# WKWebView.FullscreenState

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum FullscreenState
```

```c
enum WKFullscreenState : NSInteger;
```

## Topics

### Constants
- [WKWebView.FullscreenState.enteringFullscreen](./fullscreenstate-swift.enum/enteringfullscreen.md)
- [WKWebView.FullscreenState.exitingFullscreen](./fullscreenstate-swift.enum/exitingfullscreen.md)
- [WKWebView.FullscreenState.inFullscreen](./fullscreenstate-swift.enum/infullscreen.md)
- [WKWebView.FullscreenState.notInFullscreen](./fullscreenstate-swift.enum/notinfullscreen.md)
### Initializers
- [init?(rawValue: Int)](./fullscreenstate-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Web view configuration
- [class WKWebViewConfiguration](../wkwebviewconfiguration.md)
  A collection of properties that you use to initialize a web view.
- [class WKWindowFeatures](../wkwindowfeatures.md)
  Display-related attributes that a webpage requests for its window.
- [class WKProcessPool](../wkprocesspool.md)
  An opaque token that you use to run multiple web views in a single process.
- [class WKPreferences](../wkpreferences.md)
  An object that encapsulates the standard behaviors to apply to websites.
- [class WKWebpagePreferences](../wkwebpagepreferences.md)
  An object that specifies the behaviors to use when loading and rendering page content.
- [WKWebpagePreferences.ContentMode](../wkwebpagepreferences/contentmode.md)
  Constants that indicate how to render web view content.
- [WKWebpagePreferences.UpgradeToHTTPSPolicy](../wkwebpagepreferences/upgradetohttpspolicy.md)
- [enum WKSecurityRestrictionMode](../wksecurityrestrictionmode.md)
- [WKPreferences.InactiveSchedulingPolicy](../wkpreferences/inactiveschedulingpolicy-swift.enum.md)
  An enumeration that lists policies for how a web view that’s not in a window handles tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/fullscreenstate-swift.enum)*