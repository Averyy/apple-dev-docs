# setContentOffset(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the point at which the origin of the content view is offset from the origin of the scroll view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setContentOffset(_ contentOffset: CGPoint, animated: Bool)
```

```objc
- (void) setContentOffset:(CGPoint) contentOffset animated:(BOOL) animated;
```

## Parameters

- `contentOffset`: A point (expressed in points) that’s offset from the content view’s origin.
- `animated`: [`true`](../../Swift/true.md) to animate the transition at a constant velocity to the new offset, [`false`](../../Swift/false.md) to make the transition immediate.

## See Also

### Managing the content size and offset
- [var contentSize: CGSize](./contentsize.md)
  The size of the content view.
- [var contentOffset: CGPoint](./contentoffset.md)
  The point at which the origin of the content view is offset from the origin of the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/setcontentoffset(_:animated:))*