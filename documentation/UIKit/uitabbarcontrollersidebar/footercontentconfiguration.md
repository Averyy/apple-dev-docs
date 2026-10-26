# footerContentConfiguration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Content configuration for an optional header to display in the sidebar. The footer is displayed below all tab content in the sidebar.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```objc
@property (nonatomic, copy, nullable) id<UIContentConfiguration> footerContentConfiguration;
```

## See Also

### Headers and footers
- [var bottomBarView: UIView?](../uitabbarcontroller/sidebar-swift.class/bottombarview.md)
  A view to display at the bottom of the sidebar, like a UIToolbar. The width of this view will be managed by the sidebar itself, and its height will be set to the value it returns from `systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:` Default is nil.
- [headerContentConfiguration](./headercontentconfiguration.md)
  Content configuration for an optional header to display in the sidebar. The header is displayed above all tab content in the sidebar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontrollersidebar/footercontentconfiguration)*