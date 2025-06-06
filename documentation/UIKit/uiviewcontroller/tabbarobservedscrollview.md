# tabBarObservedScrollView

**Framework**: UIKit  
**Kind**: property

The full-screen scroll view to synchronize with a scrolling tab bar.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
@MainActor
var tabBarObservedScrollView: UIScrollView? { get set }
```

#### Discussion

Typically, the position of the tab bar remains fixed while content scrolls underneath it. Use this property in your tvOS apps to create an interface where the tab bar scrolls with the rest of your content. When you set the value of this property to a scroll view, UIKit synchronizes the position of the tab bar with the current scroll position of that scroll view. The default value of this property is `nil`.

## See Also

- [var tabBarItem: UITabBarItem!](uiviewcontroller/tabbaritem.md)
  The tab bar item that represents the view controller when added to a tab bar controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/tabbarobservedscrollview)*