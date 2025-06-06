# multipleScenesNotSupported

**Framework**: UIKit  
**Kind**: property

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

- [static var requestDenied: UISceneError.Code](uisceneerror/requestdenied.md)
  An error that indicates the request was denied.
- [static var geometryRequestUnsupported: UISceneError.Code](uisceneerror/geometryrequestunsupported.md)
  An error that indicates the geometry request is invalid or unsupported.
- [static var geometryRequestDenied: UISceneError.Code](uisceneerror/geometryrequestdenied.md)
  An error that indicates the geometry request is valid but the system denied the request.
- [UISceneError.Code](uisceneerror/code.md)
  Error codes for issues with scenes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneerror/multiplescenesnotsupported)*