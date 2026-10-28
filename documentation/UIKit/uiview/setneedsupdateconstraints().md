# setNeedsUpdateConstraints()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Controls whether the view’s constraints need updating.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setNeedsUpdateConstraints()
```

```objc
- (void) setNeedsUpdateConstraints;
```

## Discussion

When a property of your custom view changes in a way that would impact constraints, you can call this method to indicate that the constraints need to be updated at some point in the future. The system will then call [`updateConstraints()`](./updateconstraints%28%29.md) as part of its normal layout pass. Use this as an optimization tool to batch constraint changes. Updating constraints all at once just before they are needed ensures that you don’t needlessly recalculate constraints when multiple changes are made to your view in between layout passes.

## See Also

### Triggering Auto Layout
- [func needsUpdateConstraints() -> Bool](./needsupdateconstraints%28%29.md)
  A Boolean value that determines whether the view’s constraints need updating.
- [func updateConstraints()](./updateconstraints%28%29.md)
  Updates constraints for the view.
- [func updateConstraintsIfNeeded()](./updateconstraintsifneeded%28%29.md)
  Updates the constraints for the receiving view and its subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/setneedsupdateconstraints())*