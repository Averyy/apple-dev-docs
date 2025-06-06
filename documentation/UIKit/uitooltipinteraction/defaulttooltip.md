# defaultToolTip

**Framework**: UIKit  
**Kind**: property

The text that appears in a tooltip by default.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var defaultToolTip: String? { get set }
```

#### Discussion

Set this property to the default text to display in the tooltip.

If you set the [`delegate`](uitooltipinteraction/delegate.md) property to an object that conforms to the [`UIToolTipInteractionDelegate`](uitooltipinteractiondelegate.md) protocol and implements the [`toolTipInteraction(_:configurationAt:)`](uitooltipinteractiondelegate/tooltipinteraction(_:configurationat:).md) method, then the return value of the delegate method determines the text that appears in the tooltip.

## See Also

- [var isEnabled: Bool](uitooltipinteraction/isenabled.md)
  A Boolean value that indicates whether the tooltip interaction is in the enabled state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitooltipinteraction/defaulttooltip)*