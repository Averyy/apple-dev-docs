# setNeedsUpdateProperties()

**Framework**: UIKit  
**Kind**: method

Call to manually request a properties update for the view controller. Multiple requests may be coalesced into a single update alongside the next layout pass.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
func setNeedsUpdateProperties()
```

## Mentions

- [Updating views automatically with observation tracking](updating-views-automatically-with-observation-tracking.md)

## See Also

- [UIViewController.ViewLoading](uiviewcontroller/viewloading.md)
  A property wrapper that loads the view controller’s view before accessing the property.
- [func updateProperties()](uiviewcontroller/updateproperties.md)
  Configures the view controller’s content and styling properties.
- [func updatePropertiesIfNeeded()](uiviewcontroller/updatepropertiesifneeded.md)
  Forces an immediate properties update for this view controller and its view, including any view controllers and views in this subtree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsupdateproperties())*