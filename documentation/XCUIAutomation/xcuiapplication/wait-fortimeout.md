# wait(for:timeout:)

**Framework**: Xcuiautomation  
**Kind**: method

Waits for the application to reach the specified state or timeout.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
func wait(for state: XCUIApplication.State, timeout: TimeInterval) -> Bool
```

#### Return Value

A Boolean value that indicates whether the app is in the specified state, or can reach the specified state before the timeout.

## Parameters

- `state`: The requested application state.
- `timeout`: The amount of time to wait, in seconds, for the application to reach the requested application state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/wait(for:timeout:))*