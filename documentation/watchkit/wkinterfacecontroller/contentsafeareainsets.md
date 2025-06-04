# contentSafeAreaInsets

**Framework**: WatchKit  
**Kind**: property

Insets that define the area where it’s safe to display content on the screen.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
@MainActor
var contentSafeAreaInsets: UIEdgeInsets { get }
```

#### Discussion

The 40 mm and 44 mm watches have rounded corners that may clip content that extends to the edge of the screen. The content-safe area defines the region below the status bar that avoids the rounded corners.

The system’s built-in containers and controls automatically use the content-safe area insets; however, if you build a custom user interface with SpriteKit or SceneKit, you should check the [`contentSafeAreaInsets`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contentsafeareainsets) and [`systemMinimumLayoutMargins`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/systemminimumlayoutmargins), and lay out your interface accordingly.

The system sets [`contentSafeAreaInsets`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contentsafeareainsets) property just before it calls the controller’s [`didAppear()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/didappear()) method. Before [`didAppear()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/didappear()), the property may contain an invalid value.

## See Also

- [var systemMinimumLayoutMargins: NSDirectionalEdgeInsets](systemminimumlayoutmargins.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/systemminimumlayoutmargins))
  Leading and trailing insets that represent the minimum layout margins for text elements.
- [var contentFrame: CGRect](contentframe.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contentframe))
  The frame rectangle used to display your app’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contentsafeareainsets)*