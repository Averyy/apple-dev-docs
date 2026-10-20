# removeConstraint(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified constraint from the view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func removeConstraint(_ constraint: NSLayoutConstraint)
```

```objc
- (void) removeConstraint:(NSLayoutConstraint *) constraint;
```

#### Discussion

When developing for iOS 8.0 or later, set the constraint’s [`isActive`](../nslayoutconstraint/isactive.md) property to [`false`](../../Swift/false.md) instead of calling the [`removeConstraint(_:)`](./removeconstraint%28_%29.md) method directly. The [`isActive`](../nslayoutconstraint/isactive.md) property automatically adds and removes the constraint from the correct view.

## Parameters

- `constraint`: The constraint to remove. Removing a constraint not held by the view has no effect.

## See Also

### Managing the view’s constraints
- [var constraints: [NSLayoutConstraint]](./constraints.md)
  The constraints held by the view.
- [func addConstraint(NSLayoutConstraint)](./addconstraint%28_%29.md)
  Adds a constraint on the layout of the receiving view or its subviews.
- [func addConstraints([NSLayoutConstraint])](./addconstraints%28_%29.md)
  Adds multiple constraints on the layout of the receiving view or its subviews.
- [func removeConstraints([NSLayoutConstraint])](./removeconstraints%28_%29.md)
  Removes the specified constraints from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/removeconstraint(_:))*