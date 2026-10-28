# setNeedsUpdateOfVerticalBarConfiguration()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Signals to the system that the preferred vertical bar configuration, such as its behavior, has changed.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
func setNeedsUpdateOfVerticalBarConfiguration()
```

```objc
- (void) setNeedsUpdateOfVerticalBarConfiguration;
```

## Discussion

Call this method following changes to any state that affects the return values of methods like [`preferredVerticalBarBehavior`](./preferredverticalbarbehavior.md) or [`childForPreferredVerticalBarBehavior`](./childforpreferredverticalbarbehavior.md).

## See Also

### Configuring bars on the vertical axis
- [var preferredVerticalBarBehavior: UIVerticalBarBehavior](./preferredverticalbarbehavior.md)
  The vertical bar behavior that this view controller prefers.
- [enum UIVerticalBarBehavior](../uiverticalbarbehavior.md)
  A behavior that determines whether the vertical bar is used.
- [var childForPreferredVerticalBarBehavior: UIViewController?](./childforpreferredverticalbarbehavior.md)
  Which child view controller, if any, should control the vertical bar behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsupdateofverticalbarconfiguration())*