# childViewControllerForTouchBar

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The child view controller that the system uses to display content in the Touch Bar.

**Availability**:
- Mac Catalyst 13.0+

## Declaration

```swift
var childViewControllerForTouchBar: UIViewController? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIViewController * childViewControllerForTouchBar;
```

#### Discussion

Override this property to have the system use the [`touchBar`](../uiresponder/touchbar.md) object from a child view controller instead of the current view controller. If [`childViewControllerForTouchBar`](./childviewcontrollerfortouchbar.md) is `nil`, the system uses the current view controller’s [`touchBar`](../uiresponder/touchbar.md) object.

The default value is `nil`.

## See Also

### Managing the Touch Bar
- [func setNeedsTouchBarUpdate()](./setneedstouchbarupdate%28%29.md)
  Tells the system to update the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/childviewcontrollerfortouchbar)*