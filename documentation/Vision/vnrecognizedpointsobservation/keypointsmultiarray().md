# keypointsMultiArray()

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Retrieves the grouping of normalized point coordinates and confidence scores in a format compatible with Core ML.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func keypointsMultiArray() throws -> MLMultiArray
```

```objc
- (MLMultiArray *) keypointsMultiArrayAndReturnError:(NSError **) error;
```

#### Return Value

The key points converted to an [`MLMultiArray`](../../CoreML/mlmultiarray.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizedpointsobservation/keypointsmultiarray())*