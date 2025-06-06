# setConstraints(_:activeWhenNearEdge:)

**Framework**: UIKit  
**Kind**: method

Configures the tracking layout guide to automatically activate and deactivate constraints when the guide is close to the given edge.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setConstraints(_ trackingConstraints: [NSLayoutConstraint], activeWhenNearEdge edge: NSDirectionalRectEdge)
```

## Parameters

- `trackingConstraints`: The constraints to activate when the tracking layout guide is close to  , and to deactivate when it moves away from  . If you pass  , the guide stops tracking the constraints associated with  .
- `edge`: The edge that the tracking layout guide uses to determine whether to activate or deactivate the constraints.

## See Also

- [func setConstraints([NSLayoutConstraint], activeWhenAwayFrom: NSDirectionalRectEdge)](uitrackinglayoutguide/setconstraints(_:activewhenawayfrom:).md)
  Configures the tracking layout guide to automatically activate and deactivate constraints when the guide is away from the given edge.
- [func constraints(activeWhenNearEdge: NSDirectionalRectEdge) -> [NSLayoutConstraint]](uitrackinglayoutguide/constraints(activewhennearedge:).md)
  Returns the constraints that the tracking layout guide activates when it’s near the given edge, and deactivates when it’s away from the given edge.
- [func constraints(activeWhenAwayFrom: NSDirectionalRectEdge) -> [NSLayoutConstraint]](uitrackinglayoutguide/constraints(activewhenawayfrom:).md)
  Returns the constraints that the tracking layout guide activates when it’s away from the given edge, and deactivates when it’s near the edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitrackinglayoutguide/setconstraints(_:activewhennearedge:))*