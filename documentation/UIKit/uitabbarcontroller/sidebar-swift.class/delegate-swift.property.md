# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The object managing the delegate of the sidebar.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
weak var delegate: (any UITabBarController.Sidebar.Delegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UITabBarControllerSidebarDelegate> delegate;
```

## See Also

### Setting the sidebar delegate
- [UITabBarController.Sidebar.Delegate](./delegate-swift.protocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.property)*