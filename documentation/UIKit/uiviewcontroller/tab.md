# tab

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The `UITab` instance that was used to create the receiver, and represents the view controller. Default is nil.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
weak var tab: UITab? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) UITab * tab;
```

## See Also

### Configuring tab bar content
- [var tabBarItem: UITabBarItem!](./tabbaritem.md)
  The tab bar item that represents the view controller when added to a tab bar controller.
- [var tabBarObservedScrollView: UIScrollView?](./tabbarobservedscrollview.md)
  The full-screen scroll view to synchronize with a scrolling tab bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/tab)*