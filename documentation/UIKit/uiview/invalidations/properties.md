# UIView.Invalidations.Properties

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS
- Swift 5.1+

## Declaration

```swift
struct Properties
```

## Topics

### Initializers
- [init()](./properties/init%28%29.md)

## Relationships

### Conforms To
- [UIViewInvalidating](../../uiviewinvalidating.md)

## See Also

### Views
- [func updateProperties()](../updateproperties%28%29.md)
  Configures the view’s content and styling properties before layout.
- [func setNeedsUpdateProperties()](../setneedsupdateproperties%28%29.md)
  Call to manually request a properties update for the view. Multiple requests may be coalesced into a single update alongside the next layout pass.
- [func updatePropertiesIfNeeded()](../updatepropertiesifneeded%28%29.md)
  Forces an immediate properties update for this view (and its view controller, if applicable) and any subviews, including any view controllers or views in its subtree.
- [func layoutSubviews()](../layoutsubviews%28%29.md)
  Lays out subviews.
- [func updateConstraints()](../updateconstraints%28%29.md)
  Updates constraints for the view.
- [func draw(CGRect)](../draw%28_%29.md)
  Draws the view’s image within the passed-in rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/invalidations/properties)*