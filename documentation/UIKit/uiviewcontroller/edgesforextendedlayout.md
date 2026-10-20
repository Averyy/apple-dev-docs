# edgesForExtendedLayout

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The edges that you extend for your view controller.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var edgesForExtendedLayout: UIRectEdge { get set }
```

```objc
@property (nonatomic, assign) UIRectEdge edgesForExtendedLayout;
```

#### Discussion

Instead of this property, use the safe area of your view to determine which parts of your interface are occluded by other content. For more information, see the [`safeAreaLayoutGuide`](../uiview/safearealayoutguide.md) and [`safeAreaInsets`](../uiview/safeareainsets.md) properties of [`UIView`](../uiview.md).

In iOS 10 and earlier, use this property to report which edges of your view controller extend underneath navigation bars or other system-provided views. The default value of this property is [`all`](../uirectedge/all.md), and it is recommended that you do not change that value.

If you remove an edge value from this property, the system does not lay out your content underneath other bars on that same edge. In addition, the system provides a default background so that translucent bars have an appropriate appearance. The window’s root view controller does not react to this property.

## See Also

### Configuring the view’s layout behavior
- [struct UIRectEdge](../uirectedge.md)
  Constants that specify the edges of a rectangle.
- [var extendedLayoutIncludesOpaqueBars: Bool](./extendedlayoutincludesopaquebars.md)
  A Boolean value indicating whether or not the extended layout includes opaque bars.
- [func viewWillLayoutSubviews()](./viewwilllayoutsubviews%28%29.md)
  Notifies the view controller that its view is about to lay out its subviews.
- [func viewDidLayoutSubviews()](./viewdidlayoutsubviews%28%29.md)
  Notifies the view controller when its view finishes laying out its subviews.
- [func updateViewConstraints()](./updateviewconstraints%28%29.md)
  Notifies the view controller when its view needs to update its constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/edgesforextendedlayout)*