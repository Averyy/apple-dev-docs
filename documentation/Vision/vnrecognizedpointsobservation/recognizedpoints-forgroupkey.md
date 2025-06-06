# recognizedPoints(forGroupKey:)

**Framework**: Vision  
**Kind**: method

Retrieves the recognized points for a key.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func recognizedPoints(forGroupKey groupKey: VNRecognizedPointGroupKey) throws -> [VNRecognizedPointKey : VNRecognizedPoint]
```

#### Return Value

A dictionary of labeled points for the group.

## Parameters

- `groupKey`: The group key to retrieve recognized points for.

## See Also

- [var availableKeys: [VNRecognizedPointKey]](vnrecognizedpointsobservation/availablekeys.md)
  The available point keys in the observation.
- [var availableGroupKeys: [VNRecognizedPointGroupKey]](vnrecognizedpointsobservation/availablegroupkeys.md)
  The available point group keys in the observation.
- [func recognizedPoint(forKey: VNRecognizedPointKey) throws -> VNRecognizedPoint](vnrecognizedpointsobservation/recognizedpoint(forkey:).md)
  Retrieves a recognized point for a key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizedpointsobservation/recognizedpoints(forgroupkey:))*