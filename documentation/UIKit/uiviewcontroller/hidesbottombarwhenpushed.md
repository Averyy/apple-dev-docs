# hidesBottomBarWhenPushed

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the toolbar at the bottom of the screen is hidden when the view controller is pushed on to a navigation controller.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
var hidesBottomBarWhenPushed: Bool { get set }
```

```objc
@property (nonatomic) BOOL hidesBottomBarWhenPushed;
```

#### Discussion

A view controller added as a child of a navigation controller can display an optional toolbar at the bottom of the screen. The value of this property on the topmost view controller determines whether the toolbar is visible. If the value of this property is [`true`](../../Swift/true.md), the toolbar is hidden. If the value of this property is [`false`](../../Swift/false.md), the bar is visible.

## See Also

### Configuring a navigation interface
- [var navigationItem: UINavigationItem](./navigationitem.md)
  The navigation item used to represent the view controller in a parent’s navigation bar.
- [func setToolbarItems([UIBarButtonItem]?, animated: Bool)](./settoolbaritems%28_,animated%29.md)
  Sets the toolbar items to be displayed along with the view controller.
- [var toolbarItems: [UIBarButtonItem]?](./toolbaritems.md)
  The toolbar items associated with the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/hidesbottombarwhenpushed)*