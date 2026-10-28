# requiresConstraintBasedLayout

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether the receiver depends on the constraint-based layout system.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
class var requiresConstraintBasedLayout: Bool { get }
```

```objc
@property (class, nonatomic, readonly) BOOL requiresConstraintBasedLayout;
```

## Return Value

[`true`](../../Swift/true.md) if the view must be in a window using constraint-based layout to function properly, [`false`](../../Swift/false.md) otherwise.

## Discussion

Custom views should override this to return [`true`](../../Swift/true.md) if they cannot layout correctly using autoresizing.

## See Also

### Laying out subviews
- [func layoutSubviews()](./layoutsubviews%28%29.md)
  Lays out subviews.
- [func setNeedsLayout()](./setneedslayout%28%29.md)
  Invalidates the current layout of the receiver and triggers a layout update during the next update cycle.
- [func layoutIfNeeded()](./layoutifneeded%28%29.md)
  Lays out the subviews immediately, if layout updates are pending.
- [var translatesAutoresizingMaskIntoConstraints: Bool](./translatesautoresizingmaskintoconstraints.md)
  A Boolean value that determines whether the view’s autoresizing mask converts to Auto Layout constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/requiresconstraintbasedlayout)*