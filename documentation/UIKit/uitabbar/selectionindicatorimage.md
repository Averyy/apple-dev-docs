# selectionIndicatorImage

**Framework**: UIKit  
**Kind**: property

The image to use for the selection indicator.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var selectionIndicatorImage: UIImage? { get set }
```

#### Discussion

Use this property to specify a custom selection image. Your image is rendered on top of the tab bar but behind the contents of the tab bar item itself. The default value of this property is `nil`, which causes the tab bar to apply a default highlight to the selected item.

## See Also

- [var unselectedItemTintColor: UIColor?](uitabbar/unselecteditemtintcolor.md)
  The tint color to apply to unselected tabs.
- [var selectedImageTintColor: UIColor?](uitabbar/selectedimagetintcolor.md)
  The tint color applied to the selected tab bar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/selectionindicatorimage)*