# UIView.Invalidations.Properties

**Framework**: UIKit  
**Kind**: struct

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- tvOS 26.0+ (Beta)
- visionOS ?+
- Swift 5.1+

## Declaration

```swift
struct Properties
```

## Topics

### Initializers
- [init()](uiview/invalidations/properties/init.md)

## Relationships

### Conforms To
- [UIViewInvalidating](uiviewinvalidating.md)

## See Also

- [func updateProperties()](uiview/updateproperties.md)
  Override point for subclasses to update properties of this view. Never call this method directly; use `setNeedsUpdateProperties` to schedule an update.
- [func setNeedsUpdateProperties()](uiview/setneedsupdateproperties.md)
  Call to manually request a properties update for the view. Multiple requests may be coalesced into a single update alongside the next layout pass.
- [func updatePropertiesIfNeeded()](uiview/updatepropertiesifneeded.md)
  Forces an immediate properties update for this view (and its view controller, if applicable) and any subviews, including any view controllers or views in its subtree.
- [func layoutSubviews()](uiview/layoutsubviews.md)
  Lays out subviews.
- [func updateConstraints()](uiview/updateconstraints.md)
  Updates constraints for the view.
- [func draw(CGRect)](uiview/draw(_:).md)
  Draws the view’s image within the passed-in rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/invalidations/properties)*