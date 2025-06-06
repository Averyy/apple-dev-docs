# addUIInterruptionMonitor(withDescription:handler:)

**Framework**: Xctest  
**Kind**: method

Adds a handler to the current context.

## Declaration

```swift
func addUIInterruptionMonitor(withDescription handlerDescription: String, handler: @escaping (XCUIElement) -> Bool) -> any NSObjectProtocol
```

## Mentions

- [Handling UI Interruptions](handling-ui-interruptions.md)

#### Return Value

Returns a token that can be used to unregister the handler. Handlers are invoked in the reverse order in which they are added until one of the handlers returns true, indicating that it has handled the alert.

## Parameters

- `handlerDescription`: An explanation of the behavior and purpose of this handler, mainly used for debugging and analysis.
- `handler`: A handler block for handling asynchronous UI interruptions such as alerts and other dialogs. Handlers should return   if they handled the UI,   if they did not. The handler is passed an   representing the top level UI element for the alert.

## See Also

- [Handling UI Interruptions](handling-ui-interruptions.md)
  Improve your UI test’s stability by handling interface changes that block the UI elements under test.
- [func removeUIInterruptionMonitor(any NSObjectProtocol)](xctestcase/removeuiinterruptionmonitor(_:).md)
  Removes a handler using the token from when you added the handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/adduiinterruptionmonitor(withdescription:handler:))*