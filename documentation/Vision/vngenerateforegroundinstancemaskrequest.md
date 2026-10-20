# VNGenerateForegroundInstanceMaskRequest

**Framework**: Vision  
**Kind**: class  
**Role**: Class

A request that generates an instance mask of noticable objects to separate from the background.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class VNGenerateForegroundInstanceMaskRequest
```

```objc
@interface VNGenerateForegroundInstanceMaskRequest : VNImageBasedRequest
```

## Topics

### Accessing the Results
- [var results: [VNInstanceMaskObservation]?](./vngenerateforegroundinstancemaskrequest/results.md)
  The instance masks the request observes.

## Relationships

### Inherits From
- [VNImageBasedRequest](./vnimagebasedrequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Image background removal
- [Applying visual effects to foreground subjects](./applying-visual-effects-to-foreground-subjects.md)
  Segment the foreground subjects of an image and composite them to a new background with visual effects.
- [class VNInstanceMaskObservation](./vninstancemaskobservation.md)
  An observation that contains an instance mask that labels instances in the mask.
- [var VNGenerateForegroundInstanceMaskRequestRevision1: Int](./vngenerateforegroundinstancemaskrequestrevision1.md)
  A constant for specifying the first revision of the foreground instance mask request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vngenerateforegroundinstancemaskrequest)*