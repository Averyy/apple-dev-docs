# index(_:offsetBy:limitedBy:)

**Framework**: WeatherKit  
**Kind**: method

Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.

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
func index(_ i: Self.Index, offsetBy distance: Int, limitedBy limit: Self.Index) -> Self.Index?
```

#### Return Value

An index offset by `distance` from the index `i`, unless that index would be beyond `limit` in the direction of movement. In that case, the method returns `nil`.

#### Discussion

The following example obtains an index advanced four positions from an array’s starting index and then prints the element at that position. The operation doesn’t require going beyond the limiting `numbers.endIndex` value, so it succeeds.

```None
let numbers = [10, 20, 30, 40, 50]
let i = numbers.index(numbers.startIndex, offsetBy: 4)
print(numbers[i])
// Prints "50"
```

The next example attempts to retrieve an index ten positions from `numbers.startIndex`, but fails, because that distance is beyond the index passed as `limit`.

```None
let j = numbers.index(numbers.startIndex,
                      offsetBy: 10,
                      limitedBy: numbers.endIndex)
print(j)
// Prints "nil"
```

The value passed as `distance` must not offset `i` beyond the bounds of the collection, unless the index passed as `limit` prevents offsetting beyond those bounds.

> **Note**: O(1)

## Parameters

- `i`: A valid index of the array.
- `distance`: The distance to offset  .
- `limit`: A valid index of the collection to use as a limit. If   ,   should be greater than   to have any   effect. Likewise, if  ,   should be less than    to have any effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/historicalcomparisons/index(_:offsetby:limitedby:))*