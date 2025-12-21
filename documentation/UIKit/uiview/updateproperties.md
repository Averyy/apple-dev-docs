# updateProperties()

**Framework**: UIKit  
**Kind**: method

Configures the view’s content and styling properties before layout.

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

Override this method to configure content and styling in your view subclass. Don’t call this method directly; instead, call [`setNeedsUpdateProperties()`](uiview/setneedsupdateproperties().md) to schedule an update.

This method supports automatic observation tracking. For more information, see [`Updating views automatically with observation tracking`](updating-views-automatically-with-observation-tracking.md).

## See Also

- [func layoutSubviews()](uiview/layoutsubviews.md)
  Lays out subviews.
- [func updateConstraints()](uiview/updateconstraints.md)
  Updates constraints for the view.
- [func draw(CGRect)](uiview/draw(_:).md)
  Draws the view’s image within the passed-in rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/updateproperties())*