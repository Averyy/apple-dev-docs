# first

**Framework**: Weatherkit  
**Kind**: property

The first element of the collection.

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
var first: Self.Element? { get }
```

#### Discussion

If the collection is empty, the value of this property is `nil`.

```None
let numbers = [10, 20, 30, 40, 50]
if let firstNumber = numbers.first {
    print(firstNumber)
}
// Prints "10"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/historicalcomparisons/first)*