# backgroundColor

**Framework**: UIKit  
**Kind**: property

The background color of the action button.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@NSCopying
@MainActor var backgroundColor: UIColor? { get set }
```

#### Discussion

Use this property to specify the background color for your button. If you don’t specify a value for this property, UIKit assigns a default color based on the value in the [`style`](uitableviewrowaction/style-swift.property.md) property.

## See Also

- [var style: UITableViewRowAction.Style](uitableviewrowaction/style-swift.property.md)
  The style applied to the action button.
- [UITableViewRowAction.Style](uitableviewrowaction/style-swift.enum.md)
  Constants that specify the appearance of action buttons.
- [var title: String?](uitableviewrowaction/title.md)
  The title of the action button.
- [var backgroundEffect: UIVisualEffect?](uitableviewrowaction/backgroundeffect.md)
  The visual effect to apply to the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewrowaction/backgroundcolor)*