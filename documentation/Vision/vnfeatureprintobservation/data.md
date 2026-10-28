# data

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The feature print data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var data: Data { get }
```

```objc
@property (atomic, strong, readonly) NSData * data;
```

## Discussion

The data is divided into separate elements. Determine the type of element using [`elementType`](./elementtype.md), and the number of elements using [`elementCount`](./elementcount.md).

## See Also

### Fetching Feature Print Data
- [var elementCount: Int](./elementcount.md)
  The total number of elements in the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnfeatureprintobservation/data)*