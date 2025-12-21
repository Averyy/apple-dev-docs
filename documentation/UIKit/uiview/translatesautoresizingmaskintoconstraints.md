# translatesAutoresizingMaskIntoConstraints

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the view’s autoresizing mask is translated into Auto Layout constraints.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var translatesAutoresizingMaskIntoConstraints: Bool { get set }
```

#### Discussion

If this property’s value is [`true`](https://developer.apple.com/documentation/Swift/true), the system creates a set of constraints that duplicate the behavior specified by the view’s autoresizing mask. This also lets you modify the view’s size and location using the view’s [`frame`](uiview/frame.md), [`bounds`](uiview/bounds.md), or [`center`](uiview/center.md) properties, allowing you to create a static, frame-based layout within Auto Layout.

Note that the autoresizing mask constraints fully specify the view’s size and position; therefore, you cannot add additional constraints to modify this size or position without introducing conflicts. If you want to use Auto Layout to dynamically calculate the size and position of your view, you must set this property to [`false`](https://developer.apple.com/documentation/Swift/false), and then provide a non ambiguous, nonconflicting set of constraints for the view.

By default, the property is set to [`true`](https://developer.apple.com/documentation/Swift/true) for any view you programmatically create. If you add views in Interface Builder, the system automatically sets this property to [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func layoutSubviews()](uiview/layoutsubviews.md)
  Lays out subviews.
- [func setNeedsLayout()](uiview/setneedslayout.md)
  Invalidates the current layout of the receiver and triggers a layout update during the next update cycle.
- [func layoutIfNeeded()](uiview/layoutifneeded.md)
  Lays out the subviews immediately, if layout updates are pending.
- [class var requiresConstraintBasedLayout: Bool](uiview/requiresconstraintbasedlayout.md)
  A Boolean value that indicates whether the receiver depends on the constraint-based layout system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/translatesautoresizingmaskintoconstraints)*