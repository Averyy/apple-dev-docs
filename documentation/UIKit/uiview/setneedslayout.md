# setNeedsLayout()

**Framework**: UIKit  
**Kind**: method

Invalidates the current layout of the receiver and triggers a layout update during the next update cycle.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func setNeedsLayout()
```

## Mentions

- [Updating views automatically with observation tracking](updating-views-automatically-with-observation-tracking.md)

#### Discussion

Call this method on your application’s main thread when you want to adjust the layout of a view’s subviews. This method makes a note of the request and returns immediately. Because this method does not force an immediate update, but instead waits for the next update cycle, you can use it to invalidate the layout of multiple views before any of those views are updated. This behavior allows you to consolidate all of your layout updates to one update cycle, which is usually better for performance.

## See Also

- [func layoutSubviews()](uiview/layoutsubviews.md)
  Lays out subviews.
- [func layoutIfNeeded()](uiview/layoutifneeded.md)
  Lays out the subviews immediately, if layout updates are pending.
- [class var requiresConstraintBasedLayout: Bool](uiview/requiresconstraintbasedlayout.md)
  A Boolean value that indicates whether the receiver depends on the constraint-based layout system.
- [var translatesAutoresizingMaskIntoConstraints: Bool](uiview/translatesautoresizingmaskintoconstraints.md)
  A Boolean value that determines whether the view’s autoresizing mask is translated into Auto Layout constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/setneedslayout())*