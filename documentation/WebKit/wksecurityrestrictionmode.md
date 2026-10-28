# WKSecurityRestrictionMode

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
enum WKSecurityRestrictionMode
```

```c
enum WKSecurityRestrictionMode : NSInteger;
```

## Overview

Security restriction modes for WebView content.

## Topics

### Enumeration Cases
- [WKSecurityRestrictionMode.lockdown](./wksecurityrestrictionmode/lockdown.md)
- [WKSecurityRestrictionMode.maximizeCompatibility](./wksecurityrestrictionmode/maximizecompatibility.md)
- [WKSecurityRestrictionMode.none](./wksecurityrestrictionmode/none.md)
### Initializers
- [init?(rawValue: Int)](./wksecurityrestrictionmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Web view configuration
- [class WKWebViewConfiguration](./wkwebviewconfiguration.md)
  A collection of properties that you use to initialize a web view.
- [class WKWindowFeatures](./wkwindowfeatures.md)
  Display-related attributes that a webpage requests for its window.
- [class WKProcessPool](./wkprocesspool.md)
  An opaque token that you use to run multiple web views in a single process.
- [class WKPreferences](./wkpreferences.md)
  An object that encapsulates the standard behaviors to apply to websites.
- [class WKWebpagePreferences](./wkwebpagepreferences.md)
  An object that specifies the behaviors to use when loading and rendering page content.
- [WKWebpagePreferences.ContentMode](./wkwebpagepreferences/contentmode.md)
  Constants that indicate how to render web view content.
- [WKWebpagePreferences.UpgradeToHTTPSPolicy](./wkwebpagepreferences/upgradetohttpspolicy.md)
- [WKPreferences.InactiveSchedulingPolicy](./wkpreferences/inactiveschedulingpolicy-swift.enum.md)
  An enumeration that lists policies for how a web view that’s not in a window handles tasks.
- [WKWebView.FullscreenState](./wkwebview/fullscreenstate-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wksecurityrestrictionmode)*