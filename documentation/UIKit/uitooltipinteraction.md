# UIToolTipInteraction

**Framework**: UIKit  
**Kind**: class

An interaction object that makes it possible to show a tooltip when hovering a pointer over a view or control.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIToolTipInteraction
```

#### Overview

To show a tooltip when the pointer hovers over a view, add a [`UIToolTipInteraction`](uitooltipinteraction.md) object to the view. For example, the following code listings shows how to add a tooltip to a label:

```swift
let label = UILabel()
label.text = "Label with a tooltip"

let tooltipInteraction = UIToolTipInteraction(defaultToolTip: "The label's tooltip.")
label.addInteraction(tooltipInteraction)
```

If you want your app to determine the tooltip text at a later time — for instance, to reflect the current state of your app — set the interaction’s [`delegate`](uitooltipinteraction/delegate.md) property to an object that conforms to the [`UIToolTipInteractionDelegate`](uitooltipinteractiondelegate.md) protocol.

To add a tooltip to a control derived from [`UIControl`](uicontrol.md), use the convenience property [`toolTip`](uicontrol/tooltip.md); for example, to add a tooltip to the button:

```swift
let button = UIButton(configuration: configuration, primaryAction: action)
button.toolTip = "Click to buy this item. You'll have a chance to change your mind before confirming your purchase."
```

Setting the [`toolTip`](uicontrol/tooltip.md) property creates a tooltip interaction for the control, which you can retrieve from the [`toolTipInteraction`](uicontrol/tooltipinteraction.md) property.

> **Note**:  Tooltips appear when your app runs in macOS or visionOS. To show a tooltip in macOS, your app must be an iPhone or iPad app running on a Mac with Apple silicon, or built with Mac Catalyst.

## Topics

### Creating a tooltip interaction
- [init()](uitooltipinteraction/init.md)
  Creates a tooltip interaction object.
- [init(defaultToolTip: String)](uitooltipinteraction/init(defaulttooltip:).md)
  Creates a tooltip interaction object and sets the default tooltip text.
### Managing the interaction
- [var isEnabled: Bool](uitooltipinteraction/isenabled.md)
  A Boolean value that indicates whether the tooltip interaction is in the enabled state.
- [var defaultToolTip: String?](uitooltipinteraction/defaulttooltip.md)
  The text that appears in a tooltip by default.
### Providing tooltip configurations
- [var delegate: (any UIToolTipInteractionDelegate)?](uitooltipinteraction/delegate.md)
  An object that provides text that a tooltip displays instead of the default text.
- [protocol UIToolTipInteractionDelegate](uitooltipinteractiondelegate.md)
  An interface that provides tooltip settings to an interaction.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIInteraction](uiinteraction.md)

## See Also

- [Showing help tags for views and controls using tooltip interactions](showing-help-tags-for-views-and-controls-using-tooltip-interactions.md)
  Explain the purpose of interface elements by showing a tooltip when a person positions the pointer over the element.
- [protocol UIToolTipInteractionDelegate](uitooltipinteractiondelegate.md)
  An interface that provides tooltip settings to an interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitooltipinteraction)*