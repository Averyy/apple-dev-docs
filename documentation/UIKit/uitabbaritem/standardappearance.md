# standardAppearance

**Framework**: UIKit  
**Kind**: property

The appearance settings for a tab bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var standardAppearance: UITabBarAppearance? { get set }
```

#### Discussion

When a tab bar displays the selected item, the appearance setting in this property overrides the settings in the [`standardAppearance`](uitabbar/standardappearance.md) property of [`UITabBar`](uitabbar.md).

Use this property to apply a tab bar appearance based on the tab bar item stored in the [`selectedItem`](uitabbar/selecteditem.md) property. If the selected item’s [`standardAppearance`](uitabbaritem/standardappearance.md) property is `nil`, UIKit uses the tab bar’s standard appearance.

## See Also

- [var selectedImage: UIImage?](uitabbaritem/selectedimage.md)
  The source image the item uses to generate its selected image.
- [var scrollEdgeAppearance: UITabBarAppearance?](uitabbaritem/scrolledgeappearance.md)
  The appearance settings for the tab bar when the edge of scrollable content aligns with the edge of the tab bar.
- [var titlePositionAdjustment: UIOffset](uitabbaritem/titlepositionadjustment.md)
  The offset to apply to the title’s position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritem/standardappearance)*