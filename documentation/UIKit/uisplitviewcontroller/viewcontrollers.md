# viewControllers

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The array of view controllers the split view controller manages.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var viewControllers: [UIViewController] { get set }
```

```objc
@property (nonatomic, copy) NSArray<__kindof UIViewController *> * viewControllers;
```

#### Discussion

When the split view interface is expanded, this property contains two or three view controllers depending on the interface’s [`style`](./style-swift.property.md). The first view controller in the array is the primary view controller. It’s followed by the supplementary (if present) and then the secondary view controller.

When the split view interface is collapsed, this property contains only one view controller. If a view controller is set for the [`UISplitViewController.Column.compact`](./column/compact.md) column, this property contains that view controller. Otherwise, this property contains the primary view controller.

In a column-style split view controller, it’s recommended that you set the child view controllers using the [`setViewController(_:for:)`](./setviewcontroller%28_,for%29.md) method and get them using the [`viewController(for:)`](./viewcontroller%28for%29.md) method.

In a classic split view controller, you can use this property to assign the primary and secondary view controllers that you want to display initially. After the split view controller is onscreen, you can use this property to get the view controllers in the split view interface. After you assign the initial view controllers, it’s better to set the child view controllers using the [`show(_:sender:)`](./show%28_,sender%29.md) and [`showDetailViewController(_:sender:)`](./showdetailviewcontroller%28_,sender%29.md) methods. Although you can still change the view controllers in this property directly, you should do so only if you manually manage your app’s view controller transitions.

## See Also

### Related Documentation
- [func showDetailViewController(UIViewController, sender: Any?)](./showdetailviewcontroller%28_,sender%29.md)
  Presents the specified view controller as the secondary view controller of the split view interface.
- [func show(UIViewController, sender: Any?)](./show%28_,sender%29.md)
  Presents the specified view controller as the primary view controller in the split view interface.
### Managing the child view controllers
- [UISplitViewController.Column](./column.md)
  Constants that describe the columns within the split view interface.
- [func setViewController(UIViewController?, for: UISplitViewController.Column)](./setviewcontroller%28_,for%29.md)
  Presents the provided view controller in the specified column of the split view interface.
- [func viewController(for: UISplitViewController.Column) -> UIViewController?](./viewcontroller%28for%29.md)
  Returns the view controller associated with the specified column of the split view interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/viewcontrollers)*