# init(tabBarSystemItem:tag:)

**Framework**: UIKit  
**Kind**: init

Creates a tab bar item using a system-provided configuration.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(tabBarSystemItem systemItem: UITabBarItem.SystemItem, tag: Int)
```

#### Discussion

You can’t change the [`title`](uibaritem/title.md) and [`image`](uibaritem/image.md) properties of an item this method creates.

## Parameters

- `systemItem`: The preferred system item. For possible values, see  .
- `tag`: An integer you use to identify the object.

## See Also

- [convenience init(title: String?, image: UIImage?, tag: Int)](uitabbaritem/init(title:image:tag:).md)
  Creates a tab bar item that displays a title and an image.
- [convenience init(title: String?, image: UIImage?, selectedImage: UIImage?)](uitabbaritem/init(title:image:selectedimage:).md)
  Creates a tab bar item that toggles the image it displays when its selected state changes.
- [init()](uitabbaritem/init.md)
  Creates a tab bar item with a default configuration.
- [init?(coder: NSCoder)](uitabbaritem/init(coder:).md)
  Creates a tab bar item from a serialized instance.
- [UITabBarItem.SystemItem](uitabbaritem/systemitem.md)
  Constants that represent the system tab bar items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritem/init(tabbarsystemitem:tag:))*