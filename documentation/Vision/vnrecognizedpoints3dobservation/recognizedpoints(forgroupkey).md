# recognizedPoints(forGroupKey:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSDictionary<NSString *,VNRecognizedPoint3D *> *) recognizedPointsForGroupKey:(VNRecognizedPointGroupKey) groupKey error:(NSError **) error;
```

## Return Value

A dictionary of labeled points for the group.

## Parameters

- `groupKey`: The group key to retrieve points for.

## See Also

### Inspecting the Observation
- [var availableKeys: [VNRecognizedPointKey]](./availablekeys.md)
  The available point keys in the observation.
- [var availableGroupKeys: [VNRecognizedPointGroupKey]](./availablegroupkeys.md)
  The available point group keys in the observation.
- [func recognizedPoint(forKey: VNRecognizedPointKey) throws -> VNRecognizedPoint3D](./recognizedpoint%28forkey%29.md)
  Returns a point for a key you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizedpoints3dobservation/recognizedpoints(forgroupkey:))*