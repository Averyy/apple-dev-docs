# starts(with:)

**Framework**: WeatherKit  
**Kind**: method

Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.

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
func starts<PossiblePrefix>(with possiblePrefix: PossiblePrefix) -> Bool where PossiblePrefix : Sequence, Self.Element == PossiblePrefix.Element
```

#### Return Value

`true` if the initial elements of the sequence are the same as the elements of `possiblePrefix`; otherwise, `false`. If `possiblePrefix` has no elements, the return value is `true`.

#### Discussion

This example tests whether one countable range begins with the elements of another countable range.

```None
let a = 1...3
let b = 1...10

print(b.starts(with: a))
// Prints "true"
```

Passing a sequence with no elements or an empty collection as `possiblePrefix` always results in `true`.

```None
print(b.starts(with: []))
// Prints "true"
```

> **Note**: O(), where  is the lesser of the length of the sequence and the length of `possiblePrefix`.

## Parameters

- `possiblePrefix`: A sequence to compare to this sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/hourlyweatherstatistics/starts(with:))*