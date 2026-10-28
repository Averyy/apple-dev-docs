# contentSafeAreaInsets

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

Insets that define the area where it’s safe to display content on the screen.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
var contentSafeAreaInsets: UIEdgeInsets { get }
```

```objc
@property (nonatomic, readonly) UIEdgeInsets contentSafeAreaInsets;
```

## Discussion

The 40 mm and 44 mm watches have rounded corners that may clip content that extends to the edge of the screen. The content-safe area defines the region below the status bar that avoids the rounded corners.

The system’s built-in containers and controls automatically use the content-safe area insets; however, if you build a custom user interface with SpriteKit or SceneKit, you should check the [`contentSafeAreaInsets`](./contentsafeareainsets.md) and [`systemMinimumLayoutMargins`](./systemminimumlayoutmargins.md), and lay out your interface accordingly.

The system sets [`contentSafeAreaInsets`](./contentsafeareainsets.md) property just before it calls the controller’s [`didAppear()`](./didappear%28%29.md) method. Before [`didAppear()`](./didappear%28%29.md), the property may contain an invalid value.

## See Also

### Respecting safe areas and layout margins
- [var systemMinimumLayoutMargins: NSDirectionalEdgeInsets](./systemminimumlayoutmargins.md)
  Leading and trailing insets that represent the minimum layout margins for text elements.
- [var contentFrame: CGRect](./contentframe.md)
  The frame rectangle used to display your app’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contentsafeareainsets)*