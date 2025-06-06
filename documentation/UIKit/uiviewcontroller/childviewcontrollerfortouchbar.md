# childViewControllerForTouchBar

**Framework**: UIKit  
**Kind**: property

The child view controller that the system uses to display content in the Touch Bar.

**Availability**:
- Mac Catalyst 13.0+

## Declaration

```swift
@MainActor
var childViewControllerForTouchBar: UIViewController? { get }
```

#### Discussion

Override this property to have the system use the [`touchBar`](uiresponder/touchbar.md) object from a child view controller instead of the current view controller. If [`childViewControllerForTouchBar`](uiviewcontroller/childviewcontrollerfortouchbar.md) is `nil`, the system uses the current view controller’s [`touchBar`](uiresponder/touchbar.md) object.

The default value is `nil`.

## See Also

- [func setNeedsTouchBarUpdate()](uiviewcontroller/setneedstouchbarupdate.md)
  Tells the system to update the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/childviewcontrollerfortouchbar)*