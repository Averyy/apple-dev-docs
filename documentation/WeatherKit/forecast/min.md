# min()

**Framework**: Weatherkit  
**Kind**: method

Returns the minimum element in the sequence.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@warn_unqualified_access
func min() -> Self.Element?
```

#### Return Value

The sequence’s minimum element. If the sequence has no elements, returns `nil`.

#### Discussion

This example finds the smallest value in an array of height measurements.

```None
let heights = [67.5, 65.7, 64.3, 61.1, 58.5, 60.3, 64.9]
let lowestHeight = heights.min()
print(lowestHeight)
// Prints "Optional(58.5)"
```

> **Note**: O(), where  is the length of the sequence.

O(), where  is the length of the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/forecast/min())*