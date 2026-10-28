# WKWebpagePreferences.UpgradeToHTTPSPolicy

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum WKWebpagePreferencesUpgradeToHTTPSPolicy : NSInteger;
```

## Overview

A secure navigation policy represents whether or not there is a preference for loading a webpage with https, and how failures should be handled.

## Topics

### Enumeration Cases
- [WKWebpagePreferences.UpgradeToHTTPSPolicy.automaticFallbackToHTTP](./upgradetohttpspolicy/automaticfallbacktohttp.md)
- [WKWebpagePreferences.UpgradeToHTTPSPolicy.errorOnFailure](./upgradetohttpspolicy/erroronfailure.md)
- [WKWebpagePreferences.UpgradeToHTTPSPolicy.keepAsRequested](./upgradetohttpspolicy/keepasrequested.md)
- [WKWebpagePreferences.UpgradeToHTTPSPolicy.userMediatedFallbackToHTTP](./upgradetohttpspolicy/usermediatedfallbacktohttp.md)
### Initializers
- [init?(rawValue: Int)](./upgradetohttpspolicy/init%28rawvalue%29.md)

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
- [WKWebpagePreferences.ContentMode](./contentmode.md)
  Constants that indicate how to render web view content.
- [enum WKSecurityRestrictionMode](../wksecurityrestrictionmode.md)
- [WKPreferences.InactiveSchedulingPolicy](../wkpreferences/inactiveschedulingpolicy-swift.enum.md)
  An enumeration that lists policies for how a web view that’s not in a window handles tasks.
- [WKWebView.FullscreenState](../wkwebview/fullscreenstate-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebpagepreferences/upgradetohttpspolicy)*