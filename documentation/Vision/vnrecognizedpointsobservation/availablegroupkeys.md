# availableGroupKeys

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly) NSArray<NSString *> * availableGroupKeys;
```

## See Also

### Inspecting the Observation
- [var availableKeys: [VNRecognizedPointKey]](./availablekeys.md)
  The available point keys in the observation.
- [func recognizedPoint(forKey: VNRecognizedPointKey) throws -> VNRecognizedPoint](./recognizedpoint%28forkey%29.md)
  Retrieves a recognized point for a key.
- [func recognizedPoints(forGroupKey: VNRecognizedPointGroupKey) throws -> [VNRecognizedPointKey : VNRecognizedPoint]](./recognizedpoints%28forgroupkey%29.md)
  Retrieves the recognized points for a key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizedpointsobservation/availablegroupkeys)*