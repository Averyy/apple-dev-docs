# selectedItem

**Framework**: UIKit  
**Kind**: property

The currently selected item on the tab bar.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var selectedItem: UITabBarItem? { get set }
```

#### Discussion

Use this property to get the currently selected item. If you change the value of this property, the tab bar selects the corresponding item and updates the tab bar’s appearance accordingly. Set the property to `nil` to clear the selection.

When an item is selected, the tab bar displays the image in the tab bar item’s [`selectedImage`](uitabbaritem/selectedimage.md) property. If the [`selectedImageTintColor`](uitabbar/selectedimagetintcolor.md) property is set, the tab bar also applies the color in that property to the selected image. To prevent system coloring of an item, provide images using the [`UIImage.RenderingMode.alwaysOriginal`](uiimage/renderingmode-swift.enum/alwaysoriginal.md) rendering mode.

The default value for this property is `nil`.

## See Also

- [var items: [UITabBarItem]?](uitabbar/items.md)
  The items displayed by the tab bar.
- [func setItems([UITabBarItem]?, animated: Bool)](uitabbar/setitems(_:animated:).md)
  Sets the items on the tab bar, optionally animating any changes into position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/selecteditem)*