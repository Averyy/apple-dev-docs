# updateContentUnavailableConfiguration(using:)

**Framework**: UIKit  
**Kind**: method

Updates the content-unavailable configuration for the provided state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@objc(_bridgedUpdateContentUnavailableConfigurationUsingState:) @preconcurrency dynamic func updateContentUnavailableConfiguration(using state: UIContentUnavailableConfigurationState)
```

#### Discussion

Override this method to update the value of [`contentUnavailableConfiguration`](uiviewcontroller/contentunavailableconfiguration-4b95e.md) as appropriate for the given state.

Don’t call this method directly. Instead, call [`setNeedsUpdateContentUnavailableConfiguration()`](uiviewcontroller/setneedsupdatecontentunavailableconfiguration().md) to tell the system to request an update.

In iOS 18 and later, UIKit supports automatic trait tracking inside this method for traits from this view controller’s `traitCollection` and the `traitCollection` of its [`view`](uiviewcontroller/view.md). For more information, see [`Automatic trait tracking`](automatic-trait-tracking.md).

## Parameters

- `state`: The current configuration state for a content-unavailable view.

## See Also

- [func updateProperties()](uiviewcontroller/updateproperties.md)
  Override point for subclasses to update properties of this view controller or its view. Never call this method directly; use `setNeedsUpdateProperties` to schedule an update.
- [func setNeedsUpdateProperties()](uiviewcontroller/setneedsupdateproperties.md)
  Call to manually request a properties update for the view controller. Multiple requests may be coalesced into a single update alongside the next layout pass.
- [func updatePropertiesIfNeeded()](uiviewcontroller/updatepropertiesifneeded.md)
  Forces an immediate properties update for this view controller and its view, including any view controllers and views in this subtree.
- [func viewWillLayoutSubviews()](uiviewcontroller/viewwilllayoutsubviews.md)
  Notifies the view controller that its view is about to lay out its subviews.
- [func viewDidLayoutSubviews()](uiviewcontroller/viewdidlayoutsubviews.md)
  Notifies the view controller when its view finishes laying out its subviews.
- [func updateViewConstraints()](uiviewcontroller/updateviewconstraints.md)
  Notifies the view controller when its view needs to update its constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/updatecontentunavailableconfiguration(using:))*