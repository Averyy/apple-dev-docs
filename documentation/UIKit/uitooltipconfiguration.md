# UIToolTipConfiguration

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UIToolTipConfiguration : NSObject
```

#### Overview

Use a tooltip configuration to specify:

- The text that appears in the tooltip.
- The region that the pointer must hover over to trigger the appearance of the tooltip.

A [`UIToolTipInteraction`](./uitooltipinteraction.md) object asks for a configuration from its [`delegate`](./uitooltipinteraction/delegate.md) by calling the delegate method [`toolTipInteraction(_:configurationAt:)`](./uitooltipinteractiondelegate/tooltipinteraction%28_,configurationat%29.md).

## Topics

### Creating a tooltip configuration
- [convenience init(toolTip: String)](./uitooltipconfiguration/init%28tooltip%29.md)
  Creates a tooltip configuration and sets the tooltip text.
- [convenience init(toolTip: String, in: CGRect)](./uitooltipconfiguration/init%28tooltip,in%29.md)
  Creates a tooltip configuration, and sets the tooltip text and hover region within the view or control.
### Accessing the configuration settings
- [var toolTip: String](./uitooltipconfiguration/tooltip.md)
  The text to display in the tooltip.
- [var sourceRect: CGRect?](./uitooltipconfiguration/sourcerect-8zvo1.md)
  The region of the view or control where the pointer must hover to trigger the appearance of the tooltip.
### Initializers
- [convenience init(toolTip: String, inRect: CGRect)](./uitooltipconfiguration/init%28tooltip,inrect%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Providing a tooltip configuration
- [func toolTipInteraction(UIToolTipInteraction, configurationAt: CGPoint) -> UIToolTipConfiguration?](./uitooltipinteractiondelegate/tooltipinteraction%28_,configurationat%29.md)
  Asks the delegate for a tooltip configuration that describes the tooltip settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitooltipconfiguration)*