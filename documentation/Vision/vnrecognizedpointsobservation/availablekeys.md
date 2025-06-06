# availableKeys

**Framework**: Vision  
**Kind**: property

The available point keys in the observation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var availableKeys: [VNRecognizedPointKey] { get }
```

## See Also

- [var availableGroupKeys: [VNRecognizedPointGroupKey]](vnrecognizedpointsobservation/availablegroupkeys.md)
  The available point group keys in the observation.
- [func recognizedPoint(forKey: VNRecognizedPointKey) throws -> VNRecognizedPoint](vnrecognizedpointsobservation/recognizedpoint(forkey:).md)
  Retrieves a recognized point for a key.
- [func recognizedPoints(forGroupKey: VNRecognizedPointGroupKey) throws -> [VNRecognizedPointKey : VNRecognizedPoint]](vnrecognizedpointsobservation/recognizedpoints(forgroupkey:).md)
  Retrieves the recognized points for a key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizedpointsobservation/availablekeys)*