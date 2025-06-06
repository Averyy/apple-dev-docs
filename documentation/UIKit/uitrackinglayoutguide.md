# UITrackingLayoutGuide

**Framework**: UIKit  
**Kind**: class

A layout guide that automatically activates and deactivates layout constraints depending on its proximity to edges.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITrackingLayoutGuide
```

## Topics

### Configuring automatic constraint activation
- [func setConstraints([NSLayoutConstraint], activeWhenNearEdge: NSDirectionalRectEdge)](uitrackinglayoutguide/setconstraints(_:activewhennearedge:).md)
  Configures the tracking layout guide to automatically activate and deactivate constraints when the guide is close to the given edge.
- [func setConstraints([NSLayoutConstraint], activeWhenAwayFrom: NSDirectionalRectEdge)](uitrackinglayoutguide/setconstraints(_:activewhenawayfrom:).md)
  Configures the tracking layout guide to automatically activate and deactivate constraints when the guide is away from the given edge.
- [func constraints(activeWhenNearEdge: NSDirectionalRectEdge) -> [NSLayoutConstraint]](uitrackinglayoutguide/constraints(activewhennearedge:).md)
  Returns the constraints that the tracking layout guide activates when it’s near the given edge, and deactivates when it’s away from the given edge.
- [func constraints(activeWhenAwayFrom: NSDirectionalRectEdge) -> [NSLayoutConstraint]](uitrackinglayoutguide/constraints(activewhenawayfrom:).md)
  Returns the constraints that the tracking layout guide activates when it’s away from the given edge, and deactivates when it’s near the edge.
### Tracking constraints
- [func removeAllTrackedConstraints()](uitrackinglayoutguide/removealltrackedconstraints.md)
  Stops the layout guide from tracking any constraints.

## Relationships

### Inherits From
- [UILayoutGuide](uilayoutguide.md)
### Inherited By
- [UIKeyboardLayoutGuide](uikeyboardlayoutguide.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)

## See Also

- [Adjusting your layout with keyboard layout guide](adjusting-your-layout-with-keyboard-layout-guide.md)
  Respond dynamically to keyboard movement by using the tracking features of the keyboard layout guide.
- [class UIKeyboardLayoutGuide](uikeyboardlayoutguide.md)
  A layout guide that represents the space the keyboard occupies in your app’s layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitrackinglayoutguide)*