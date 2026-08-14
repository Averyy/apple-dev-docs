# WKPreferences.InactiveSchedulingPolicy

**Framework**: WebKit  
**Kind**: enum

An enumeration that lists policies for how a web view that’s not in a window handles tasks.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum InactiveSchedulingPolicy
```

## Topics

### Scheduling policies
- [WKPreferences.InactiveSchedulingPolicy.none](wkpreferences/inactiveschedulingpolicy-swift.enum/none.md)
  A policy where a web view that’s not in a window runs tasks normally.
- [WKPreferences.InactiveSchedulingPolicy.suspend](wkpreferences/inactiveschedulingpolicy-swift.enum/suspend.md)
  A policy where a web view that’s not in a window fully suspends tasks.
- [WKPreferences.InactiveSchedulingPolicy.throttle](wkpreferences/inactiveschedulingpolicy-swift.enum/throttle.md)
  A policy where a web view that’s not in a window limits processing, but does not fully suspend tasks.
### Initializers
- [init?(rawValue: Int)](wkpreferences/inactiveschedulingpolicy-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class WKWebViewConfiguration](wkwebviewconfiguration.md)
  A collection of properties that you use to initialize a web view.
- [class WKWindowFeatures](wkwindowfeatures.md)
  Display-related attributes that a webpage requests for its window.
- [class WKProcessPool](wkprocesspool.md)
  An opaque token that you use to run multiple web views in a single process.
- [class WKPreferences](wkpreferences.md)
  An object that encapsulates the standard behaviors to apply to websites.
- [class WKWebpagePreferences](wkwebpagepreferences.md)
  An object that specifies the behaviors to use when loading and rendering page content.
- [WKWebpagePreferences.ContentMode](wkwebpagepreferences/contentmode.md)
  Constants that indicate how to render web view content.
- [WKWebpagePreferences.UpgradeToHTTPSPolicy](wkwebpagepreferences/upgradetohttpspolicy.md)
- [enum WKSecurityRestrictionMode](wksecurityrestrictionmode.md)
- [WKWebView.FullscreenState](wkwebview/fullscreenstate-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkpreferences/inactiveschedulingpolicy-swift.enum)*