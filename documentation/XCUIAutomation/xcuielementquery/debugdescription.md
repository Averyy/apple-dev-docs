# debugDescription

**Framework**: XCUIAutomation  
**Kind**: property

Provides debugging information about the query.

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
var debugDescription: String { get }
```

#### Discussion

The data in the string varies based on the time at which it’s captured, but it may include any of the following as well as additional data:

- A description of each step of the query evaluation
- Information about the inputs and matched outputs of each step of the query

The data this method returns is for debugging your test. Don’t depend on any part the resulting string for test evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielementquery/debugdescription)*