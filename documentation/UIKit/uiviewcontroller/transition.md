# UIViewController.Transition

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UIViewControllerTransition : NSObject
```

## Topics

### Creating zoom transitions
- [static func zoom(options: UIViewController.Transition.ZoomOptions?, sourceViewProvider: (UIViewController.Transition.ZoomSourceViewProviderContext) -> UIView?) -> Self](./transition/zoom%28options,sourceviewprovider%29.md)
  Creates a zoom transition from the view that the source provider specifies.
- [UIViewController.Transition.ZoomOptions](./transition/zoomoptions.md)
  Options for a zoom transition.
- [UIViewController.Transition.ZoomSourceViewProviderContext](./transition/zoomsourceviewprovidercontext.md)
  A context object that contains references to the view controllers from a zoom transition.
- [+ zoomWithOptions:sourceViewProvider:](../uiviewcontrollertransition/zoomwithoptions_sourceviewprovider_.md)
  Creates a zoom transition from the view specified by the source provider.
### Accessing transitions
- [static var coverVertical: Self](./transition/coververtical.md)
  A transition where the new view slides up from the bottom of the screen.
- [static var crossDissolve: Self](./transition/crossdissolve.md)
  A transition where the current view fades out while the new view fades in at the same time.
- [static var flipHorizontal: Self](./transition/fliphorizontal.md)
  A transition where the current view flips horizontally to reveal the new view.
- [static var partialCurl: Self](./transition/partialcurl.md)
  A transition where one corner of the current view curls up, revealing the new view underneath.
- [+ coverVerticalTransition](../uiviewcontrollertransition/coververticaltransition.md)
  A transition where the new view slides up from the bottom of the screen.
- [+ crossDissolveTransition](../uiviewcontrollertransition/crossdissolvetransition.md)
  A transition where the current view fades out while the new view fades in at the same time.
- [+ flipHorizontalTransition](../uiviewcontrollertransition/fliphorizontaltransition.md)
  A transition where the current view flips horizontally to reveal the new view.
- [+ partialCurlTransition](../uiviewcontrollertransition/partialcurltransition.md)
  A transition where one corner of the current view curls up, revealing the new view underneath.
### Type Methods
- [static func zoom(options: UIViewController.Transition.ZoomOptions?, sourceBarButtonItemProvider: (UIViewController.Transition.ZoomSourceViewProviderContext) -> UIBarButtonItem?) -> Self](./transition/zoom%28options,sourcebarbuttonitemprovider%29.md)
- [+ zoomWithOptions:sourceBarButtonItemProvider:](../uiviewcontrollertransition/zoomwithoptions_sourcebarbuttonitemprovider_.md)
  Zoom from the `UIBarButtonItem` provided by the `sourceBarButtonItemProvider` to the presented or pushed view controller’s view.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Working with transitions
- [var preferredTransition: UIViewController.Transition?](./preferredtransition.md)
  An object that defines the transition animation when switching to the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/transition)*