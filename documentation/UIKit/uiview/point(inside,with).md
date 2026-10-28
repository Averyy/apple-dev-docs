# point(inside:with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the receiver contains the specified point.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func point(inside point: CGPoint, with event: UIEvent?) -> Bool
```

```objc
- (BOOL) pointInside:(CGPoint) point withEvent:(UIEvent *) event;
```

## Return Value

[`true`](../../Swift/true.md) if `point` is inside the receiver’s bounds; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `point`: A point that is in the receiver’s local coordinate system (bounds).
- `event`: The event that warranted a call to this method. If you are calling this method from outside your event-handling code, you may specify `nil`.

## See Also

### Hit-testing in a view
- [func hitTest(CGPoint, with: UIEvent?) -> UIView?](./hittest%28_,with%29.md)
  Returns the farthest descendant in the view hierarchy of the current view, including itself, that contains the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/point(inside:with:))*