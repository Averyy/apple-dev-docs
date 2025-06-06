# UIViewController.Transition.ZoomSourceViewProviderContext

**Framework**: UIKit  
**Kind**: class

A context object that contains references to the view controllers from a zoom transition.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
class ZoomSourceViewProviderContext
```

## Topics

### Accessing the view controllers
- [var sourceViewController: UIViewController](uiviewcontroller/transition/zoomsourceviewprovidercontext/sourceviewcontroller.md)
  The view controller that presents the zoomed view.
- [var zoomedViewController: UIViewController](uiviewcontroller/transition/zoomsourceviewprovidercontext/zoomedviewcontroller.md)
  The view controller for the presented view.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [static func zoom(options: UIViewController.Transition.ZoomOptions?, sourceViewProvider: (UIViewController.Transition.ZoomSourceViewProviderContext) -> UIView?) -> Self](uiviewcontroller/transition/zoom(options:sourceviewprovider:).md)
  Creates a zoom transition from the view that the source provider specifies.
- [UIViewController.Transition.ZoomOptions](uiviewcontroller/transition/zoomoptions.md)
  Options for a zoom transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/transition/zoomsourceviewprovidercontext)*