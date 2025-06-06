# addConstraints(_:)

**Framework**: UIKit  
**Kind**: method

Adds multiple constraints on the layout of the receiving view or its subviews.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addConstraints(_ constraints: [NSLayoutConstraint])
```

#### Discussion

All constraints must involve only views that are within scope of the receiving view. Specifically, any views involved must be either the receiving view itself, or a subview of the receiving view. Constraints that are added to a view are said to be held by that view. The coordinate system used when evaluating each constraint is the coordinate system of the view that holds the constraint.

When developing for iOS 8.0 or later, use the [`NSLayoutConstraint`](nslayoutconstraint.md) class’s  [`activate(_:)`](nslayoutconstraint/activate(_:).md) method instead of calling the [`addConstraints(_:)`](uiview/addconstraints(_:).md) method directly. The [`activate(_:)`](nslayoutconstraint/activate(_:).md) method automatically adds the constraints to the correct views.

## Parameters

- `constraints`: An array of constraints to be added to the view. All constraints may only reference the view itself or its subviews.

## See Also

- [var constraints: [NSLayoutConstraint]](uiview/constraints.md)
  The constraints held by the view.
- [func addConstraint(NSLayoutConstraint)](uiview/addconstraint(_:).md)
  Adds a constraint on the layout of the receiving view or its subviews.
- [func removeConstraint(NSLayoutConstraint)](uiview/removeconstraint(_:).md)
  Removes the specified constraint from the view.
- [func removeConstraints([NSLayoutConstraint])](uiview/removeconstraints(_:).md)
  Removes the specified constraints from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/addconstraints(_:))*