# defaultToolTip

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The text that appears in a tooltip by default.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
var defaultToolTip: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * defaultToolTip;
```

## Discussion

Set this property to the default text to display in the tooltip.

If you set the [`delegate`](./delegate.md) property to an object that conforms to the [`UIToolTipInteractionDelegate`](../uitooltipinteractiondelegate.md) protocol and implements the [`toolTipInteraction(_:configurationAt:)`](../uitooltipinteractiondelegate/tooltipinteraction%28_,configurationat%29.md) method, then the return value of the delegate method determines the text that appears in the tooltip.

## See Also

### Managing the interaction
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the tooltip interaction is in the enabled state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitooltipinteraction/defaulttooltip)*