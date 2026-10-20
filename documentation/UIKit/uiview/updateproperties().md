# updateProperties()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Configures the view’s content and styling properties before layout.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func updateProperties()
```

```objc
- (void) updateProperties;
```

## Mentions

- [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md)

#### Overview

Override this method to configure content and styling in your view subclass. Don’t call this method directly; instead, call [`setNeedsUpdateProperties()`](./setneedsupdateproperties%28%29.md) to schedule an update.

This method supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md).

## See Also

### Observing data in views
- [func layoutSubviews()](./layoutsubviews%28%29.md)
  Lays out subviews.
- [func updateConstraints()](./updateconstraints%28%29.md)
  Updates constraints for the view.
- [func draw(CGRect)](./draw%28_%29.md)
  Draws the view’s image within the passed-in rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/updateproperties())*