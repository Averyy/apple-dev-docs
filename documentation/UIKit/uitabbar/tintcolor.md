# tintColor

**Framework**: UIKit  
**Kind**: property

The tint color to apply to the tab bar items.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var tintColor: UIColor! { get set }
```

#### Discussion

Assigning a value to this property applies the specified color only to the tab bar’s items. Even if you do not specify a color, the tab bar may tint items using the tint color of one of its ancestor views. For information on how tinting colors are applied to views in a view hierarchy, see the description of the [`tintColor`](uiview/tintcolor.md) property in [`UIView`](uiview.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/tintcolor)*