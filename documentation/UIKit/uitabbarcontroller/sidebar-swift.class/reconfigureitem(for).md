# reconfigureItem(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Requests the sidebar reconfigure the item representing the specified tab. This method has no effect if the `tab` is not currently displayed in the sidebar.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
func reconfigureItem(for tab: UITab)
```

```objc
- (void) reconfigureItemForTab:(UITab *) tab;
```

## See Also

### Managing customization
- [var isHidden: Bool](./ishidden.md)
  Determines if the sidebar is currently hidden.
- [var preferredLayout: UITabBarController.Sidebar.Layout](./preferredlayout.md)
  The preferred layout for how the sidebar lays out with the tab bar controller’s content. Default is `.automatic`
- [UITabBarController.Sidebar.Layout](./layout.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/reconfigureitem(for:))*