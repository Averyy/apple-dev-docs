# UITabBarItem.SystemItem

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that represent the system tab bar items.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum SystemItem
```

```c
enum UITabBarSystemItem : NSInteger;
```

## Topics

### System items
- [UITabBarItem.SystemItem.bookmarks](./systemitem/bookmarks.md)
  The bookmarks system item.
- [UITabBarItem.SystemItem.contacts](./systemitem/contacts.md)
  The contacts system item.
- [UITabBarItem.SystemItem.downloads](./systemitem/downloads.md)
  The downloads system item.
- [UITabBarItem.SystemItem.favorites](./systemitem/favorites.md)
  The favorites system item.
- [UITabBarItem.SystemItem.featured](./systemitem/featured.md)
  The featured system item.
- [UITabBarItem.SystemItem.history](./systemitem/history.md)
  The history system item.
- [UITabBarItem.SystemItem.more](./systemitem/more.md)
  The more system item.
- [UITabBarItem.SystemItem.mostRecent](./systemitem/mostrecent.md)
  The most recent system item.
- [UITabBarItem.SystemItem.mostViewed](./systemitem/mostviewed.md)
  The most viewed system item.
- [UITabBarItem.SystemItem.recents](./systemitem/recents.md)
  The recents system item.
- [UITabBarItem.SystemItem.search](./systemitem/search.md)
  The search system item.
- [UITabBarItem.SystemItem.topRated](./systemitem/toprated.md)
  The top rated system item.
### Initializers
- [init?(rawValue: Int)](./systemitem/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a tab bar item
- [convenience init(tabBarSystemItem: UITabBarItem.SystemItem, tag: Int)](./init%28tabbarsystemitem,tag%29.md)
  Creates a tab bar item using a system-provided configuration.
- [convenience init(title: String?, image: UIImage?, tag: Int)](./init%28title,image,tag%29.md)
  Creates a tab bar item that displays a title and an image.
- [convenience init(title: String?, image: UIImage?, selectedImage: UIImage?)](./init%28title,image,selectedimage%29.md)
  Creates a tab bar item that toggles the image it displays when its selected state changes.
- [init()](./init%28%29.md)
  Creates a tab bar item with a default configuration.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a tab bar item from a serialized instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritem/systemitem)*