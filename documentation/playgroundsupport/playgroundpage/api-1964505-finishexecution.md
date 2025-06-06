# finishExecution()

**Framework**: Playground Support  
**Kind**: instm

Terminates execution of the current playground page.

**Availability**:
- macOS 11.0+
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
func finishExecution() -> Never
```

#### Discussion

This function immediately terminates any code running in the playground. Call this function when you've set [`needsIndefiniteExecution`](playgroundpage/1964501-needsindefiniteexecution.md) to `true` to indicate that the indefinite period of code execution has ended.

## See Also

- [var executionMode: PlaygroundPage.ExecutionMode](playgroundpage/3029561-executionmode.md)
  The currently selected speed for executing the code on this playground page.
- [enum PlaygroundPage.ExecutionMode](playgroundpage/executionmode.md)
  The available speeds for executing the code on a playground page.
- [var needsIndefiniteExecution: Bool](playgroundpage/1964501-needsindefiniteexecution.md)
  A Boolean value that indicates whether indefinite execution is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundsupport/playgroundpage/1964505-finishexecution)*