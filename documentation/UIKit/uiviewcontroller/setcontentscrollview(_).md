# setContentScrollView(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the scroll view that bars observe for all edges of the view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func setContentScrollView(_ scrollView: UIScrollView?)
```

## Discussion

Calling this convenience method is identical to calling [`setContentScrollView(_:for:)`](./setcontentscrollview%28_,for%29.md) and passing [`all`](../nsdirectionalrectedge/all.md) for the `edge` parameter.

## Parameters

- `scrollView`: The scroll view to observe.

## See Also

### Working with scrolling content
- [func setContentScrollView(UIScrollView?, for: NSDirectionalRectEdge)](./setcontentscrollview%28_,for%29.md)
  Sets the scroll view that bars observe for the specified edge.
- [func contentScrollView(for: NSDirectionalRectEdge) -> UIScrollView?](./contentscrollview%28for%29.md)
  Returns the scroll view the view controller observes for the specified edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/setcontentscrollview(_:))*