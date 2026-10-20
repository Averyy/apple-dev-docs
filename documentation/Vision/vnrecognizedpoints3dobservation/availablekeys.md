# availableKeys

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly) NSArray<NSString *> * availableKeys;
```

## See Also

### Inspecting the Observation
- [var availableGroupKeys: [VNRecognizedPointGroupKey]](./availablegroupkeys.md)
  The available point group keys in the observation.
- [func recognizedPoint(forKey: VNRecognizedPointKey) throws -> VNRecognizedPoint3D](./recognizedpoint%28forkey%29.md)
  Returns a point for a key you specify.
- [func recognizedPoints(forGroupKey: VNRecognizedPointGroupKey) throws -> [VNRecognizedPointKey : VNRecognizedPoint3D]](./recognizedpoints%28forgroupkey%29.md)
  Returns a point for a group key you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizedpoints3dobservation/availablekeys)*