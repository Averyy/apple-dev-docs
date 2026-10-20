# recognizedPoint(forKey:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Returns a point for a key you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func recognizedPoint(forKey pointKey: VNRecognizedPointKey) throws -> VNRecognizedPoint3D
```

```objc
- (VNRecognizedPoint3D *) recognizedPointForKey:(VNRecognizedPointKey) pointKey error:(NSError **) error;
```

#### Return Value

The point the observation associates with the key.

## Parameters

- `pointKey`: The key of the point to retrieve.

## See Also

### Inspecting the Observation
- [var availableKeys: [VNRecognizedPointKey]](./availablekeys.md)
  The available point keys in the observation.
- [var availableGroupKeys: [VNRecognizedPointGroupKey]](./availablegroupkeys.md)
  The available point group keys in the observation.
- [func recognizedPoints(forGroupKey: VNRecognizedPointGroupKey) throws -> [VNRecognizedPointKey : VNRecognizedPoint3D]](./recognizedpoints%28forgroupkey%29.md)
  Returns a point for a group key you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizedpoints3dobservation/recognizedpoint(forkey:))*