# WKWebpagePreferences.UpgradeToHTTPSPolicy

**Framework**: WebKit  
**Kind**: enum

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- visionOS 2.2+

## Declaration

```swift
enum UpgradeToHTTPSPolicy
```

#### Overview

A secure navigation policy represents whether or not there is a preference for loading a webpage with https, and how failures should be handled.

## Topics

### Enumeration Cases
- [WKWebpagePreferences.UpgradeToHTTPSPolicy.automaticFallbackToHTTP](wkwebpagepreferences/upgradetohttpspolicy/automaticfallbacktohttp.md)
- [WKWebpagePreferences.UpgradeToHTTPSPolicy.errorOnFailure](wkwebpagepreferences/upgradetohttpspolicy/erroronfailure.md)
- [WKWebpagePreferences.UpgradeToHTTPSPolicy.keepAsRequested](wkwebpagepreferences/upgradetohttpspolicy/keepasrequested.md)
- [WKWebpagePreferences.UpgradeToHTTPSPolicy.userMediatedFallbackToHTTP](wkwebpagepreferences/upgradetohttpspolicy/usermediatedfallbacktohttp.md)
### Initializers
- [init?(rawValue: Int)](wkwebpagepreferences/upgradetohttpspolicy/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [enum WKSecurityRestrictionMode](wksecurityrestrictionmode.md)
- [WKPreferences.InactiveSchedulingPolicy](wkpreferences/inactiveschedulingpolicy-swift.enum.md)
  An enumeration that lists policies for how a web view that’s not in a window handles tasks.
- [WKWebView.FullscreenState](wkwebview/fullscreenstate-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebpagepreferences/upgradetohttpspolicy)*