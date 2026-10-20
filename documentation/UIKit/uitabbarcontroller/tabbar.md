# tabBar

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The tab bar view associated with this controller.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var tabBar: UITabBar { get }
```

```objc
@property (nonatomic, readonly) UITabBar * tabBar;
```

#### Discussion

You should never attempt to manipulate the [`UITabBar`](../uitabbar.md) object itself stored in this property. If you attempt to do so, the tab bar view throws an exception. To configure the items for your tab bar interface, you should instead assign one or more custom view controllers to the [`viewControllers`](./viewcontrollers.md) property. The tab bar collects the needed tab bar items from the view controllers you specify.

The tab bar view provided by this property is only for situations where you want to display an action sheet using the [`show(from:)`](../uiactionsheet/show%28from%29-9i3tw.md) method of the [`UIActionSheet`](../uiactionsheet.md) class.

## See Also

### Accessing the tab bar controller properties
- [func tab(forIdentifier: String) -> UITab?](./tab%28foridentifier%29.md)
  Returns the `tab` matching the specified `identifier` in the tab bar controller’s tabs. Returns nil if no tab is found matching the `identifier`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/tabbar)*