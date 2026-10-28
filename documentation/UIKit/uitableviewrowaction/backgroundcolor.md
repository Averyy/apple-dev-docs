# backgroundColor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The background color of the action button.

**Availability**:
- iOS 8.0+ - Deprecated in 13.0
- iPadOS 8.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UITableViewRowAction`](../uitableviewrowaction.md).

## Declaration

```swift
@NSCopying
var backgroundColor: UIColor? { get set }
```

```objc
@property (nonatomic, copy, nullable) UIColor * backgroundColor;
```

## Discussion

Use this property to specify the background color for your button. If you don’t specify a value for this property, UIKit assigns a default color based on the value in the [`style`](./style-swift.property.md) property.

## See Also

### Configuring the action’s appearance
- [var style: UITableViewRowAction.Style](./style-swift.property.md)
  The style applied to the action button.
- [UITableViewRowAction.Style](./style-swift.enum.md)
  Constants that specify the appearance of action buttons.
- [var title: String?](./title.md)
  The title of the action button.
- [var backgroundEffect: UIVisualEffect?](./backgroundeffect.md)
  The visual effect to apply to the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewrowaction/backgroundcolor)*