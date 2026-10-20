# liveView

**Framework**: Playground Support  
**Kind**: instp  
**Role**: Instance Property

A live view that shows the result of running the code that’s on the current page.

**Availability**:
- macOS 11.0+
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

*macOS*

```swift
final var liveView: (any PlaygroundLiveViewable)? { get set }
```

*Swift Playgrounds*

```swift
var liveView: PlaygroundLiveViewable? { get set }
```

#### Discussion

Display a live view by setting [`liveView`](./api-1964506-liveview.md) to an object that conforms to the [`PlaygroundLiveViewable`](../playgroundliveviewable.md) protocol. Dismiss any open live view by setting [`liveView`](./api-1964506-liveview.md) to `nil`.

The live view is displayed in the assistant editor for the current playground page. There can be only one live view open at any time.

Displaying the live view requires that [`needsIndefiniteExecution`](./api-1964501-needsindefiniteexecution.md) be set to [`true`](../../Swift/true.md). When [`liveView`](./api-1964506-liveview.md) is set to a non-`nil` value, the system sets [`needsIndefiniteExecution`](./api-1964501-needsindefiniteexecution.md) to [`true`](../../Swift/true.md).

## See Also

### Configuring Live Views
- [static let current: PlaygroundPage](./api-1964509-current.md)
  The current playground page.
- [func setLiveView<IncomingView>(IncomingView)](./api-3375751-setliveview.md)
  Displays a SwiftUI view that shows the result of running the code that’s on the current page.
- [func setLiveView<IncomingView>(IncomingView)](./api-3375752-setliveview.md)
  Displays a view that shows the result of running the code that’s on the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundsupport/playgroundpage/1964506-liveview)*