# suffix(from:)

**Framework**: hvf  
**Kind**: method

Returns a subsequence from the specified position to the end of the collection.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func suffix(from start: Self.Index) -> Self.SubSequence
```

#### Return Value

A subsequence starting at the `start` position.

#### Discussion

The following example searches for the index of the number `40` in an array of integers, and then prints the suffix of the array starting at that index:

```None
let numbers = [10, 20, 30, 40, 50, 60]
if let i = numbers.firstIndex(of: 40) {
    print(numbers.suffix(from: i))
}
// Prints "[40, 50, 60]"
```

Passing the collection’s `endIndex` as the `start` parameter results in an empty subsequence.

```None
print(numbers.suffix(from: numbers.endIndex))
// Prints "[]"
```

Using the `suffix(from:)` method is equivalent to using a partial range from the index as the collection’s subscript. The subscript notation is preferred over `suffix(from:)`.

```None
if let i = numbers.firstIndex(of: 40) {
    print(numbers[i...])
}
// Prints "[40, 50, 60]"
```

> **Note**: O(1)

## Parameters

- `start`: The index at which to start the resulting subsequence.    must be a valid index of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/partrenderer/axisvalues/suffix(from:))*