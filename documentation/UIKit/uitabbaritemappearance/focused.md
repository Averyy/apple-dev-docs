# focused

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The appearance data to apply to the tab bar item when it’s focused.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var focused: UITabBarItemStateAppearance { get }
```

```objc
@property (nonatomic, strong, readonly) UITabBarItemStateAppearance * focused;
```

## Discussion

To set the attributes for this state, get the object in this property and modify it.

## See Also

### Configuring attributes for different item states
- [var normal: UITabBarItemStateAppearance](./normal.md)
  The appearance data to apply to the tab bar item when it’s enabled, unselected, and not the focused item.
- [var selected: UITabBarItemStateAppearance](./selected.md)
  The appearance data to apply to the tab bar item when it’s selected.
- [var disabled: UITabBarItemStateAppearance](./disabled.md)
  The appearance data to apply to the tab bar item when it’s disabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritemappearance/focused)*