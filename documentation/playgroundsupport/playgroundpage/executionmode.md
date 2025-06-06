# PlaygroundPage.ExecutionMode

**Framework**: Playground Support  
**Kind**: enum

The available speeds for executing the code on a playground page.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
enum PlaygroundPage.ExecutionMode
```

#### Overview

The [`PlaygroundPage.ExecutionMode.run`](playgroundpage/executionmode/run.md), [`PlaygroundPage.ExecutionMode.runFaster`](playgroundpage/executionmode/runfaster.md), and [`PlaygroundPage.ExecutionMode.runFastest`](playgroundpage/executionmode/runfastest.md) modes all execute code immediately. The [`PlaygroundPage.ExecutionMode.step`](playgroundpage/executionmode/step.md) and [`PlaygroundPage.ExecutionMode.stepSlowly`](playgroundpage/executionmode/stepslowly.md) modes execute  code statement by statement, highlighting each statement on the page as it's executed.

For faster execution, explicitly support the [`PlaygroundPage.ExecutionMode.runFaster`](playgroundpage/executionmode/runfaster.md) and [`PlaygroundPage.ExecutionMode.runFastest`](playgroundpage/executionmode/runfastest.md) modes in your live view code. These modes signal to you that the learner wants the live view to show progress faster than the normal speed. These execution options aren't displayed to the learner unless you opt in by adding the `MaximumSupportedExecutionSpeed` key to a page's manifest property list. Set the key to `Faster` or `Fastest`, depending on how many speeds your live view supports.

## Topics

### Controlling Execution Speed
- [PlaygroundPage.ExecutionMode.run](playgroundpage/executionmode/run.md)
  An execution mode that runs at the normal speed.
- [PlaygroundPage.ExecutionMode.runFaster](playgroundpage/executionmode/runfaster.md)
  An execution mode that runs more quickly than usual.
- [PlaygroundPage.ExecutionMode.runFastest](playgroundpage/executionmode/runfastest.md)
  An execution mode that runs at the fastest possible speed.
### Stepping Through Code
- [PlaygroundPage.ExecutionMode.step](playgroundpage/executionmode/step.md)
  An execution mode that executes code statement by statement.
- [PlaygroundPage.ExecutionMode.stepSlowly](playgroundpage/executionmode/stepslowly.md)
  An execution mode that executes code statement by statement with extra pauses between each.
### Comparing Modes
- [static func != (PlaygroundPage.ExecutionMode, PlaygroundPage.ExecutionMode) -> Bool](playgroundpage/executionmode/3029554.md)
  Returns `true` when the execution modes being compared are different.

## See Also

- [var executionMode: PlaygroundPage.ExecutionMode](playgroundpage/3029561-executionmode.md)
  The currently selected speed for executing the code on this playground page.
- [var needsIndefiniteExecution: Bool](playgroundpage/1964501-needsindefiniteexecution.md)
  A Boolean value that indicates whether indefinite execution is enabled.
- [func finishExecution() -> Never](playgroundpage/1964505-finishexecution.md)
  Terminates execution of the current playground page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundsupport/playgroundpage/executionmode)*