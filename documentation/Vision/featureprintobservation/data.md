# data

**Framework**: Vision  
**Kind**: property

The feature print data.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
let data: Data
```

#### Discussion

Vision divides the data into separate elements. Determine the type of element using `elementType`, and the number of elements using `elementCount`.

## See Also

- [let elementCount: Int](featureprintobservation/elementcount.md)
  The total number of elements in the data.
- [let elementType: ElementType](featureprintobservation/elementtype.md)
  The type of each element in the data.
- [enum ElementType](elementtype.md)
  The type of element in feature print data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/featureprintobservation/data)*