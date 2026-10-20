# needsIndefiniteExecution

**Framework**: Playground Support  
**Kind**: instp  
**Role**: Instance Property

A Boolean value that indicates whether indefinite execution is enabled.

**Availability**:
- macOS 11.0+
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

*macOS*

```swift
final var needsIndefiniteExecution: Bool { get set }
```

*Swift Playgrounds*

```swift
var needsIndefiniteExecution: Bool { get set }
```

#### Discussion

By default, all top-level code is executed, and then execution is terminated. When working with asynchronous code, enable indefinite execution to allow execution to continue after the end of the playground’s top-level code is reached. This, in turn, gives threads and callbacks time to execute.

With a traditional live view, editing the playground automatically stops execution, even when indefinite execution is enabled. When using the always-on live view, execution continues whether or not indefinite execution is enabled.

Set [`needsIndefiniteExecution`](./api-1964501-needsindefiniteexecution.md) to `true` to continue execution after the end of top-level code. Set it to `false` to stop execution at that point.

The default value is [`false`](../../Swift/false.md). It's set to true when [`liveView`](./api-1964506-liveview.md) is set to a non-`nil` value.

## See Also

### Configuring Execution
- [var executionMode: PlaygroundPage.ExecutionMode](./api-3029561-executionmode.md)
  The currently selected speed for executing the code on this playground page.
- [enum PlaygroundPage.ExecutionMode](./executionmode.md)
  The available speeds for executing the code on a playground page.
- [func finishExecution() -> Never](./api-1964505-finishexecution.md)
  Terminates execution of the current playground page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundsupport/playgroundpage/1964501-needsindefiniteexecution)*