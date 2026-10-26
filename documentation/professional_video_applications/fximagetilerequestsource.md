# FxImageTileRequestSource

**Framework**: Professional Video Applications  
**Kind**: struct  
**Role**: Structure

An enumeration that identifies the requested frame.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
struct FxImageTileRequestSource
```

```c
typedef enum FxImageTileRequestSource;
```

## Topics

### Constants
- [var kFxImageTileRequestSourceEffectClip: FxImageTileRequestSource](./kfximagetilerequestsourceeffectclip.md)
  A constant that indicates that the requested frame is associated with the source clip.
- [var kFxImageTileRequestSourceNone: FxImageTileRequestSource](./kfximagetilerequestsourcenone.md)
  A constant that indicates that the requested frame is not associated with an effect or parameter.
- [var kFxImageTileRequestSourceOutput: FxImageTileRequestSource](./kfximagetilerequestsourceoutput.md)
  A constant that indicates that the requested frame is the output of a plug-in.
- [var kFxImageTileRequestSourceParameter: FxImageTileRequestSource](./kfximagetilerequestsourceparameter.md)
  A constant that indicates that the requested frame is associated with an image well parameter.
### Initializers
- [init(UInt)](./fximagetilerequestsource/init%28_%29.md)
- [init(rawValue: UInt)](./fximagetilerequestsource/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt](./fximagetilerequestsource/rawvalue.md)
### Default Implementations
- [Equatable Implementations](./fximagetilerequestsource/equatable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Enumerations
- [typealias FxError](./fxerror.md)
  Errors returned by plug-in hosts applications.
- [struct FxEyeType](./fxeyetype.md)
  Identifies which eye is being sent from a stereoscopic project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fximagetilerequestsource)*