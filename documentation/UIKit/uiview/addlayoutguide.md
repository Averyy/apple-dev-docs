# addLayoutGuide(_:)

**Framework**: UIKit  
**Kind**: method

Adds the specified layout guide to the view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addLayoutGuide(_ layoutGuide: UILayoutGuide)
```

#### Discussion

This method adds the specified layout guide to the end of the view’s [`layoutGuides`](uiview/layoutguides.md) array. It also assigns the view to the guide’s [`owningView`](uilayoutguide/owningview.md) property. Each guide can have only one owning view.

After the guide has been added to a view, it can participate in Auto Layout constraints with that view’s hierarchy.

## Parameters

- `layoutGuide`: The layout guide to be added.

## See Also

- [var layoutGuides: [UILayoutGuide]](uiview/layoutguides.md)
  The array of layout guide objects owned by this view.
- [var layoutMarginsGuide: UILayoutGuide](uiview/layoutmarginsguide.md)
  A layout guide representing the view’s margins.
- [var readableContentGuide: UILayoutGuide](uiview/readablecontentguide.md)
  A layout guide representing an area with a readable width within the view.
- [func removeLayoutGuide(UILayoutGuide)](uiview/removelayoutguide(_:).md)
  Removes the specified layout guide from the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/addlayoutguide(_:))*