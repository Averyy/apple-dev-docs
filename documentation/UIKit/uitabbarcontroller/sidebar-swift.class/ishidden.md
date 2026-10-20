# isHidden

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Determines if the sidebar is currently hidden.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
var isHidden: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isHidden) BOOL hidden;
```

## Mentions

- [Elevating your iPad app with a tab bar and sidebar](../../elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md)

## See Also

### Managing customization
- [var preferredLayout: UITabBarController.Sidebar.Layout](./preferredlayout.md)
  The preferred layout for how the sidebar lays out with the tab bar controller’s content. Default is `.automatic`
- [UITabBarController.Sidebar.Layout](./layout.md)
- [func reconfigureItem(for: UITab)](./reconfigureitem%28for%29.md)
  Requests the sidebar reconfigure the item representing the specified tab. This method has no effect if the `tab` is not currently displayed in the sidebar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/ishidden)*