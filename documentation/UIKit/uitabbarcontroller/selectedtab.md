# selectedTab

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The currently selected tab, which can be a root tab or any of their descendants.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var selectedTab: UITab? { get set }
```

```objc
@property (nonatomic, strong, nullable) UITab * selectedTab;
```

## Discussion

The default value for this property is `nil`.

## See Also

### Managing the selected tab
- [var selectedViewController: UIViewController?](./selectedviewcontroller.md)
  The view controller associated with the currently selected tab item.
- [var selectedIndex: Int](./selectedindex.md)
  The index of the view controller associated with the currently selected tab item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/selectedtab)*