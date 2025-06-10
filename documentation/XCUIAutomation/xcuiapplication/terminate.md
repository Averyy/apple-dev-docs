# terminate()

**Framework**: XCUIAutomation  
**Kind**: method

Terminates any running instance of the application.

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
func terminate()
```

#### Discussion

If the application has an existing debug session via Xcode, the debugger sends a command to terminate the application. Otherwise, an appropriate platform-specific mechanism terminates the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/terminate())*