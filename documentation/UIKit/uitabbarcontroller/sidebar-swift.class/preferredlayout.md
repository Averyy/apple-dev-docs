# preferredLayout

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The preferred layout for how the sidebar lays out with the tab bar controller’s content. Default is `.automatic`

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
var preferredLayout: UITabBarController.Sidebar.Layout { get set }
```

```objc
@property (nonatomic, assign) UITabBarControllerSidebarLayout preferredLayout;
```

## See Also

### Managing customization
- [var isHidden: Bool](./ishidden.md)
  Determines if the sidebar is currently hidden.
- [UITabBarController.Sidebar.Layout](./layout.md)
- [func reconfigureItem(for: UITab)](./reconfigureitem%28for%29.md)
  Requests the sidebar reconfigure the item representing the specified tab. This method has no effect if the `tab` is not currently displayed in the sidebar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/preferredlayout)*