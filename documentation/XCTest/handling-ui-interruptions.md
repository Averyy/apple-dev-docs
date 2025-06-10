# Handling UI Interruptions

**Framework**: XCTest

Improve your UI test’s stability by handling interface changes that block the UI elements under test.

#### Overview

Use XCTestCase UI interruption monitors to handle situations in which unrelated UI elements might appear and block the test’s interaction with elements in the workflow under test. The following situations could result in a blocked test:

- Your app presents a modal view that takes focus away from the UI under test, as can happen, for example, when a background task fails and you notify the user of the failure.
- Your app performs an action that causes the operating system to present a modal UI. An example is an action that presents a photo picker, which may make the system request access to photos if the user hasn’t already granted it.

> ❗ **Important**:  When an alert or other modal UI is an expected part of the test workflow, don’t write a UI interruption monitor. The test won’t use the monitor because the modal UI isn’t blocking the test. A UI test only tries its UI interruption monitors if the elements it needs to interact with to complete the test are blocked by an interruption from an unrelated UI.

##### Add a Ui Interruption Monitor to Your Test

Call [`addUIInterruptionMonitor(withDescription:handler:)`](xctestcase/adduiinterruptionmonitor(withdescription:handler:).md) with a block that handles the interrupting UI and gets the test back on its expected path. Your block should return `true` if it clears the interruption, and `false` otherwise. UI interruption monitors are stored in a stack and their blocks are tried in last-in, first-out order, so returning `false` gives other interruption monitors the chance to run.

`XCTest` removes added UI interruption monitors when the test completes, so it’s not necessary to explicitly remove them. However, if you need to remove a monitor during test execution, call [`removeUIInterruptionMonitor(_:)`](xctestcase/removeuiinterruptionmonitor(_:).md).

## See Also

- [func addUIInterruptionMonitor(withDescription: String, handler: (XCUIElement) -> Bool) -> any NSObjectProtocol](xctestcase/adduiinterruptionmonitor(withdescription:handler:).md)
  Adds a handler to the current context.
- [func removeUIInterruptionMonitor(any NSObjectProtocol)](xctestcase/removeuiinterruptionmonitor(_:).md)
  Removes a handler using the token from when you added the handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/handling-ui-interruptions)*