# removeConstraints(_:)

**Framework**: UIKit  
**Kind**: method

Removes the specified constraints from the view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func removeConstraints(_ constraints: [NSLayoutConstraint])
```

#### Discussion

When developing for iOS 8.0 or later, use the [`NSLayoutConstraint`](nslayoutconstraint.md) class’s  [`deactivate(_:)`](nslayoutconstraint/deactivate(_:).md) method instead of calling the [`removeConstraints(_:)`](uiview/removeconstraints(_:).md) method directly. The [`deactivate(_:)`](nslayoutconstraint/deactivate(_:).md) method automatically removes the constraints from the correct views.

## Parameters

- `constraints`: The constraints to remove.

## See Also

- [var constraints: [NSLayoutConstraint]](uiview/constraints.md)
  The constraints held by the view.
- [func addConstraint(NSLayoutConstraint)](uiview/addconstraint(_:).md)
  Adds a constraint on the layout of the receiving view or its subviews.
- [func addConstraints([NSLayoutConstraint])](uiview/addconstraints(_:).md)
  Adds multiple constraints on the layout of the receiving view or its subviews.
- [func removeConstraint(NSLayoutConstraint)](uiview/removeconstraint(_:).md)
  Removes the specified constraint from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/removeconstraints(_:))*