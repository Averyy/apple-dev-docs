# WKPreferences

**Framework**: WebKit  
**Kind**: class

An object that encapsulates the standard behaviors to apply to websites.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKPreferences
```

#### Overview

Use a [`WKPreferences`](wkpreferences.md) object to specify the preferences for your website, including the minimum font size, the JavaScript behavior, and the behavior for handling fraudulent websites. Create this object and assign it to the [`preferences`](wkwebviewconfiguration/preferences.md) property of the [`WKWebViewConfiguration`](wkwebviewconfiguration.md) object you use to create your web view.

## Topics

### Setting Rendering Preferences
- [var minimumFontSize: CGFloat](wkpreferences/minimumfontsize.md)
  The minimum font size, in points.
- [var shouldPrintBackgrounds: Bool](wkpreferences/shouldprintbackgrounds.md)
  A Boolean value that indicates whether to include any background color or graphics when printing content.
### Setting Behavior Preferences
- [var tabFocusesLinks: Bool](wkpreferences/tabfocuseslinks.md)
  A Boolean value that indicates whether pressing the tab key changes the focus to links and form controls.
- [var isTextInteractionEnabled: Bool](wkpreferences/istextinteractionenabled.md)
  A Boolean value that indicates whether to allow people to select or otherwise interact with text.
- [var isElementFullscreenEnabled: Bool](wkpreferences/iselementfullscreenenabled.md)
  A Boolean value that indicates whether a web view can display content full screen.
- [var inactiveSchedulingPolicy: WKPreferences.InactiveSchedulingPolicy](wkpreferences/inactiveschedulingpolicy-swift.property.md)
  A policy you set to specify how a web view that’s not in a window handles tasks.
- [WKPreferences.InactiveSchedulingPolicy](wkpreferences/inactiveschedulingpolicy-swift.enum.md)
  An enumeration that lists policies for how a web view that’s not in a window handles tasks.
### Setting Java and JavaScript Preferences
- [var javaScriptCanOpenWindowsAutomatically: Bool](wkpreferences/javascriptcanopenwindowsautomatically.md)
  A Boolean value that indicates whether JavaScript can open windows without user interaction.
- [var isSiteSpecificQuirksModeEnabled: Bool](wkpreferences/issitespecificquirksmodeenabled.md)
  A Boolean that indicates whether to apply site-specific compatibility workarounds.
### Setting Fraud Warning Preferences
- [var isFraudulentWebsiteWarningEnabled: Bool](wkpreferences/isfraudulentwebsitewarningenabled.md)
  A Boolean value that indicates whether the web view shows warnings for suspected fraudulent content, such as malware or phishing attemps.
### Deprecated
- [var javaEnabled: Bool](wkpreferences/javaenabled.md)
  A Boolean value that indicates whether Java is enabled.
- [var javaScriptEnabled: Bool](wkpreferences/javascriptenabled.md)
  A Boolean value that indicates whether JavaScript is enabled.
- [var plugInsEnabled: Bool](wkpreferences/pluginsenabled.md)
  A Boolean value that indicates whether plug-ins are enabled.
### Instance Properties
- [var isLookToScrollEnabled: Bool](wkpreferences/islooktoscrollenabled.md)

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
- [class WKProcessPool](wkprocesspool.md)
  An opaque token that you use to run multiple web views in a single process.
- [class WKWebpagePreferences](wkwebpagepreferences.md)
  An object that specifies the behaviors to use when loading and rendering page content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkpreferences)*