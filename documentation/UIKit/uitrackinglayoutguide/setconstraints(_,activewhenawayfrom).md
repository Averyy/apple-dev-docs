# setConstraints(_:activeWhenAwayFrom:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Configures the tracking layout guide to automatically activate and deactivate constraints when the guide is away from the given edge.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
func setConstraints(_ trackingConstraints: [NSLayoutConstraint], activeWhenAwayFrom edge: NSDirectionalRectEdge)
```

```objc
- (void) setConstraints:(NSArray<NSLayoutConstraint *> *) trackingConstraints activeWhenAwayFromEdge:(NSDirectionalRectEdge) edge;
```

## Parameters

- `trackingConstraints`: The constraints to deactivate when the tracking layout guide is close to `edge`, and to activate when it moves away from `edge`. If you pass `nil`, the guide deactivates any currently active constraints associated with this edge and removes them from tracking.
- `edge`: The edge that the tracking layout guide uses to determine whether to activate or deactivate the constraints.

## See Also

### Configuring automatic constraint activation
- [func setConstraints([NSLayoutConstraint], activeWhenNearEdge: NSDirectionalRectEdge)](./setconstraints%28_,activewhennearedge%29.md)
  Configures the tracking layout guide to automatically activate and deactivate constraints when the guide is close to the given edge.
- [func constraints(activeWhenNearEdge: NSDirectionalRectEdge) -> [NSLayoutConstraint]](./constraints%28activewhennearedge%29.md)
  Returns the constraints that the tracking layout guide activates when it’s near the given edge, and deactivates when it’s away from the given edge.
- [func constraints(activeWhenAwayFrom: NSDirectionalRectEdge) -> [NSLayoutConstraint]](./constraints%28activewhenawayfrom%29.md)
  Returns the constraints that the tracking layout guide activates when it’s away from the given edge, and deactivates when it’s near the edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitrackinglayoutguide/setconstraints(_:activewhenawayfrom:))*