# recognizedPoint(forKey:)

**Framework**: Vision  
**Kind**: method

Retrieves a recognized point for a key.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func recognizedPoint(forKey pointKey: VNRecognizedPointKey) throws -> VNRecognizedPoint
```

#### Return Value

The recognized point associated with the key.

## Parameters

- `pointKey`: The key of the point to retrieve.

## See Also

- [var availableKeys: [VNRecognizedPointKey]](vnrecognizedpointsobservation/availablekeys.md)
  The available point keys in the observation.
- [var availableGroupKeys: [VNRecognizedPointGroupKey]](vnrecognizedpointsobservation/availablegroupkeys.md)
  The available point group keys in the observation.
- [func recognizedPoints(forGroupKey: VNRecognizedPointGroupKey) throws -> [VNRecognizedPointKey : VNRecognizedPoint]](vnrecognizedpointsobservation/recognizedpoints(forgroupkey:).md)
  Retrieves the recognized points for a key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizedpointsobservation/recognizedpoint(forkey:))*