# delegate

**Framework**: UIKit  
**Kind**: property

An object that provides text that a tooltip displays instead of the default text.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UIToolTipInteractionDelegate)? { get set }
```

#### Discussion

To provide tooltip text based on the current state or unique logic of your app, set the [`delegate`](uitooltipinteraction/delegate.md) property to an object that conforms to the [`UIToolTipInteractionDelegate`](uitooltipinteractiondelegate.md) protocol and implements the [`toolTipInteraction(_:configurationAt:)`](uitooltipinteractiondelegate/tooltipinteraction(_:configurationat:).md) method. The method returns a [`UIToolTipConfiguration`](uitooltipconfiguration.md) object containing the text to display in the tooltip. For example, the following code listing instructs the tooltip to show the name of the view’s background color instead of the [`defaultToolTip`](uitooltipinteraction/defaulttooltip.md) text. If the color name is unavailable, the method returns `nil`, which disables the display of the tooltip.

```swift
func toolTipInteraction(_ interaction: UIToolTipInteraction, configurationAt point: CGPoint) -> UIToolTipConfiguration? {
    let configuration: UIToolTipConfiguration?
    if let accessibilityName = backgroundColor?.accessibilityName {
        configuration = UIToolTipConfiguration(toolTip: "The color is \(accessibilityName).")
    } else {
        configuration = nil
    }
    
    return configuration
}
```

## See Also

- [protocol UIToolTipInteractionDelegate](uitooltipinteractiondelegate.md)
  An interface that provides tooltip settings to an interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitooltipinteraction/delegate)*