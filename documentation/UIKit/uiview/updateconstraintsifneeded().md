# updateConstraintsIfNeeded()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Updates the constraints for the receiving view and its subviews.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func updateConstraintsIfNeeded()
```

```objc
- (void) updateConstraintsIfNeeded;
```

## Discussion

Whenever a new layout pass is triggered for a view, the system invokes this method to ensure that any constraints for the view and its subviews are updated with information from the current view hierarchy and its constraints. This method is called automatically by the system, but may be invoked manually if you need to examine the most up to date constraints.

Subclasses should not override this method.

## See Also

### Triggering Auto Layout
- [func needsUpdateConstraints() -> Bool](./needsupdateconstraints%28%29.md)
  A Boolean value that determines whether the view’s constraints need updating.
- [func setNeedsUpdateConstraints()](./setneedsupdateconstraints%28%29.md)
  Controls whether the view’s constraints need updating.
- [func updateConstraints()](./updateconstraints%28%29.md)
  Updates constraints for the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/updateconstraintsifneeded())*