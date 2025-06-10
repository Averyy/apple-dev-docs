# formSymmetricDifference(_:)

**Framework**: XCUIAutomation  
**Kind**: method

Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.

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
mutating func formSymmetricDifference(_ other: Self)
```

#### Discussion

This method is implemented as a `^` (bitwise XOR) operation on the two sets’ raw values.

## Parameters

- `other`: An option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/keymodifierflags/formsymmetricdifference(_:))*