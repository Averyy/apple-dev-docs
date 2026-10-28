# selectionIndicatorImage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The image to use for the selection indicator.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var selectionIndicatorImage: UIImage? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIImage * selectionIndicatorImage;
```

## Discussion

Use this property to specify a custom selection image. Your image is rendered on top of the tab bar but behind the contents of the tab bar item itself. The default value of this property is `nil`, which causes the tab bar to apply a default highlight to the selected item.

## See Also

### Configuring selection appearance
- [var unselectedItemTintColor: UIColor?](./unselecteditemtintcolor.md)
  The tint color to apply to unselected tabs.
- [var selectedImageTintColor: UIColor?](./selectedimagetintcolor.md)
  The tint color applied to the selected tab bar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/selectionindicatorimage)*