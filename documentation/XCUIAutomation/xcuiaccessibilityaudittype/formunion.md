# formUnion(_:)

**Framework**: XCUIAutomation  
**Kind**: method

Inserts the elements of another set into this option set.

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
mutating func formUnion(_ other: Self)
```

#### Discussion

This method is implemented as a `|` (bitwise OR) operation on the two sets’ raw values.

## Parameters

- `other`: An option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiaccessibilityaudittype/formunion(_:))*