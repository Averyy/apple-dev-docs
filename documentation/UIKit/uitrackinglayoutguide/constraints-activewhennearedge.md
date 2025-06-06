# constraints(activeWhenNearEdge:)

**Framework**: UIKit  
**Kind**: method

Returns the constraints that the tracking layout guide activates when it’s near the given edge, and deactivates when it’s away from the given edge.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func constraints(activeWhenNearEdge edge: NSDirectionalRectEdge) -> [NSLayoutConstraint]
```

#### Return Value

An array of layout constraints that the tracking layout guide automatically activates and deactivates.

## Parameters

- `edge`: The edge that the tracking layout guide uses to determine when to activate or deactivate the constraints.

## See Also

- [func setConstraints([NSLayoutConstraint], activeWhenNearEdge: NSDirectionalRectEdge)](uitrackinglayoutguide/setconstraints(_:activewhennearedge:).md)
  Configures the tracking layout guide to automatically activate and deactivate constraints when the guide is close to the given edge.
- [func setConstraints([NSLayoutConstraint], activeWhenAwayFrom: NSDirectionalRectEdge)](uitrackinglayoutguide/setconstraints(_:activewhenawayfrom:).md)
  Configures the tracking layout guide to automatically activate and deactivate constraints when the guide is away from the given edge.
- [func constraints(activeWhenAwayFrom: NSDirectionalRectEdge) -> [NSLayoutConstraint]](uitrackinglayoutguide/constraints(activewhenawayfrom:).md)
  Returns the constraints that the tracking layout guide activates when it’s away from the given edge, and deactivates when it’s near the edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitrackinglayoutguide/constraints(activewhennearedge:))*