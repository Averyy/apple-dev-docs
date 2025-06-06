# needsUpdateConstraints()

**Framework**: UIKit  
**Kind**: method

A Boolean value that determines whether the view’s constraints need updating.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func needsUpdateConstraints() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the view’s constraints need updating, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

The constraint-based layout system uses the return value of this method to determine whether it needs to call [`updateConstraints()`](uiview/updateconstraints().md) on your view as part of its normal layout pass.

## See Also

- [func setNeedsUpdateConstraints()](uiview/setneedsupdateconstraints.md)
  Controls whether the view’s constraints need updating.
- [func updateConstraints()](uiview/updateconstraints.md)
  Updates constraints for the view.
- [func updateConstraintsIfNeeded()](uiview/updateconstraintsifneeded.md)
  Updates the constraints for the receiving view and its subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/needsupdateconstraints())*