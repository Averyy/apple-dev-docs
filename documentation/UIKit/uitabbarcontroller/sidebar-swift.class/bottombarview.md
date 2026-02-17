# bottomBarView

**Framework**: UIKit  
**Kind**: property

A view to display at the bottom of the sidebar, like a UIToolbar. The width of this view will be managed by the sidebar itself, and its height will be set to the value it returns from `systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:` Default is nil.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
var bottomBarView: UIView? { get set }
```

## See Also

- [var footerContentConfiguration: (any UIContentConfiguration)?](uitabbarcontroller/sidebar-swift.class/footercontentconfiguration.md)
- [var headerContentConfiguration: (any UIContentConfiguration)?](uitabbarcontroller/sidebar-swift.class/headercontentconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/bottombarview)*