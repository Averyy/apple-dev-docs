# contentScrollView(for:)

**Framework**: UIKit  
**Kind**: method

Returns the scroll view the view controller observes for the specified edge.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func contentScrollView(for edge: NSDirectionalRectEdge) -> UIScrollView?
```

#### Return Value

The scroll view the view controller observes for the edge.

#### Discussion

Toolbars, navigation bars, and tab bars adjust their appearance when the edge of a scroll view’s content aligns with the edge of the bar. If you want to disable this behavior for one or more edges, override this method and return `nil` for the appropriate edge. If you don’t set a scroll view with [`setContentScrollView(_:for:)`](uiviewcontroller/setcontentscrollview(_:for:).md) or [`setContentScrollView(_:)`](uiviewcontroller/setcontentscrollview(_:).md), the default implementation of this method returns `nil`.

The following example disables the scroll edge view for the top edge only. This example disables the appearance changes of the navigation bar at the top edge, but not the toolbar at the bottom edge.

```swift
override func contentScrollView(for edge: NSDirectionalRectEdge) -> UIScrollView? {
    if edge == .top {
        return nil
    } else {
        return super.contentScrollView(for: edge)
    }
}
```

## Parameters

- `edge`: The edge the scroll view observes for alignment,   or  . Passing any other value raises an exception.

## See Also

- [func setContentScrollView(UIScrollView?, for: NSDirectionalRectEdge)](uiviewcontroller/setcontentscrollview(_:for:).md)
  Sets the scroll view that bars observe for the specified edge.
- [func setContentScrollView(UIScrollView?)](uiviewcontroller/setcontentscrollview(_:).md)
  Sets the scroll view that bars observe for all edges of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/contentscrollview(for:))*