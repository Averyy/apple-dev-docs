# systemMinimumLayoutMargins

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

Leading and trailing insets that represent the minimum layout margins for text elements.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
var systemMinimumLayoutMargins: NSDirectionalEdgeInsets { get }
```

```objc
@property (nonatomic, readonly) NSDirectionalEdgeInsets systemMinimumLayoutMargins;
```

## Discussion

The 40 mm and 44 mm watches have rounded corners. As a result, the items in the status bar do not extend all the way to the edge of the screen.

The system provides the minimum layout margins to help you align your text content with the status bar. The system’s built-in containers and controls take the minimum layout margins into account automatically when laying out your interface; however, if you build a custom user interface with SpriteKit or SceneKit, check the [`contentSafeAreaInsets`](./contentsafeareainsets.md) and [`systemMinimumLayoutMargins`](./systemminimumlayoutmargins.md), and lay out your interface accordingly.

The system sets the [`systemMinimumLayoutMargins`](./systemminimumlayoutmargins.md) property just before it calls the controller’s [`didAppear()`](./didappear%28%29.md) method. Before calling [`didAppear()`](./didappear%28%29.md), the property may contain an invalid value.

## See Also

### Respecting safe areas and layout margins
- [var contentSafeAreaInsets: UIEdgeInsets](./contentsafeareainsets.md)
  Insets that define the area where it’s safe to display content on the screen.
- [var contentFrame: CGRect](./contentframe.md)
  The frame rectangle used to display your app’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/systemminimumlayoutmargins)*