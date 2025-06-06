# UIToolTipConfiguration

**Framework**: UIKit  
**Kind**: class

An object that a tooltip interaction delegate uses to describe the tooltip settings.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIToolTipConfiguration
```

#### Overview

Use a tooltip configuration to specify:

- The text that appears in the tooltip.
- The region that the pointer must hover over to trigger the appearance of the tooltip.

A [`UIToolTipInteraction`](uitooltipinteraction.md) object asks for a configuration from its [`delegate`](uitooltipinteraction/delegate.md) by calling the delegate method [`toolTipInteraction(_:configurationAt:)`](uitooltipinteractiondelegate/tooltipinteraction(_:configurationat:).md).

## Topics

### Creating a tooltip configuration
- [convenience init(toolTip: String)](uitooltipconfiguration/init(tooltip:).md)
  Creates a tooltip configuration and sets the tooltip text.
- [convenience init(toolTip: String, in: CGRect)](uitooltipconfiguration/init(tooltip:in:).md)
  Creates a tooltip configuration, and sets the tooltip text and hover region within the view or control.
### Accessing the configuration settings
- [var toolTip: String](uitooltipconfiguration/tooltip.md)
  The text to display in the tooltip.
- [var sourceRect: CGRect?](uitooltipconfiguration/sourcerect-8zvo1.md)
  The region of the view or control where the pointer must hover to trigger the appearance of the tooltip.

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

## See Also

- [func toolTipInteraction(UIToolTipInteraction, configurationAt: CGPoint) -> UIToolTipConfiguration?](uitooltipinteractiondelegate/tooltipinteraction(_:configurationat:).md)
  Asks the delegate for a tooltip configuration that describes the tooltip settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitooltipconfiguration)*