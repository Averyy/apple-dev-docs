# backgroundEffect

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The visual effect to apply to the button.

**Availability**:
- iOS 8.0+ - Deprecated in 13.0
- iPadOS 8.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UITableViewRowAction`](../uitableviewrowaction.md).

## Declaration

```swift
@NSCopying
var backgroundEffect: UIVisualEffect? { get set }
```

```objc
@property (nonatomic, copy, nullable) UIVisualEffect * backgroundEffect;
```

## Discussion

Assigning a visual effect object to this property adds that effect to the background of the action button.

## See Also

### Configuring the action’s appearance
- [var style: UITableViewRowAction.Style](./style-swift.property.md)
  The style applied to the action button.
- [UITableViewRowAction.Style](./style-swift.enum.md)
  Constants that specify the appearance of action buttons.
- [var title: String?](./title.md)
  The title of the action button.
- [var backgroundColor: UIColor?](./backgroundcolor.md)
  The background color of the action button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewrowaction/backgroundeffect)*