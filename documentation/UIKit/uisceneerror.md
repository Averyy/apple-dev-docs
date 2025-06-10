# UISceneError

**Framework**: UIKit  
**Kind**: struct

Errors returned during the creation or management of a scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct UISceneError
```

## Topics

### Identifying an error cause
- [static var multipleScenesNotSupported: UISceneError.Code](uisceneerror/multiplescenesnotsupported.md)
  An error that indicates multiple scenes aren’t supported.
- [static var requestDenied: UISceneError.Code](uisceneerror/requestdenied.md)
  An error that indicates the request was denied.
- [static var geometryRequestUnsupported: UISceneError.Code](uisceneerror/geometryrequestunsupported.md)
  An error that indicates the geometry request is invalid or unsupported.
- [static var geometryRequestDenied: UISceneError.Code](uisceneerror/geometryrequestdenied.md)
  An error that indicates the geometry request is valid but the system denied the request.
- [UISceneError.Code](uisceneerror/code.md)
  Error codes for issues with scenes.
### Inspecting error information
- [static var errorDomain: String](uisceneerror/errordomain.md)
  The domain for scene-related errors.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [UISceneError.Code](uisceneerror/code.md)
  Error codes for issues with scenes.
- [let UISceneErrorDomain: String](uisceneerrordomain.md)
  The domain for scene-related errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneerror)*