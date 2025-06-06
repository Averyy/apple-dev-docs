# selectedImageTintColor

**Framework**: UIKit  
**Kind**: property

The tint color applied to the selected tab bar item.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var selectedImageTintColor: UIColor? { get set }
```

#### Discussion

The default value is `nil`, which results in use of the tab bar’s [`tintColor`](uitabbar/tintcolor.md) property.

## See Also

- [var unselectedItemTintColor: UIColor?](uitabbar/unselecteditemtintcolor.md)
  The tint color to apply to unselected tabs.
- [var selectionIndicatorImage: UIImage?](uitabbar/selectionindicatorimage.md)
  The image to use for the selection indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/selectedimagetintcolor)*