# translatesAutoresizingMaskIntoConstraints

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the view’s autoresizing mask converts to Auto Layout constraints.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var translatesAutoresizingMaskIntoConstraints: Bool { get set }
```

#### Discussion

If this property’s value is [`true`](https://developer.apple.com/documentation/Swift/true), the system creates a set of constraints that duplicate the behavior specified by the view’s autoresizing mask. You can also modify the view’s size and location using the view’s [`frame`](uiview/frame.md), [`bounds`](uiview/bounds.md), or [`center`](uiview/center.md) properties, creating a static, frame-based layout within Auto Layout.

Because the autoresizing mask constraints specify the view’s size and position, you can’t add constraints to modify this size or position without introducing conflicts. To use Auto Layout to dynamically calculate the size and position of your view, set this property to [`false`](https://developer.apple.com/documentation/Swift/false), and then provide a nonambiguous, nonconflicting set of constraints for the view.

Set this property on a subview from a containing superview or view controller, not from within the view itself:

```swift
customSubview.translatesAutoresizingMaskIntoConstraints = false
```

Don’t set this property on `self` inside a custom view’s own code, because this prevents the containing superview from managing its layout. Don’t modify this property’s value for views that UIKit classes manage, such as [`UITableViewCell`](uitableviewcell.md), [`arrangedSubviews`](uistackview/arrangedsubviews.md), and [`view`](uiviewcontroller/view.md). These classes handle layout automatically, and changing this property interferes with their layout behavior.

By default, the system sets this property to [`true`](https://developer.apple.com/documentation/Swift/true) for any view you programmatically create. If you add views in Interface Builder, the system automatically sets this property to [`false`](https://developer.apple.com/documentation/Swift/false).

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