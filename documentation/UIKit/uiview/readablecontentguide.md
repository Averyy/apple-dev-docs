# readableContentGuide

**Framework**: UIKit  
**Kind**: property

A layout guide representing an area with a readable width within the view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var readableContentGuide: UILayoutGuide { get }
```

#### Discussion

This layout guide defines an area that can easily be read without forcing users to move their head to track the lines. The readable content area follows the following rules:

1. The readable content guide never extends beyond the view’s layout margin guide.
2. The readable content guide is vertically centered inside the layout margin guide.
3. The readable content guide’s width is equal to or less than the readable width defined for the current dynamic text size.

Use the readable content guide to lay out a single column of text. If you are laying out multiple columns, you can use the guide’s width to determine the optimal width for your columns.

## See Also

- [func addLayoutGuide(UILayoutGuide)](uiview/addlayoutguide(_:).md)
  Adds the specified layout guide to the view.
- [var layoutGuides: [UILayoutGuide]](uiview/layoutguides.md)
  The array of layout guide objects owned by this view.
- [var layoutMarginsGuide: UILayoutGuide](uiview/layoutmarginsguide.md)
  A layout guide representing the view’s margins.
- [func removeLayoutGuide(UILayoutGuide)](uiview/removelayoutguide(_:).md)
  Removes the specified layout guide from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/readablecontentguide)*