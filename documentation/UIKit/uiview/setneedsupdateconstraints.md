# setNeedsUpdateConstraints()

**Framework**: UIKit  
**Kind**: method

Controls whether the view’s constraints need updating.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setNeedsUpdateConstraints()
```

#### Discussion

When a property of your custom view changes in a way that would impact constraints, you can call this method to indicate that the constraints need to be updated at some point in the future. The system will then call [`updateConstraints()`](uiview/updateconstraints().md) as part of its normal layout pass. Use this as an optimization tool to batch constraint changes. Updating constraints all at once just before they are needed ensures that you don’t needlessly recalculate constraints when multiple changes are made to your view in between layout passes.

## See Also

- [func needsUpdateConstraints() -> Bool](uiview/needsupdateconstraints.md)
  A Boolean value that determines whether the view’s constraints need updating.
- [func updateConstraints()](uiview/updateconstraints.md)
  Updates constraints for the view.
- [func updateConstraintsIfNeeded()](uiview/updateconstraintsifneeded.md)
  Updates the constraints for the receiving view and its subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/setneedsupdateconstraints())*