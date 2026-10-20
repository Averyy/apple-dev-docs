# needsUpdateConstraints()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

A Boolean value that determines whether the view’s constraints need updating.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func needsUpdateConstraints() -> Bool
```

```objc
- (BOOL) needsUpdateConstraints;
```

#### Return Value

[`true`](../../Swift/true.md) if the view’s constraints need updating, [`false`](../../Swift/false.md) otherwise.

#### Discussion

The constraint-based layout system uses the return value of this method to determine whether it needs to call [`updateConstraints()`](./updateconstraints%28%29.md) on your view as part of its normal layout pass.

## See Also

### Triggering Auto Layout
- [func setNeedsUpdateConstraints()](./setneedsupdateconstraints%28%29.md)
  Controls whether the view’s constraints need updating.
- [func updateConstraints()](./updateconstraints%28%29.md)
  Updates constraints for the view.
- [func updateConstraintsIfNeeded()](./updateconstraintsifneeded%28%29.md)
  Updates the constraints for the receiving view and its subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/needsupdateconstraints())*