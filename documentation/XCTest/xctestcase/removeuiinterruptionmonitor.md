# removeUIInterruptionMonitor(_:)

**Framework**: XCTest  
**Kind**: method

Removes a handler using the token from when you added the handler.

## Declaration

```swift
func removeUIInterruptionMonitor(_ monitor: any NSObjectProtocol)
```

## Mentions

- [Handling UI Interruptions](handling-ui-interruptions.md)

## Parameters

- `monitor`: An identifier token for an interruption monitor, obtained from a previous call to  .

## See Also

- [Handling UI Interruptions](handling-ui-interruptions.md)
  Improve your UI test’s stability by handling interface changes that block the UI elements under test.
- [func addUIInterruptionMonitor(withDescription: String, handler: (XCUIElement) -> Bool) -> any NSObjectProtocol](xctestcase/adduiinterruptionmonitor(withdescription:handler:).md)
  Adds a handler to the current context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/removeuiinterruptionmonitor(_:))*