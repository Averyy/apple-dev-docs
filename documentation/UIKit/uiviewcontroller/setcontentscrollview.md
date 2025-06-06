# setContentScrollView(_:)

**Framework**: UIKit  
**Kind**: method

Sets the scroll view that bars observe for all edges of the view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func setContentScrollView(_ scrollView: UIScrollView?)
```

#### Discussion

Calling this convenience method is identical to calling [`setContentScrollView(_:for:)`](uiviewcontroller/setcontentscrollview(_:for:).md) and passing [`all`](nsdirectionalrectedge/all.md) for the `edge` parameter.

## Parameters

- `scrollView`: The scroll view to observe.

## See Also

- [func setContentScrollView(UIScrollView?, for: NSDirectionalRectEdge)](uiviewcontroller/setcontentscrollview(_:for:).md)
  Sets the scroll view that bars observe for the specified edge.
- [func contentScrollView(for: NSDirectionalRectEdge) -> UIScrollView?](uiviewcontroller/contentscrollview(for:).md)
  Returns the scroll view the view controller observes for the specified edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/setcontentscrollview(_:))*