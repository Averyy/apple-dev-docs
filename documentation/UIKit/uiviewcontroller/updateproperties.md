# updateProperties()

**Framework**: UIKit  
**Kind**: method

Configures the view controller’s content and styling properties.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
func updateProperties()
```

## Mentions

- [Updating views automatically with observation tracking](updating-views-automatically-with-observation-tracking.md)

#### Overview

Override this method to configure the view’s content and styling in your view controller subclass. Don’t call this method directly; instead, call [`setNeedsUpdateProperties()`](uiviewcontroller/setneedsupdateproperties().md) to schedule an update.

This method supports automatic observation tracking. For more information, see [`Updating views automatically with observation tracking`](updating-views-automatically-with-observation-tracking.md).

## See Also

- [func viewWillLayoutSubviews()](uiviewcontroller/viewwilllayoutsubviews.md)
  Notifies the view controller that its view is about to lay out its subviews.
- [func viewDidLayoutSubviews()](uiviewcontroller/viewdidlayoutsubviews.md)
  Notifies the view controller when its view finishes laying out its subviews.
- [func updateViewConstraints()](uiviewcontroller/updateviewconstraints.md)
  Notifies the view controller when its view needs to update its constraints.
- [func updateContentUnavailableConfiguration(using: UIContentUnavailableConfigurationState)](uiviewcontroller/updatecontentunavailableconfiguration(using:).md)
  Updates the content-unavailable configuration for the provided state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/updateproperties())*