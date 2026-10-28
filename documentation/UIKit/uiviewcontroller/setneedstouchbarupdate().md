# setNeedsTouchBarUpdate()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the system to update the Touch Bar.

**Availability**:
- Mac Catalyst 13.0+

## Declaration

```swift
func setNeedsTouchBarUpdate()
```

```objc
- (void) setNeedsTouchBarUpdate;
```

## Discussion

Call this method when the value from [`childViewControllerForTouchBar`](./childviewcontrollerfortouchbar.md) changes.

## See Also

### Managing the Touch Bar
- [var childViewControllerForTouchBar: UIViewController?](./childviewcontrollerfortouchbar.md)
  The child view controller that the system uses to display content in the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedstouchbarupdate())*