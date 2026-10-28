# selectedImageTintColor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The tint color applied to the selected tab bar item.

**Availability**:
- iOS 5.0+ - Deprecated in 8.0
- iPadOS 5.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the [`tintColor`](./tintcolor.md) property instead.

## Declaration

```swift
var selectedImageTintColor: UIColor? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIColor * selectedImageTintColor;
```

## Discussion

The default value is `nil`, which results in use of the tab bar’s [`tintColor`](./tintcolor.md) property.

## See Also

### Configuring selection appearance
- [var unselectedItemTintColor: UIColor?](./unselecteditemtintcolor.md)
  The tint color to apply to unselected tabs.
- [var selectionIndicatorImage: UIImage?](./selectionindicatorimage.md)
  The image to use for the selection indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/selectedimagetintcolor)*