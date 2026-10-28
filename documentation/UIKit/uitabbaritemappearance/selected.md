# selected

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The appearance data to apply to the tab bar item when it’s selected.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var selected: UITabBarItemStateAppearance { get }
```

```objc
@property (nonatomic, strong, readonly) UITabBarItemStateAppearance * selected;
```

## Discussion

To set the attributes for this state, get the object in this property and modify it.

## See Also

### Configuring attributes for different item states
- [var normal: UITabBarItemStateAppearance](./normal.md)
  The appearance data to apply to the tab bar item when it’s enabled, unselected, and not the focused item.
- [var disabled: UITabBarItemStateAppearance](./disabled.md)
  The appearance data to apply to the tab bar item when it’s disabled.
- [var focused: UITabBarItemStateAppearance](./focused.md)
  The appearance data to apply to the tab bar item when it’s focused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritemappearance/selected)*