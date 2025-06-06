# PlaygroundLiveViewSafeAreaContainer

**Framework**: Playground Support  
**Kind**: intf

A protocol that ensures that views fit without obstruction within the Swift Playgrounds user interface.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
protocol PlaygroundLiveViewSafeAreaContainer : AnyObject
```

#### Overview

This protocol provides [`liveViewSafeAreaGuide`](playgroundliveviewsafeareacontainer/3029546-liveviewsafeareaguide.md), a layout guide set to the safe area. The  is the part of the live view that isn't covered by any Swift Playgrounds user interface elements like the Run button. You use this property to constrain the bounds of your content view inside the bounds of the safe area, which depend on how you set the `LiveViewEdgeToEdge` key for the current page. When this key is set to `NO`, the safe area is exactly the same as the live view area. When the key is set to `YES`, the safe area can be smaller than the live view area.

![Side-by-side screenshots showing how the safe area can be larger or smaller depending on how you set the LiveViewEdgeToEdge key.](https://docs-assets.developer.apple.com/published/53bde67707/3036821@2x.png)

## Topics

### Accessing the Layout Guide
- [var liveViewSafeAreaGuide: UILayoutGuide](playgroundliveviewsafeareacontainer/3029546-liveviewsafeareaguide.md)
  A layout guide you use to position content so that it's unobstructed by the Swift Playgrounds user interface.

## See Also

- [protocol PlaygroundLiveViewable](playgroundliveviewable.md)
  A protocol that displays an instance as a live view in a playground.
- [enum PlaygroundLiveViewRepresentation](playgroundliveviewrepresentation.md)
  The supported types for displaying for live views in playgrounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundsupport/playgroundliveviewsafeareacontainer)*