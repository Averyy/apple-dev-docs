# recognizedPoints(forGroupKey:)

**Framework**: Vision  
**Kind**: method

Returns a point for a group key you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func recognizedPoints(forGroupKey groupKey: VNRecognizedPointGroupKey) throws -> [VNRecognizedPointKey : VNRecognizedPoint3D]
```

#### Return Value

A dictionary of labeled points for the group.

## Parameters

- `groupKey`: The group key to retrieve points for.

## See Also

- [var availableKeys: [VNRecognizedPointKey]](vnrecognizedpoints3dobservation/availablekeys.md)
  The available point keys in the observation.
- [var availableGroupKeys: [VNRecognizedPointGroupKey]](vnrecognizedpoints3dobservation/availablegroupkeys.md)
  The available point group keys in the observation.
- [func recognizedPoint(forKey: VNRecognizedPointKey) throws -> VNRecognizedPoint3D](vnrecognizedpoints3dobservation/recognizedpoint(forkey:).md)
  Returns a point for a key you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizedpoints3dobservation/recognizedpoints(forgroupkey:))*