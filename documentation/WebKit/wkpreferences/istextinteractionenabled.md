# isTextInteractionEnabled

**Framework**: Webkit  
**Kind**: property

A Boolean value that indicates whether to allow people to select or otherwise interact with text.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isTextInteractionEnabled: Bool { get set }
```

#### Discussion

The default value for this preference is [`true`](https://developer.apple.com/documentation/swift/true) on macOS and iOS. On watchOS, the default value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var tabFocusesLinks: Bool](wkpreferences/tabfocuseslinks.md)
  A Boolean value that indicates whether pressing the tab key changes the focus to links and form controls.
- [var isElementFullscreenEnabled: Bool](wkpreferences/iselementfullscreenenabled.md)
  A Boolean value that indicates whether a web view can display content full screen.
- [var inactiveSchedulingPolicy: WKPreferences.InactiveSchedulingPolicy](wkpreferences/inactiveschedulingpolicy-swift.property.md)
  A policy you set to specify how a web view that’s not in a window handles tasks.
- [WKPreferences.InactiveSchedulingPolicy](wkpreferences/inactiveschedulingpolicy-swift.enum.md)
  An enumeration that lists policies for how a web view that’s not in a window handles tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkpreferences/istextinteractionenabled)*