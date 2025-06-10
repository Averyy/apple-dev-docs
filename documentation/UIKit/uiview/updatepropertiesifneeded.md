# updatePropertiesIfNeeded()

**Framework**: UIKit  
**Kind**: method

Forces an immediate properties update for this view (and its view controller, if applicable) and any subviews, including any view controllers or views in its subtree.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
func updatePropertiesIfNeeded()
```

## See Also

- [func updateProperties()](uiview/updateproperties.md)
  Override point for subclasses to update properties of this view. Never call this method directly; use `setNeedsUpdateProperties` to schedule an update.
- [func setNeedsUpdateProperties()](uiview/setneedsupdateproperties.md)
  Call to manually request a properties update for the view. Multiple requests may be coalesced into a single update alongside the next layout pass.
- [func layoutSubviews()](uiview/layoutsubviews.md)
  Lays out subviews.
- [func updateConstraints()](uiview/updateconstraints.md)
  Updates constraints for the view.
- [func draw(CGRect)](uiview/draw(_:).md)
  Draws the view’s image within the passed-in rectangle.
- [UIView.Invalidations.Properties](uiview/invalidations/properties.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/updatepropertiesifneeded())*