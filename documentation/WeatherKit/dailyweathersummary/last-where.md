# last(where:)

**Framework**: Weatherkit  
**Kind**: method

Returns the last element of the sequence that satisfies the given predicate.

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
func last(where predicate: (Self.Element) throws -> Bool) rethrows -> Self.Element?
```

#### Return Value

The last element of the sequence that satisfies `predicate`, or `nil` if there is no element that satisfies `predicate`.

#### Discussion

This example uses the `last(where:)` method to find the last negative number in an array of integers:

```None
let numbers = [3, 7, 4, -2, 9, -6, 10, 1]
if let lastNegative = numbers.last(where: { $0 < 0 }) {
    print("The last negative number is \(lastNegative).")
}
// Prints "The last negative number is -6."
```

> **Note**: O(), where  is the length of the collection.

O(), where  is the length of the collection.

## Parameters

- `predicate`: A closure that takes an element of the sequence as   its argument and returns a Boolean value indicating whether the   element is a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/dailyweathersummary/last(where:))*