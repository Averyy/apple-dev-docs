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
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var tabFocusesLinks: Bool](wkpreferences/tabfocuseslinks.md)
  A Boolean value that indicates whether pressing the tab key changes the focus to links and form controls.
- [var isTextInteractionEnabled: Bool](wkpreferences/istextinteractionenabled.md)
  A Boolean value that indicates whether to allow people to select or otherwise interact with text.
- [var isElementFullscreenEnabled: Bool](wkpreferences/iselementfullscreenenabled.md)
  A Boolean value that indicates whether a web view can display content full screen.
- [var inactiveSchedulingPolicy: WKPreferences.InactiveSchedulingPolicy](wkpreferences/inactiveschedulingpolicy-swift.property.md)
  A policy you set to specify how a web view that’s not in a window handles tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkpreferences/inactiveschedulingpolicy-swift.enum)*