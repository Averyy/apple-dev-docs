# point(inside:with:)

**Framework**: UIKit  
**Kind**: method

Returns a Boolean value indicating whether the receiver contains the specified point.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func point(inside point: CGPoint, with event: UIEvent?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `point` is inside the receiver’s bounds; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `point`: A point that is in the receiver’s local coordinate system (bounds).
- `event`: The event that warranted a call to this method. If you are calling this method from outside your event-handling code, you may specify  .

## See Also

- [func hitTest(CGPoint, with: UIEvent?) -> UIView?](uiview/hittest(_:with:).md)
  Returns the farthest descendant in the view hierarchy of the current view, including itself, that contains the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/point(inside:with:))*