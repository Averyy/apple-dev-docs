# constraints(activeWhenAwayFrom:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the constraints that the tracking layout guide activates when it’s away from the given edge, and deactivates when it’s near the edge.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
func constraints(activeWhenAwayFrom edge: NSDirectionalRectEdge) -> [NSLayoutConstraint]
```

```objc
- (NSArray<NSLayoutConstraint *> *) constraintsActiveWhenAwayFromEdge:(NSDirectionalRectEdge) edge;
```

## Return Value

An array of layout constraints that the tracking layout guide automatically activates and deactivates.

## Parameters

- `edge`: The edge that the tracking layout guide uses to determine when to activate or deactivate the constraints.

## See Also

### Configuring automatic constraint activation
- [func setConstraints([NSLayoutConstraint], activeWhenNearEdge: NSDirectionalRectEdge)](./setconstraints%28_,activewhennearedge%29.md)
  Configures the tracking layout guide to automatically activate and deactivate constraints when the guide is close to the given edge.
- [func setConstraints([NSLayoutConstraint], activeWhenAwayFrom: NSDirectionalRectEdge)](./setconstraints%28_,activewhenawayfrom%29.md)
  Configures the tracking layout guide to automatically activate and deactivate constraints when the guide is away from the given edge.
- [func constraints(activeWhenNearEdge: NSDirectionalRectEdge) -> [NSLayoutConstraint]](./constraints%28activewhennearedge%29.md)
  Returns the constraints that the tracking layout guide activates when it’s near the given edge, and deactivates when it’s away from the given edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitrackinglayoutguide/constraints(activewhenawayfrom:))*