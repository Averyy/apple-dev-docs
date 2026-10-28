# preferredScreenEdgesDeferringSystemGestures

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The screen edges for which you want your gestures to take precedence over the system gestures.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var preferredScreenEdgesDeferringSystemGestures: UIRectEdge { get }
```

```objc
@property (nonatomic, readonly) UIRectEdge preferredScreenEdgesDeferringSystemGestures;
```

## Discussion

Normally, the screen-edge gestures defined by the system take precedence over any gesture recognizers that you define. The system uses its gestures to implement system-level behaviors, such as to display Control Center.

Whenever possible, you should allow the system gestures to take precedence. However, immersive apps can use this property to allow app-defined gestures to take precedence over the system gestures. You do that by overriding this property and returning the screen edges for which your gestures should take precedence.

If you change the edges preferred by your view controller, update the value of this property and call the [`setNeedsUpdateOfScreenEdgesDeferringSystemGestures()`](./setneedsupdateofscreenedgesdeferringsystemgestures%28%29.md) method to notify the system that the edges have changed.

For information on showing and hiding the visual indicator for returning to the Home Screen, see [`prefersHomeIndicatorAutoHidden`](./prefershomeindicatorautohidden.md).

## See Also

### Coordinating with system gestures
- [var childForScreenEdgesDeferringSystemGestures: UIViewController?](./childforscreenedgesdeferringsystemgestures.md)
  Returns the child view controller that should be queried to see if its gestures should take precedence.
- [func setNeedsUpdateOfScreenEdgesDeferringSystemGestures()](./setneedsupdateofscreenedgesdeferringsystemgestures%28%29.md)
  Notifies the system of changes to the screen edges that defer system gestures.
- [var prefersHomeIndicatorAutoHidden: Bool](./prefershomeindicatorautohidden.md)
  A Boolean that indicates whether the system is allowed to hide the visual indicator for returning to the Home Screen.
- [var childForHomeIndicatorAutoHidden: UIViewController?](./childforhomeindicatorautohidden.md)
  Returns the child view controller that is consulted about its preference for displaying a visual indicator for returning to the Home screen.
- [func setNeedsUpdateOfHomeIndicatorAutoHidden()](./setneedsupdateofhomeindicatorautohidden%28%29.md)
  Notifies UIKit that your view controller updated its preference regarding the visual indicator for returning to the Home screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredscreenedgesdeferringsystemgestures)*