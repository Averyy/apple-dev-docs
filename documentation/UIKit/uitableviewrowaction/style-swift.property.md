# style

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The style applied to the action button.

**Availability**:
- iOS 8.0+ - Deprecated in 13.0
- iPadOS 8.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UITableViewRowAction`](../uitableviewrowaction.md).

## Declaration

```swift
var style: UITableViewRowAction.Style { get }
```

```objc
@property (nonatomic, readonly) UITableViewRowActionStyle style;
```

#### Discussion

The value of this property is set at creation time and can’t be changed later.

## See Also

### Configuring the action’s appearance
- [UITableViewRowAction.Style](./style-swift.enum.md)
  Constants that specify the appearance of action buttons.
- [var title: String?](./title.md)
  The title of the action button.
- [var backgroundColor: UIColor?](./backgroundcolor.md)
  The background color of the action button.
- [var backgroundEffect: UIVisualEffect?](./backgroundeffect.md)
  The visual effect to apply to the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewrowaction/style-swift.property)*