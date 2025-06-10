# UIViewController.Transition

**Framework**: UIKit  
**Kind**: class

An object that defines the transition animation when switching to a new view controller.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
class Transition
```

## Topics

### Creating zoom transitions
- [static func zoom(options: UIViewController.Transition.ZoomOptions?, sourceViewProvider: (UIViewController.Transition.ZoomSourceViewProviderContext) -> UIView?) -> Self](uiviewcontroller/transition/zoom(options:sourceviewprovider:).md)
  Creates a zoom transition from the view that the source provider specifies.
- [UIViewController.Transition.ZoomOptions](uiviewcontroller/transition/zoomoptions.md)
  Options for a zoom transition.
- [UIViewController.Transition.ZoomSourceViewProviderContext](uiviewcontroller/transition/zoomsourceviewprovidercontext.md)
  A context object that contains references to the view controllers from a zoom transition.
### Accessing transitions
- [static var coverVertical: Self](uiviewcontroller/transition/coververtical.md)
  A transition where the new view slides up from the bottom of the screen.
- [static var crossDissolve: Self](uiviewcontroller/transition/crossdissolve.md)
  A transition where the current view fades out while the new view fades in at the same time.
- [static var flipHorizontal: Self](uiviewcontroller/transition/fliphorizontal.md)
  A transition where the current view flips horizontally to reveal the new view.
- [static var partialCurl: Self](uiviewcontroller/transition/partialcurl.md)
  A transition where one corner of the current view curls up, revealing the new view underneath.
### Type Methods
- [static func zoom(options: UIViewController.Transition.ZoomOptions?, sourceBarButtonItemProvider: (UIViewController.Transition.ZoomSourceViewProviderContext) -> UIBarButtonItem?) -> Self](uiviewcontroller/transition/zoom(options:sourcebarbuttonitemprovider:).md)

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

- [var preferredTransition: UIViewController.Transition?](uiviewcontroller/preferredtransition.md)
  An object that defines the transition animation when switching to the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/transition)*