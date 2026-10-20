# PlaygroundLiveViewable

**Framework**: Playground Support  
**Kind**: intf  
**Role**: Protocol

A protocol that displays an instance as a live view in a playground.

**Availability**:
- macOS 11.0+
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
protocol PlaygroundLiveViewable
```

#### Overview

A playground that presents a simplified user interface programming environment, for example, can make its view-like type conform to [`PlaygroundLiveViewable`](./playgroundliveviewable.md) and appear in the live view. By default, [`UIView`](../UIKit/uiview.md) and [`UIViewController`](../UIKit/uiviewcontroller.md) conform to this protocol in iOS and tvOS, and [`NSView`](../AppKit/nsview.md) and [`NSViewController`](../AppKit/nsviewcontroller.md) conform to this protocol in macOS. You only need to implement this protocol for custom objects that don't already inherit from [`UIView`](../UIKit/uiview.md), [`UIViewController`](../UIKit/uiviewcontroller.md), [`NSView`](../AppKit/nsview.md), or [`NSViewController`](../AppKit/nsviewcontroller.md).

## Topics

### Displaying Types
- [var playgroundLiveViewRepresentation: PlaygroundLiveViewRepresentation](./playgroundliveviewable/api-1978828-playgroundliveviewrepresentation.md)
  The view or view controller used to render and manage the live view.

## Relationships

### Conforming Types
- [PlaygroundRemoteLiveViewProxy](./playgroundremoteliveviewproxy.md)

## See Also

### Live Views
- [enum PlaygroundLiveViewRepresentation](./playgroundliveviewrepresentation.md)
  The supported types for displaying for live views in playgrounds.
- [protocol PlaygroundLiveViewSafeAreaContainer](./playgroundliveviewsafeareacontainer.md)
  A protocol that ensures that views fit without obstruction within the Swift Playgrounds user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundsupport/playgroundliveviewable)*