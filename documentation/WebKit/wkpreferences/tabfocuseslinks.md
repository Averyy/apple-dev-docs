# tabFocusesLinks

**Framework**: WebKit  
**Kind**: property

A Boolean value that indicates whether pressing the tab key changes the focus to links and form controls.

**Availability**:
- macOS 10.12.4+

## Declaration

```swift
@MainActor
var tabFocusesLinks: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the web view includes links and form controls in the set of items that may receive focus. Pressing the Option key temporarily reverses this preference.

## See Also

- [var isTextInteractionEnabled: Bool](wkpreferences/istextinteractionenabled.md)
  A Boolean value that indicates whether to allow people to select or otherwise interact with text.
- [var isElementFullscreenEnabled: Bool](wkpreferences/iselementfullscreenenabled.md)
  A Boolean value that indicates whether a web view can display content full screen.
- [var inactiveSchedulingPolicy: WKPreferences.InactiveSchedulingPolicy](wkpreferences/inactiveschedulingpolicy-swift.property.md)
  A policy you set to specify how a web view that’s not in a window handles tasks.
- [WKPreferences.InactiveSchedulingPolicy](wkpreferences/inactiveschedulingpolicy-swift.enum.md)
  An enumeration that lists policies for how a web view that’s not in a window handles tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkpreferences/tabfocuseslinks)*