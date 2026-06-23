# WKProcessPool

**Framework**: WebKit  
**Kind**: class

An opaque token that you use to run multiple web views in a single process.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKProcessPool
```

#### Overview

A [`WKProcessPool`](wkprocesspool.md) object represents a single process that WebKit uses to manage web content. To provide a more secure and stable experience, WebKit renders the content of web views in separate processes, rather than in your app’s process space. By default, WebKit gives each web view its own process space until it reaches an implementation-defined process limit. After that, web views with the same [`WKProcessPool`](wkprocesspool.md) object share the same web content process.

If your app creates multiple web views, assign the same [`WKProcessPool`](wkprocesspool.md) object to web views that may safely share a process space. Instantiate an instance of this class and assign it to the [`processPool`](wkwebviewconfiguration/processpool.md) property of each web view’s [`WKWebViewConfiguration`](wkwebviewconfiguration.md) object.

## Topics

### Initializers
- [init?(coder: NSCoder)](wkprocesspool/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class WKWebViewConfiguration](wkwebviewconfiguration.md)
  A collection of properties that you use to initialize a web view.
- [class WKWindowFeatures](wkwindowfeatures.md)
  Display-related attributes that a webpage requests for its window.
- [class WKPreferences](wkpreferences.md)
  An object that encapsulates the standard behaviors to apply to websites.
- [class WKWebpagePreferences](wkwebpagepreferences.md)
  An object that specifies the behaviors to use when loading and rendering page content.
- [WKWebpagePreferences.ContentMode](wkwebpagepreferences/contentmode.md)
  Constants that indicate how to render web view content.
- [WKWebpagePreferences.UpgradeToHTTPSPolicy](wkwebpagepreferences/upgradetohttpspolicy.md)
- [enum WKSecurityRestrictionMode](wksecurityrestrictionmode.md)
- [WKPreferences.InactiveSchedulingPolicy](wkpreferences/inactiveschedulingpolicy-swift.enum.md)
  An enumeration that lists policies for how a web view that’s not in a window handles tasks.
- [WKWebView.FullscreenState](wkwebview/fullscreenstate-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkprocesspool)*