# tabBarObservedScrollView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The full-screen scroll view to synchronize with a scrolling tab bar.

**Availability**:
- tvOS 13.0+ - Deprecated in 27.2

> **Deprecated**: Use [`setContentScrollView(_:for:)`](./setcontentscrollview%28_,for%29.md) instead.

## Declaration

```swift
var tabBarObservedScrollView: UIScrollView? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIScrollView * tabBarObservedScrollView;
```

## Discussion

Typically, the position of the tab bar remains fixed while content scrolls underneath it. Use this property in your tvOS apps to create an interface where the tab bar scrolls with the rest of your content. When you set the value of this property to a scroll view, UIKit synchronizes the position of the tab bar with the current scroll position of that scroll view. The default value of this property is `nil`.

## See Also

### Configuring tab bar content
- [var tab: UITab?](./tab.md)
  The `UITab` instance that was used to create the receiver, and represents the view controller. Default is nil.
- [var tabBarItem: UITabBarItem!](./tabbaritem.md)
  The tab bar item that represents the view controller when added to a tab bar controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/tabbarobservedscrollview)*