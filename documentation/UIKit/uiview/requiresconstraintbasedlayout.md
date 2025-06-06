# requiresConstraintBasedLayout

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the receiver depends on the constraint-based layout system.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class var requiresConstraintBasedLayout: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the view must be in a window using constraint-based layout to function properly, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

Custom views should override this to return [`true`](https://developer.apple.com/documentation/swift/true) if they cannot layout correctly using autoresizing.

## See Also

- [func layoutSubviews()](uiview/layoutsubviews.md)
  Lays out subviews.
- [func setNeedsLayout()](uiview/setneedslayout.md)
  Invalidates the current layout of the receiver and triggers a layout update during the next update cycle.
- [func layoutIfNeeded()](uiview/layoutifneeded.md)
  Lays out the subviews immediately, if layout updates are pending.
- [var translatesAutoresizingMaskIntoConstraints: Bool](uiview/translatesautoresizingmaskintoconstraints.md)
  A Boolean value that determines whether the view’s autoresizing mask is translated into Auto Layout constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/requiresconstraintbasedlayout)*