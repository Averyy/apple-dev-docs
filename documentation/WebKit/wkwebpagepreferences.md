# WKWebpagePreferences

**Framework**: Webkit  
**Kind**: class

An object that specifies the behaviors to use when loading and rendering page content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKWebpagePreferences
```

#### Overview

Create a [`WKWebpagePreferences`](wkwebpagepreferences.md) object when you want to change the default rendering behavior of your web view. Typically, iOS devices render web content for a mobile experience, and Mac devices render content for a desktop experience.

## Topics

### Setting the JavaScript preferences
- [var allowsContentJavaScript: Bool](wkwebpagepreferences/allowscontentjavascript.md)
  A Boolean value that indicates whether JavaScript from web content is allowed to run.
### Setting the preferred content mode
- [var preferredContentMode: WKWebpagePreferences.ContentMode](wkwebpagepreferences/preferredcontentmode.md)
  The content mode for the web view to use when it loads and renders a webpage.
- [WKWebpagePreferences.ContentMode](wkwebpagepreferences/contentmode.md)
  Constants that indicate how to render web view content.
### Getting Lockdown Mode info
- [var isLockdownModeEnabled: Bool](wkwebpagepreferences/islockdownmodeenabled.md)
  A Boolean value that indicates whether to use Lockdown Mode in the web view.
### Instance Properties
- [var preferredHTTPSNavigationPolicy: WKWebpagePreferences.UpgradeToHTTPSPolicy](wkwebpagepreferences/preferredhttpsnavigationpolicy.md)
### Enumerations
- [WKWebpagePreferences.UpgradeToHTTPSPolicy](wkwebpagepreferences/upgradetohttpspolicy.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class WKWebViewConfiguration](wkwebviewconfiguration.md)
  A collection of properties that you use to initialize a web view.
- [class WKWindowFeatures](wkwindowfeatures.md)
  Display-related attributes that a webpage requests for its window.
- [class WKProcessPool](wkprocesspool.md)
  An opaque token that you use to run multiple web views in a single process.
- [class WKPreferences](wkpreferences.md)
  An object that encapsulates the standard behaviors to apply to websites.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebpagepreferences)*