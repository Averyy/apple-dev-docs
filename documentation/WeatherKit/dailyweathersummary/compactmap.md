# compactMap(_:)

**Framework**: WeatherKit  
**Kind**: method

Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.

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
func compactMap<ElementOfResult>(_ transform: (Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]
```

#### Return Value

An array of the non-`nil` results of calling `transform` with each element of the sequence.

#### Discussion

Use this method to receive an array of non-optional values when your transformation produces an optional value.

In this example, note the difference in the result of using `map` and `compactMap` with a transformation that returns an optional `Int` value.

```None
let possibleNumbers = ["1", "2", "three", "///4///", "5"]

let mapped: [Int?] = possibleNumbers.map { str in Int(str) }
// [1, 2, nil, nil, 5]

let compactMapped: [Int] = possibleNumbers.compactMap { str in Int(str) }
// [1, 2, 5]
```

> **Note**: O(), where  is the length of this sequence.

## Parameters

- `transform`: A closure that accepts an element of this   sequence as its argument and returns an optional value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/dailyweathersummary/compactmap(_:))*