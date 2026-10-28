# addConstraint(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds a constraint on the layout of the receiving view or its subviews.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func addConstraint(_ constraint: NSLayoutConstraint)
```

```objc
- (void) addConstraint:(NSLayoutConstraint *) constraint;
```

## Discussion

The constraint must involve only views that are within scope of the receiving view. Specifically, any views involved must be either the receiving view itself, or a subview of the receiving view. Constraints that are added to a view are said to be held by that view. The coordinate system used when evaluating the constraint is the coordinate system of the view that holds the constraint.

When developing for iOS 8.0 or later, set the constraint’s [`isActive`](../nslayoutconstraint/isactive.md) property to [`true`](../../Swift/true.md) instead of calling the [`addConstraint(_:)`](./addconstraint%28_%29.md) method directly. The [`isActive`](../nslayoutconstraint/isactive.md) property automatically adds and removes the constraint from the correct view.

## Parameters

- `constraint`: The constraint to be added to the view. The constraint may only reference the view itself or its subviews.

## See Also

### Managing the view’s constraints
- [var constraints: [NSLayoutConstraint]](./constraints.md)
  The constraints held by the view.
- [func addConstraints([NSLayoutConstraint])](./addconstraints%28_%29.md)
  Adds multiple constraints on the layout of the receiving view or its subviews.
- [func removeConstraint(NSLayoutConstraint)](./removeconstraint%28_%29.md)
  Removes the specified constraint from the view.
- [func removeConstraints([NSLayoutConstraint])](./removeconstraints%28_%29.md)
  Removes the specified constraints from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/addconstraint(_:))*