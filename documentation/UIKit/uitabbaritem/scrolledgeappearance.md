# scrollEdgeAppearance

**Framework**: UIKit  
**Kind**: property

The appearance settings for the tab bar when the edge of scrollable content aligns with the edge of the tab bar.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var scrollEdgeAppearance: UITabBarAppearance? { get set }
```

#### Discussion

When a tab bar displays the selected item, the appearance setting in this property overrides the settings in the [`scrollEdgeAppearance`](uitoolbar/scrolledgeappearance.md) property of [`UIToolbar`](uitoolbar.md).

Use this property to apply a scroll edge appearance based on the tab bar item stored in the [`selectedItem`](uitabbar/selecteditem.md) property. If the selected item’s [`scrollEdgeAppearance`](uitabbaritem/scrolledgeappearance.md) property is `nil`, UIKit uses the tab bar’s scroll edge appearance.

## See Also

- [var selectedImage: UIImage?](uitabbaritem/selectedimage.md)
  The source image the item uses to generate its selected image.
- [var standardAppearance: UITabBarAppearance?](uitabbaritem/standardappearance.md)
  The appearance settings for a tab bar.
- [var titlePositionAdjustment: UIOffset](uitabbaritem/titlepositionadjustment.md)
  The offset to apply to the title’s position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritem/scrolledgeappearance)*