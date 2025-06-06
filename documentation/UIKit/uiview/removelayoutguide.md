# removeLayoutGuide(_:)

**Framework**: UIKit  
**Kind**: method

Removes the specified layout guide from the view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func removeLayoutGuide(_ layoutGuide: UILayoutGuide)
```

#### Discussion

This method removes the layout guide from the view’s [`layoutGuides`](uiview/layoutguides.md) array and sets the guide’s [`owningView`](uilayoutguide/owningview.md) property to `nil`. It also removes any constraints to the layout guide.

Layout guides cannot participate in Auto Layout constraints unless they are added to a view in the view hierarchy.

## Parameters

- `layoutGuide`: The layout guide to be removed.

## See Also

- [func addLayoutGuide(UILayoutGuide)](uiview/addlayoutguide(_:).md)
  Adds the specified layout guide to the view.
- [var layoutGuides: [UILayoutGuide]](uiview/layoutguides.md)
  The array of layout guide objects owned by this view.
- [var layoutMarginsGuide: UILayoutGuide](uiview/layoutmarginsguide.md)
  A layout guide representing the view’s margins.
- [var readableContentGuide: UILayoutGuide](uiview/readablecontentguide.md)
  A layout guide representing an area with a readable width within the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/removelayoutguide(_:))*