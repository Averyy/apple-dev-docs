# setNeedsUpdateProperties()

**Framework**: UIKit  
**Kind**: method

Call to manually request a properties update for the view controller. Multiple requests may be coalesced into a single update alongside the next layout pass.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
func setNeedsUpdateProperties()
```

## See Also

- [func updateProperties()](uiviewcontroller/updateproperties.md)
  Override point for subclasses to update properties of this view controller or its view. Never call this method directly; use `setNeedsUpdateProperties` to schedule an update.
- [func updatePropertiesIfNeeded()](uiviewcontroller/updatepropertiesifneeded.md)
  Forces an immediate properties update for this view controller and its view, including any view controllers and views in this subtree.
- [func viewWillLayoutSubviews()](uiviewcontroller/viewwilllayoutsubviews.md)
  Notifies the view controller that its view is about to lay out its subviews.
- [func viewDidLayoutSubviews()](uiviewcontroller/viewdidlayoutsubviews.md)
  Notifies the view controller when its view finishes laying out its subviews.
- [func updateViewConstraints()](uiviewcontroller/updateviewconstraints.md)
  Notifies the view controller when its view needs to update its constraints.
- [func updateContentUnavailableConfiguration(using: UIContentUnavailableConfigurationState)](uiviewcontroller/updatecontentunavailableconfiguration(using:).md)
  Updates the content-unavailable configuration for the provided state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsupdateproperties())*