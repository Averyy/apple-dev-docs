# setContentOffset(_:animated:)

**Framework**: UIKit  
**Kind**: method

Sets the offset from the content view’s origin that corresponds to the scroll view’s origin.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setContentOffset(_ contentOffset: CGPoint, animated: Bool)
```

## Parameters

- `contentOffset`: A point (expressed in points) that’s offset from the content view’s origin.
- `animated`:   to animate the transition at a constant velocity to the new offset,   to make the transition immediate.

## See Also

- [var contentSize: CGSize](uiscrollview/contentsize.md)
  The size of the content view.
- [var contentOffset: CGPoint](uiscrollview/contentoffset.md)
  The point at which the origin of the content view is offset from the origin of the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscrollview/setcontentoffset(_:animated:))*