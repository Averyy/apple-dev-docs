# viewDidLayoutSubviews()

**Framework**: UIKit  
**Kind**: method

Notifies the view controller when its view finishes laying out its subviews.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func viewDidLayoutSubviews()
```

## Mentions

- [Displaying and managing views with a view controller](displaying-and-managing-views-with-a-view-controller.md)

#### Discussion

When the bounds change for a view controller’s view, the view adjusts the positions of its subviews and then the system calls this method. However, this method being called  indicate that the individual layouts of the view’s subviews have been adjusted. Each subview is responsible for adjusting its own layout.

Your view controller can override this method to make changes after the view lays out its subviews. The default implementation of this method does nothing.

In iOS 18 and later, UIKit supports automatic trait tracking inside this method for traits from this view controller’s `traitCollection` and the `traitCollection` of its [`view`](uiviewcontroller/view.md). For more information, see [`Automatic trait tracking`](automatic-trait-tracking.md).

## See Also

- [func updateProperties()](uiviewcontroller/updateproperties.md)
  Override point for subclasses to update properties of this view controller or its view. Never call this method directly; use `setNeedsUpdateProperties` to schedule an update.
- [func setNeedsUpdateProperties()](uiviewcontroller/setneedsupdateproperties.md)
  Call to manually request a properties update for the view controller. Multiple requests may be coalesced into a single update alongside the next layout pass.
- [func updatePropertiesIfNeeded()](uiviewcontroller/updatepropertiesifneeded.md)
  Forces an immediate properties update for this view controller and its view, including any view controllers and views in this subtree.
- [func viewWillLayoutSubviews()](uiviewcontroller/viewwilllayoutsubviews.md)
  Notifies the view controller that its view is about to lay out its subviews.
- [func updateViewConstraints()](uiviewcontroller/updateviewconstraints.md)
  Notifies the view controller when its view needs to update its constraints.
- [func updateContentUnavailableConfiguration(using: UIContentUnavailableConfigurationState)](uiviewcontroller/updatecontentunavailableconfiguration(using:).md)
  Updates the content-unavailable configuration for the provided state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/viewdidlayoutsubviews())*