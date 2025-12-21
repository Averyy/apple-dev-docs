# removeConstraint(_:)

**Framework**: UIKit  
**Kind**: method

Removes the specified constraint from the view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func removeConstraint(_ constraint: NSLayoutConstraint)
```

#### Discussion

When developing for iOS 8.0 or later, set the constraint’s [`isActive`](nslayoutconstraint/isactive.md) property to [`false`](https://developer.apple.com/documentation/Swift/false) instead of calling the [`removeConstraint(_:)`](uiview/removeconstraint(_:).md) method directly. The [`isActive`](nslayoutconstraint/isactive.md) property automatically adds and removes the constraint from the correct view.

## Parameters

- `constraint`: The constraint to remove. Removing a constraint not held by the view has no effect.

## See Also

- [var constraints: [NSLayoutConstraint]](uiview/constraints.md)
  The constraints held by the view.
- [func addConstraint(NSLayoutConstraint)](uiview/addconstraint(_:).md)
  Adds a constraint on the layout of the receiving view or its subviews.
- [func addConstraints([NSLayoutConstraint])](uiview/addconstraints(_:).md)
  Adds multiple constraints on the layout of the receiving view or its subviews.
- [func removeConstraints([NSLayoutConstraint])](uiview/removeconstraints(_:).md)
  Removes the specified constraints from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/removeconstraint(_:))*