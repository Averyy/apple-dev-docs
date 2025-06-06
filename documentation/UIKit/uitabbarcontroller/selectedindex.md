# selectedIndex

**Framework**: Uikit  
**Kind**: property

The index of the view controller associated with the currently selected tab item.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var selectedIndex: Int { get set }
```

#### Discussion

This property nominally represents an index into the array of the [`viewControllers`](uitabbarcontroller/viewcontrollers.md) property. However, if the selected view controller is currently the More navigation controller, this property contains the value `NSNotFound`. Setting this property changes the selected view controller to the one at the designated index in the [`viewControllers`](uitabbarcontroller/viewcontrollers.md) array. To select the More navigation controller itself, you must change the value of the [`selectedViewController`](uitabbarcontroller/selectedviewcontroller.md) property instead.

In versions of iOS prior to version 3.0, this property reflects the index of the selected tab bar item only. Attempting to set this value to an index of a view controller that is not visible in the tab bar, but is instead managed by the More navigation controller, has no effect.

> **Note**:  The More interface is not available in tvOS.

## See Also

- [var selectedViewController: UIViewController?](uitabbarcontroller/selectedviewcontroller.md)
  The view controller associated with the currently selected tab item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/selectedindex)*