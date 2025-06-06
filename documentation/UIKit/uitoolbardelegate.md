# UIToolbarDelegate

**Framework**: UIKit  
**Kind**: protocol

The interface that toolbar delegate objects implement to manage the toolbar behavior.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIToolbarDelegate : UIBarPositioningDelegate
```

#### Overview

This protocol declares no methods of its own, but conforms to the [`UIBarPositioningDelegate`](uibarpositioningdelegate.md) protocol to support the positioning of a toolbar when it’s moved to a window.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIBarPositioningDelegate](uibarpositioningdelegate.md)

## See Also

- [var delegate: (any UIToolbarDelegate)?](uitoolbar/delegate.md)
  The toolbar’s delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitoolbardelegate)*