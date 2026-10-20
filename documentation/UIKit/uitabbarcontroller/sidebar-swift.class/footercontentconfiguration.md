# footerContentConfiguration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency var footerContentConfiguration: (any UIContentConfiguration)? { get set }
```

## See Also

### Headers and footers
- [var bottomBarView: UIView?](./bottombarview.md)
  A view to display at the bottom of the sidebar, like a UIToolbar. The width of this view will be managed by the sidebar itself, and its height will be set to the value it returns from `systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:` Default is nil.
- [var headerContentConfiguration: (any UIContentConfiguration)?](./headercontentconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/footercontentconfiguration)*