# isEnabled

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the tooltip interaction is in the enabled state.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isEnabled: Bool { get set }
```

#### Discussion

A view or control can only display a tooltip from an enabled interaction. Set the value of the [`isEnabled`](uitooltipinteraction/isenabled.md) property to [`true`](https://developer.apple.com/documentation/Swift/true) to enable the interaction or [`false`](https://developer.apple.com/documentation/Swift/false) to disable it. The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var defaultToolTip: String?](uitooltipinteraction/defaulttooltip.md)
  The text that appears in a tooltip by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitooltipinteraction/isenabled)*