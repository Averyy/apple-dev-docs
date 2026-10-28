# extendedLayoutIncludesOpaqueBars

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether or not the extended layout includes opaque bars.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var extendedLayoutIncludesOpaqueBars: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL extendedLayoutIncludesOpaqueBars;
```

## Discussion

The default value of this property is [`false`](../../Swift/false.md).

> **Note**:  Bars are translucent by default in iOS 7.0

## See Also

### Configuring the view’s layout behavior
- [var edgesForExtendedLayout: UIRectEdge](./edgesforextendedlayout.md)
  The edges that you extend for your view controller.
- [struct UIRectEdge](../uirectedge.md)
  Constants that specify the edges of a rectangle.
- [func viewWillLayoutSubviews()](./viewwilllayoutsubviews%28%29.md)
  Notifies the view controller that its view is about to lay out its subviews.
- [func viewDidLayoutSubviews()](./viewdidlayoutsubviews%28%29.md)
  Notifies the view controller when its view finishes laying out its subviews.
- [func updateViewConstraints()](./updateviewconstraints%28%29.md)
  Notifies the view controller when its view needs to update its constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/extendedlayoutincludesopaquebars)*