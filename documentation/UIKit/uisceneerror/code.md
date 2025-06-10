# UISceneError.Code

**Framework**: UIKit  
**Kind**: enum

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

## Topics

### Error codes
- [UISceneError.Code.multipleScenesNotSupported](uisceneerror/code/multiplescenesnotsupported.md)
  An error that indicates multiple scenes aren’t supported.
- [UISceneError.Code.requestDenied](uisceneerror/code/requestdenied.md)
  An error that indicates the request was denied.
- [UISceneError.Code.geometryRequestUnsupported](uisceneerror/code/geometryrequestunsupported.md)
  An error that indicates the geometry request is invalid or unsupported.
- [UISceneError.Code.geometryRequestDenied](uisceneerror/code/geometryrequestdenied.md)
  An error that indicates the geometry request is valid but the system denied the request.
### Initializers
- [init?(rawValue: Int)](uisceneerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct UISceneError](uisceneerror.md)
  Errors returned during the creation or management of a scene.
- [let UISceneErrorDomain: String](uisceneerrordomain.md)
  The domain for scene-related errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneerror/code)*