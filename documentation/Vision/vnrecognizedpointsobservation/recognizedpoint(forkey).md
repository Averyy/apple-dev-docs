# recognizedPoint(forKey:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (VNRecognizedPoint *) recognizedPointForKey:(VNRecognizedPointKey) pointKey error:(NSError **) error;
```

## Return Value

The recognized point associated with the key.

## Parameters

- `pointKey`: The key of the point to retrieve.

## See Also

### Inspecting the Observation
- [var availableKeys: [VNRecognizedPointKey]](./availablekeys.md)
  The available point keys in the observation.
- [var availableGroupKeys: [VNRecognizedPointGroupKey]](./availablegroupkeys.md)
  The available point group keys in the observation.
- [func recognizedPoints(forGroupKey: VNRecognizedPointGroupKey) throws -> [VNRecognizedPointKey : VNRecognizedPoint]](./recognizedpoints%28forgroupkey%29.md)
  Retrieves the recognized points for a key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrecognizedpointsobservation/recognizedpoint(forkey:))*