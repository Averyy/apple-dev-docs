# updateConstraints()

**Framework**: UIKit  
**Kind**: method

Updates constraints for the view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func updateConstraints()
```

#### Discussion

Override this method to optimize changes to your constraints.

> **Note**:  It’s almost always cleaner and easier to update a constraint immediately after the affecting change has occurred. For example, if you want to change a constraint in response to a button tap, make that change directly in the button’s action method. You should only override this method when changing constraints in place is too slow, or when a view is producing a number of redundant changes.

To schedule a change, call [`setNeedsUpdateConstraints()`](uiview/setneedsupdateconstraints().md) on the view. The system then calls your implementation of [`updateConstraints()`](uiview/updateconstraints().md) before the layout occurs. This lets you verify that all necessary constraints for your content are in place at a time when your custom view’s properties aren’t changing.

Your implementation must be as efficient as possible. Don’t deactivate all your constraints, then reactivate the ones you need. Instead, your app must have some way of tracking your constraints, and validating them during each update pass. Only change items that need to be changed. During each update pass, you must ensure that you have the appropriate constraints for the app’s current state.

Don’t call [`setNeedsUpdateConstraints()`](uiview/setneedsupdateconstraints().md) inside your implementation. Calling [`setNeedsUpdateConstraints()`](uiview/setneedsupdateconstraints().md) schedules another update pass, creating a feedback loop.

> ❗ **Important**:  Call `[super updateConstraints]` as the final step in your implementation.

In iOS 18 and later, UIKit supports automatic trait tracking inside this method for traits from this view’s `traitCollection`. For more information, see [`Automatic trait tracking`](automatic-trait-tracking.md).

## See Also

- [func updateProperties()](uiview/updateproperties.md)
  Override point for subclasses to update properties of this view. Never call this method directly; use `setNeedsUpdateProperties` to schedule an update.
- [func setNeedsUpdateProperties()](uiview/setneedsupdateproperties.md)
  Call to manually request a properties update for the view. Multiple requests may be coalesced into a single update alongside the next layout pass.
- [func updatePropertiesIfNeeded()](uiview/updatepropertiesifneeded.md)
  Forces an immediate properties update for this view (and its view controller, if applicable) and any subviews, including any view controllers or views in its subtree.
- [func layoutSubviews()](uiview/layoutsubviews.md)
  Lays out subviews.
- [func draw(CGRect)](uiview/draw(_:).md)
  Draws the view’s image within the passed-in rectangle.
- [UIView.Invalidations.Properties](uiview/invalidations/properties.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/updateconstraints())*