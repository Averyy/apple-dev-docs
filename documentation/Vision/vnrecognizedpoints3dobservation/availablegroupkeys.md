# availableGroupKeys

**Framework**: Vision  
**Kind**: property

The available point group keys in the observation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var availableGroupKeys: [VNRecognizedPointGroupKey] { get }
```

## See Also

- [var availableKeys: [VNRecognizedPointKey]](vnrecognizedpoints3dobservation/availablekeys.md)
  The available point keys in the observation.
- [func recognizedPoint(forKey: VNRecognizedPointKey) throws -> VNRecognizedPoint3D](vnrecognizedpoints3dobservation/recognizedpoint(forkey:).md)
  Returns a point for a key you specify.
- [func recognizedPoints(forGroupKey: VNRecognizedPointGroupKey) throws -> [VNRecognizedPointKey : VNRecognizedPoint3D]](vnrecognizedpoints3dobservation/recognizedpoints(forgroupkey:).md)
  Returns a point for a group key you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizedpoints3dobservation/availablegroupkeys)*