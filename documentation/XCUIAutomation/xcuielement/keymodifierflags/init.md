# init(_:)

**Framework**: XCUIAutomation  
**Kind**: init

Creates a new set from a finite sequence of items.

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
init<S>(_ sequence: S) where S : Sequence, Self.Element == S.Element
```

#### Discussion

Use this initializer to create a new set from an existing sequence, like an array or a range:

```None
let validIndices = Set(0..<7).subtracting([2, 4, 5])
print(validIndices)
// Prints "[6, 0, 1, 3]"
```

## Parameters

- `sequence`: The elements to use as members of the new set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/keymodifierflags/init(_:))*