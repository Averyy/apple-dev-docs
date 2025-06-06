# exerciseAmbiguityInLayout()

**Framework**: UIKit  
**Kind**: method

Randomly changes the frame of a view with an ambiguous layout between the different valid values.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func exerciseAmbiguityInLayout()
```

#### Discussion

This method randomly changes the frame of a view with an ambiguous layout between its different valid values, causing the view to move in the interface. This makes it easy to visually identify what the valid frames are and may enable the developer to discern what constraints need to be added to the layout to fully specify a location for the view.

This method should only be used for debugging constraint-based layout. No application should ship with calls to this method as part of its operation.

## See Also

- [func constraintsAffectingLayout(for: NSLayoutConstraint.Axis) -> [NSLayoutConstraint]](uiview/constraintsaffectinglayout(for:).md)
  Returns the constraints impacting the layout of the view for a given axis.
- [var hasAmbiguousLayout: Bool](uiview/hasambiguouslayout.md)
  A Boolean value that determines whether the constraints impacting the layout of the view incompletely specify the location of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/exerciseambiguityinlayout())*