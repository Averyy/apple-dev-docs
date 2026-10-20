# UITableViewRowAction.Style

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the appearance of action buttons.

**Availability**:
- iOS 8.0+ - Deprecated in 13.0
- iPadOS 8.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UITableViewRowAction`](../uitableviewrowaction.md).

## Declaration

```swift
enum Style
```

```c
enum UITableViewRowActionStyle : NSInteger;
```

## Topics

### Styles
- [UITableViewRowAction.Style.default](./style-swift.enum/default.md)
  Apply the default style to the button.
- [static var destructive: UITableViewRowAction.Style](./style-swift.enum/destructive.md)
  Equal to the default style.
- [UITableViewRowAction.Style.normal](./style-swift.enum/normal.md)
  Apply a style that reflects standard non-destructive actions.
### Initializers
- [init?(rawValue: Int)](./style-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the action’s appearance
- [var style: UITableViewRowAction.Style](./style-swift.property.md)
  The style applied to the action button.
- [var title: String?](./title.md)
  The title of the action button.
- [var backgroundColor: UIColor?](./backgroundcolor.md)
  The background color of the action button.
- [var backgroundEffect: UIVisualEffect?](./backgroundeffect.md)
  The visual effect to apply to the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewrowaction/style-swift.enum)*