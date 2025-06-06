# removingSubranges(_:)

**Framework**: Weatherkit  
**Kind**: method

Returns a collection of the elements in this collection that are not represented by the given range set.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func removingSubranges(_ subranges: RangeSet<Self.Index>) -> DiscontiguousSlice<Self>
```

#### Return Value

A collection of the elements that are not in `subranges`.

#### Discussion

For example, this code sample finds the indices of all the vowel characters in the string, and then retrieves a collection that omits those characters.

```None
let str = "The rain in Spain stays mainly in the plain."
let vowels: Set<Character> = ["a", "e", "i", "o", "u"]
let vowelIndices = str.subranges(where: { vowels.contains($0) })

let disemvoweled = str.removingSubranges(vowelIndices)
print(String(disemvoweled))
// Prints "Th rn n Spn stys mnly n th pln."
```

> **Note**: O(), where  is the length of the collection.

## Parameters

- `subranges`: A range set representing the indices of the   elements to remove.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatherchanges/removingsubranges(_:))*