# init(title:image:selectedImage:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a tab bar item that toggles the image it displays when its selected state changes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
convenience init(title: String?, image: UIImage?, selectedImage: UIImage?)
```

```objc
- (instancetype) initWithTitle:(NSString *) title image:(UIImage *) image selectedImage:(UIImage *) selectedImage;
```

#### Discussion

Use `nil` for `title` or `image` if you don’t want to display that element.

If you don’t provide `selectedImage`, the item uses `image` for both selection states. The item creates the images it displays from the alpha values in the source images. To prevent system tinting, use images with the [`UIImage.RenderingMode.alwaysOriginal`](../uiimage/renderingmode-swift.enum/alwaysoriginal.md) rendering mode. The item clips any image that’s larger than its bounds.

## Parameters

- `title`: The item’s title.
- `image`: The item’s source image.
- `selectedImage`: The source image the item uses when the user selects it.

## See Also

### Creating a tab bar item
- [convenience init(tabBarSystemItem: UITabBarItem.SystemItem, tag: Int)](./init%28tabbarsystemitem,tag%29.md)
  Creates a tab bar item using a system-provided configuration.
- [convenience init(title: String?, image: UIImage?, tag: Int)](./init%28title,image,tag%29.md)
  Creates a tab bar item that displays a title and an image.
- [init()](./init%28%29.md)
  Creates a tab bar item with a default configuration.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a tab bar item from a serialized instance.
- [UITabBarItem.SystemItem](./systemitem.md)
  Constants that represent the system tab bar items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritem/init(title:image:selectedimage:))*