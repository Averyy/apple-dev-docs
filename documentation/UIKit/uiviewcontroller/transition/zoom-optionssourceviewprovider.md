# zoom(options:sourceViewProvider:)

**Framework**: UIKit  
**Kind**: method

Creates a zoom transition from the view that the source provider specifies.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
static func zoom(options: UIViewController.Transition.ZoomOptions? = nil, sourceViewProvider: @escaping (UIViewController.Transition.ZoomSourceViewProviderContext) -> UIView?) -> Self
```

## Mentions

- [Enhancing your app with fluid transitions](enhancing-your-app-with-fluid-transitions.md)

#### Discussion

The system calls the source view provider when it presents and when it dismisses the view controller. In the closure, return the [`UIView`](uiview.md) that the animation should zoom in from or zoom back out to, respectively. For more information, see [`Enhancing your app with fluid transitions`](enhancing-your-app-with-fluid-transitions.md).

## Parameters

- `options`: Additional options for the zoom transition.
- `sourceViewProvider`: A closure that returns the view, for example a thumbnail image, that the animation zooms out from and zooms back in to.

## See Also

- [UIViewController.Transition.ZoomOptions](uiviewcontroller/transition/zoomoptions.md)
  Options for a zoom transition.
- [UIViewController.Transition.ZoomSourceViewProviderContext](uiviewcontroller/transition/zoomsourceviewprovidercontext.md)
  A context object that contains references to the view controllers from a zoom transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/transition/zoom(options:sourceviewprovider:))*