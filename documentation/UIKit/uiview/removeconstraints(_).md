# removeConstraints(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified constraints from the view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func removeConstraints(_ constraints: [NSLayoutConstraint])
```

```objc
- (void) removeConstraints:(NSArray<__kindof NSLayoutConstraint *> *) constraints;
```

#### Discussion

When developing for iOS 8.0 or later, use the [`NSLayoutConstraint`](../nslayoutconstraint.md) class’s  [`deactivate(_:)`](../nslayoutconstraint/deactivate%28_%29.md) method instead of calling the [`removeConstraints(_:)`](./removeconstraints%28_%29.md) method directly. The [`deactivate(_:)`](../nslayoutconstraint/deactivate%28_%29.md) method automatically removes the constraints from the correct views.

## Parameters

- `constraints`: The constraints to remove.

## See Also

### Managing the view’s constraints
- [var constraints: [NSLayoutConstraint]](./constraints.md)
  The constraints held by the view.
- [func addConstraint(NSLayoutConstraint)](./addconstraint%28_%29.md)
  Adds a constraint on the layout of the receiving view or its subviews.
- [func addConstraints([NSLayoutConstraint])](./addconstraints%28_%29.md)
  Adds multiple constraints on the layout of the receiving view or its subviews.
- [func removeConstraint(NSLayoutConstraint)](./removeconstraint%28_%29.md)
  Removes the specified constraint from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/removeconstraints(_:))*