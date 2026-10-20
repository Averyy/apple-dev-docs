# UIViewController.Transition.ZoomOptions

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

Options for a zoom transition.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
class ZoomOptions
```

```objc
@interface UIZoomTransitionOptions : NSObject
```

## Topics

### Setting options
- [var alignmentRectProvider: ((UIViewController.Transition.ZoomOptions.AlignmentRectContext) -> CGRect?)?](./zoomoptions/alignmentrectprovider.md)
  A closure that returns the alignment rectangle for the starting and ending views.
- [UIViewController.Transition.ZoomOptions.AlignmentRectContext](./zoomoptions/alignmentrectcontext.md)
  An object that contains a zoom transition’s starting and ending views.
- [var dimmingColor: UIColor?](./zoomoptions/dimmingcolor.md)
  The dimming color.
- [var dimmingVisualEffect: UIBlurEffect?](./zoomoptions/dimmingvisualeffect.md)
  The dimming visual effect.
### Accessing the animation state
- [var interactiveDismissShouldBegin: ((UIViewController.Transition.ZoomOptions.InteractionContext) -> Bool)?](./zoomoptions/interactivedismissshouldbegin.md)
  A closure that determines whether an interactive dismissal can begin.
- [UIViewController.Transition.ZoomOptions.InteractionContext](./zoomoptions/interactioncontext.md)
  Data you can use to determine whether an interactive dismissal can begin.

## Relationships

### Inherits From
- [NSObject](../../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [NSCopying](../../../Foundation/nscopying.md)
- [NSObjectProtocol](../../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating zoom transitions
- [static func zoom(options: UIViewController.Transition.ZoomOptions?, sourceViewProvider: (UIViewController.Transition.ZoomSourceViewProviderContext) -> UIView?) -> Self](./zoom%28options,sourceviewprovider%29.md)
  Creates a zoom transition from the view that the source provider specifies.
- [UIViewController.Transition.ZoomSourceViewProviderContext](./zoomsourceviewprovidercontext.md)
  A context object that contains references to the view controllers from a zoom transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/transition/zoomoptions)*