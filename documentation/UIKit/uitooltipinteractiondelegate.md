# UIToolTipInteractionDelegate

**Framework**: UIKit  
**Kind**: protocol

An interface that provides tooltip settings to an interaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIToolTipInteractionDelegate : NSObjectProtocol
```

#### Overview

A tooltip interaction delegate provides configuration information about a tooltip. You can, for instance, use the delegate to change the text of a tooltip.

To change the tooltip text, set a tooltip interaction’s [`delegate`](uitextinteraction/delegate.md) property to an object that conforms to the [`UIToolTipInteractionDelegate`](uitooltipinteractiondelegate.md) protocol and implements the [`toolTipInteraction(_:configurationAt:)`](uitooltipinteractiondelegate/tooltipinteraction(_:configurationat:).md) method. For example, in the following code listing, the code creates a new view and assigns its background color. Then the code creates a [`UIToolTipInteraction`](uitooltipinteraction.md) object, sets the [`delegate`](uitextinteraction/delegate.md) equal to the view, and adds the interaction to the view.

```swift
lazy var viewWithBackgroundColorTooltip: UIView = {
    let view = ViewWithBackgroundColorTooltip()
    view.backgroundColor = UIColor.systemYellow
    
    let tooltipInteraction = UIToolTipInteraction()
    tooltipInteraction.delegate = view
    view.addInteraction(tooltipInteraction)
    
    return view
}()
```

The delegate’s implementation of the [`toolTipInteraction(_:configurationAt:)`](uitooltipinteractiondelegate/tooltipinteraction(_:configurationat:).md) method looks up the [`accessibilityName`](uicolor/accessibilityname.md) of the view’s background color. If the name is available, the method creates a [`UIToolTipConfiguration`](uitooltipconfiguration.md) object, passing in the name of the color. Then the method returns the configuration. If the name isn’t available, the method returns `nil`, which prevents the display of the tooltip.

```swift
class ViewWithBackgroundColorTooltip: UIView, UIToolTipInteractionDelegate {
    
    func toolTipInteraction(_ interaction: UIToolTipInteraction, configurationAt point: CGPoint) -> UIToolTipConfiguration? {

        let configuration: UIToolTipConfiguration?
        if let accessibilityName = backgroundColor?.accessibilityName {
            configuration = UIToolTipConfiguration(toolTip: "The color is \(accessibilityName).")
        } else {
            configuration = nil
        }
        
        return configuration
    }

}
```

In addition to changing the tooltip text, you can also specify the region within a view or control where a person must position the pointer to trigger the display of the tooltip. To specify the region, create the tooltip configuration using the [`init(toolTip:in:)`](uitooltipconfiguration/init(tooltip:in:).md) method.

## Topics

### Providing a tooltip configuration
- [func toolTipInteraction(UIToolTipInteraction, configurationAt: CGPoint) -> UIToolTipConfiguration?](uitooltipinteractiondelegate/tooltipinteraction(_:configurationat:).md)
  Asks the delegate for a tooltip configuration that describes the tooltip settings.
- [class UIToolTipConfiguration](uitooltipconfiguration.md)
  An object that a tooltip interaction delegate uses to describe the tooltip settings.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Showing help tags for views and controls using tooltip interactions](showing-help-tags-for-views-and-controls-using-tooltip-interactions.md)
  Explain the purpose of interface elements by showing a tooltip when a person positions the pointer over the element.
- [class UIToolTipInteraction](uitooltipinteraction.md)
  An interaction object that makes it possible to show a tooltip when hovering a pointer over a view or control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitooltipinteractiondelegate)*