# multipleScenesNotSupported

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

An error that indicates multiple scenes aren’t supported.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
static var multipleScenesNotSupported: UISceneError.Code { get }
```

#### Discussion

This error code indicates that the app doesn’t support multiple scenes or the system was unable to display multiple scenes for your app.

## See Also

### Identifying an error cause
- [static var requestDenied: UISceneError.Code](./requestdenied.md)
  An error that indicates the request was denied.
- [static var geometryRequestUnsupported: UISceneError.Code](./geometryrequestunsupported.md)
  An error that indicates the geometry request is invalid or unsupported.
- [static var geometryRequestDenied: UISceneError.Code](./geometryrequestdenied.md)
  An error that indicates the geometry request is valid but the system denied the request.
- [UISceneError.Code](./code.md)
  Error codes for issues with scenes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneerror/multiplescenesnotsupported)*