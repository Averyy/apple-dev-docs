# inactiveSchedulingPolicy

**Framework**: Webkit  
**Kind**: property

A policy you set to specify how a web view that’s not in a window handles tasks.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var inactiveSchedulingPolicy: WKPreferences.InactiveSchedulingPolicy { get set }
```

#### Discussion

Set this to indicate how a web view that’s not in a window handles tasks; for example, when the web view is in a background tab in a browser. The default value is [`WKPreferences.InactiveSchedulingPolicy.suspend`](wkpreferences/inactiveschedulingpolicy-swift.enum/suspend.md).

A web view that’s not in a window is exempted from this policy if it is playing media, performing media capture, or performing another user-interactive activity.

## See Also

- [var tabFocusesLinks: Bool](wkpreferences/tabfocuseslinks.md)
  A Boolean value that indicates whether pressing the tab key changes the focus to links and form controls.
- [var isTextInteractionEnabled: Bool](wkpreferences/istextinteractionenabled.md)
  A Boolean value that indicates whether to allow people to select or otherwise interact with text.
- [var isElementFullscreenEnabled: Bool](wkpreferences/iselementfullscreenenabled.md)
  A Boolean value that indicates whether a web view can display content full screen.
- [WKPreferences.InactiveSchedulingPolicy](wkpreferences/inactiveschedulingpolicy-swift.enum.md)
  An enumeration that lists policies for how a web view that’s not in a window handles tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkpreferences/inactiveschedulingpolicy-swift.property)*