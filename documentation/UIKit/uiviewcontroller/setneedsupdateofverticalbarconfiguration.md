# setNeedsUpdateOfVerticalBarConfiguration()

**Framework**: UIKit  
**Kind**: method

Signals to the system that the preferred vertical bar configuration, such as its behavior, has changed.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
func setNeedsUpdateOfVerticalBarConfiguration()
```

#### Discussion

Call this method following changes to any state that affects the return values of methods like [`preferredVerticalBarBehavior`](uiviewcontroller/preferredverticalbarbehavior.md) or [`childForPreferredVerticalBarBehavior`](uiviewcontroller/childforpreferredverticalbarbehavior.md).

## See Also

- [var preferredVerticalBarBehavior: UIVerticalBarBehavior](uiviewcontroller/preferredverticalbarbehavior.md)
  The vertical bar behavior that this view controller prefers.
- [enum UIVerticalBarBehavior](uiverticalbarbehavior.md)
  A behavior that determines whether the vertical bar is used.
- [var childForPreferredVerticalBarBehavior: UIViewController?](uiviewcontroller/childforpreferredverticalbarbehavior.md)
  Which child view controller, if any, should control the vertical bar behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsupdateofverticalbarconfiguration())*