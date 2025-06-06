# layoutMarginsGuide

**Framework**: UIKit  
**Kind**: property

A layout guide representing the view’s margins.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var layoutMarginsGuide: UILayoutGuide { get }
```

#### Discussion

Use this layout guide’s anchors to create constraints with the view’s margin.

## See Also

- [var layoutMargins: UIEdgeInsets](uiview/layoutmargins.md)
  The default spacing to use when laying out content in the view.
- [func addLayoutGuide(UILayoutGuide)](uiview/addlayoutguide(_:).md)
  Adds the specified layout guide to the view.
- [var layoutGuides: [UILayoutGuide]](uiview/layoutguides.md)
  The array of layout guide objects owned by this view.
- [var readableContentGuide: UILayoutGuide](uiview/readablecontentguide.md)
  A layout guide representing an area with a readable width within the view.
- [func removeLayoutGuide(UILayoutGuide)](uiview/removelayoutguide(_:).md)
  Removes the specified layout guide from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/layoutmarginsguide)*