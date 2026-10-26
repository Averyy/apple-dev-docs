# UIViewController.Transition.ZoomSourceViewProviderContext

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UIZoomTransitionSourceViewProviderContext : NSObject
```

## Topics

### Accessing the view controllers
- [var sourceViewController: UIViewController](./zoomsourceviewprovidercontext/sourceviewcontroller.md)
  The view controller that presents the zoomed view.
- [var zoomedViewController: UIViewController](./zoomsourceviewprovidercontext/zoomedviewcontroller.md)
  The view controller for the presented view.

## Relationships

### Inherits From
- [NSObject](../../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [NSObjectProtocol](../../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating zoom transitions
- [static func zoom(options: UIViewController.Transition.ZoomOptions?, sourceViewProvider: (UIViewController.Transition.ZoomSourceViewProviderContext) -> UIView?) -> Self](./zoom%28options,sourceviewprovider%29.md)
  Creates a zoom transition from the view that the source provider specifies.
- [UIViewController.Transition.ZoomOptions](./zoomoptions.md)
  Options for a zoom transition.
- [+ zoomWithOptions:sourceViewProvider:](../../uiviewcontrollertransition/zoomwithoptions_sourceviewprovider_.md)
  Creates a zoom transition from the view specified by the source provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/transition/zoomsourceviewprovidercontext)*