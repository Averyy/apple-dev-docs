# UISceneError.Code

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Error codes for issues with scenes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

```c
enum UISceneErrorCode : NSInteger;
```

## Topics

### Error codes
- [UISceneError.Code.multipleScenesNotSupported](./code/multiplescenesnotsupported.md)
  An error that indicates multiple scenes aren’t supported.
- [UISceneError.Code.requestDenied](./code/requestdenied.md)
  An error that indicates the request was denied.
- [UISceneError.Code.geometryRequestUnsupported](./code/geometryrequestunsupported.md)
  An error that indicates the geometry request is invalid or unsupported.
- [UISceneError.Code.geometryRequestDenied](./code/geometryrequestdenied.md)
  An error that indicates the geometry request is valid but the system denied the request.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [struct UISceneError](../uisceneerror.md)
  Errors returned during the creation or management of a scene.
- [let UISceneErrorDomain: String](../uisceneerrordomain.md)
  The domain for scene-related errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneerror/code)*