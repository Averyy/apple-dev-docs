# extendedLayoutIncludesOpaqueBars

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether or not the extended layout includes opaque bars.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var extendedLayoutIncludesOpaqueBars: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

> **Note**:  Bars are translucent by default in iOS 7.0

 Bars are translucent by default in iOS 7.0

## See Also

- [var edgesForExtendedLayout: UIRectEdge](uiviewcontroller/edgesforextendedlayout.md)
  The edges that you extend for your view controller.
- [struct UIRectEdge](uirectedge.md)
  Constants that specify the edges of a rectangle.
- [func viewWillLayoutSubviews()](uiviewcontroller/viewwilllayoutsubviews.md)
  Notifies the view controller that its view is about to lay out its subviews.
- [func viewDidLayoutSubviews()](uiviewcontroller/viewdidlayoutsubviews.md)
  Notifies the view controller when its view finishes laying out its subviews.
- [func updateViewConstraints()](uiviewcontroller/updateviewconstraints.md)
  Notifies the view controller when its view needs to update its constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/extendedlayoutincludesopaquebars)*