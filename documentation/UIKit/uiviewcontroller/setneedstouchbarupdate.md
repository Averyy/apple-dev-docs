# setNeedsTouchBarUpdate()

**Framework**: UIKit  
**Kind**: method

Tells the system to update the Touch Bar.

**Availability**:
- Mac Catalyst 13.0+

## Declaration

```swift
@MainActor
func setNeedsTouchBarUpdate()
```

#### Discussion

Call this method when the value from [`childViewControllerForTouchBar`](uiviewcontroller/childviewcontrollerfortouchbar.md) changes.

## See Also

- [var childViewControllerForTouchBar: UIViewController?](uiviewcontroller/childviewcontrollerfortouchbar.md)
  The child view controller that the system uses to display content in the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedstouchbarupdate())*