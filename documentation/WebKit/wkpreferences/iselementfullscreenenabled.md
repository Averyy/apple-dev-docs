# isElementFullscreenEnabled

**Framework**: WebKit  
**Kind**: property

A Boolean value that indicates whether a web view can display content full screen.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isElementFullscreenEnabled: Bool { get set }
```

#### Discussion

The default value for this preference is [`false`](https://developer.apple.com/documentation/Swift/false).

> ❗ **Important**:  When this value is [`true`](https://developer.apple.com/documentation/Swift/true) and a page requests full-screen mode, the system removes the [`WKWebView`](wkwebview.md) from your app’s view hierarchy.

## See Also

- [var tabFocusesLinks: Bool](wkpreferences/tabfocuseslinks.md)
  A Boolean value that indicates whether pressing the tab key changes the focus to links and form controls.
- [var isTextInteractionEnabled: Bool](wkpreferences/istextinteractionenabled.md)
  A Boolean value that indicates whether to allow people to select or otherwise interact with text.
- [var inactiveSchedulingPolicy: WKPreferences.InactiveSchedulingPolicy](wkpreferences/inactiveschedulingpolicy-swift.property.md)
  A policy you set to specify how a web view that’s not in a window handles tasks.
- [WKPreferences.InactiveSchedulingPolicy](wkpreferences/inactiveschedulingpolicy-swift.enum.md)
  An enumeration that lists policies for how a web view that’s not in a window handles tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkpreferences/iselementfullscreenenabled)*