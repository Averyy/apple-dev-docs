# setLiveView(_:)

**Framework**: Playground Support  
**Kind**: instm

Displays a view that shows the result of running the code that’s on the current page.

**Availability**:
- macOS 11.0+
- Xcode 12.0+
- Swift Playgrounds 4.0+

## Declaration

```swift
func setLiveView<IncomingView>(_ newLiveView: IncomingView) where IncomingView : PlaygroundLiveViewable
```

#### Discussion

The live view appears in the assistant editor for the current playground page. There can be only one live view open at any time.

When you call [`setLiveView(_:)`](playgroundpage/3375752-setliveview.md), the system sets [`needsIndefiniteExecution`](playgroundpage/1964501-needsindefiniteexecution.md) to `true`.

## Parameters

- `newLiveView`: The view to display as the current page’s live view.

## See Also

- [static let current: PlaygroundPage](playgroundpage/1964509-current.md)
  The current playground page.
- [func setLiveView<IncomingView>(IncomingView)](playgroundpage/3375751-setliveview.md)
  Displays a SwiftUI view that shows the result of running the code that’s on the current page.
- [var liveView: (any PlaygroundLiveViewable)?](playgroundpage/1964506-liveview.md)
  A live view that shows the result of running the code that’s on the current page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundsupport/playgroundpage/3375752-setliveview)*