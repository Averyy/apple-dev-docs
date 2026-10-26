# FxEyeType

**Framework**: Professional Video Applications  
**Kind**: struct  
**Role**: Structure

Identifies which eye is being sent from a stereoscopic project.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
struct FxEyeType
```

```c
typedef enum FxEyeType;
```

## Topics

### Constants
- [var kFxEyeType_LEFT: FxEyeType](./kfxeyetype_left.md)
  The left eye portion of the stereoscopic image.
- [var kFxEyeType_MONO: FxEyeType](./kfxeyetype_mono.md)
  Monoscopic only.
- [var kFxEyeType_RIGHT: FxEyeType](./kfxeyetype_right.md)
  The right eye portion of the stereoscopic image.
### Initializers
- [init(UInt32)](./fxeyetype/init%28_%29.md)
- [init(rawValue: UInt32)](./fxeyetype/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt32](./fxeyetype/rawvalue.md)
### Default Implementations
- [Equatable Implementations](./fxeyetype/equatable-implementations.md)

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
- [struct FxImageTileRequestSource](./fximagetilerequestsource.md)
  An enumeration that identifies the requested frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxeyetype)*