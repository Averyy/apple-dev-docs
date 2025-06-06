# WKWebExtension.Error

**Framework**: Webkit  
**Kind**: struct

Constants that indicate errors in the [`WKWebExtension`](wkwebextension.md) domain.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
struct Error
```

## Topics

### Type Properties
- [static var errorDomain: String](wkwebextension/error/errordomain.md)
- [static var invalidArchive: WKWebExtension.Error.Code](wkwebextension/error/invalidarchive.md)
  Indicates that the archive file is invalid or corrupt.
- [static var invalidBackgroundPersistence: WKWebExtension.Error.Code](wkwebextension/error/invalidbackgroundpersistence.md)
  Indicates that the extension specified background persistence that was not compatible with the platform or features requested.
- [static var invalidDeclarativeNetRequestEntry: WKWebExtension.Error.Code](wkwebextension/error/invaliddeclarativenetrequestentry.md)
  Indicates that an invalid declarative net request entry was encountered.
- [static var invalidManifest: WKWebExtension.Error.Code](wkwebextension/error/invalidmanifest.md)
  Indicates that an invalid `manifest.json` was encountered.
- [static var invalidManifestEntry: WKWebExtension.Error.Code](wkwebextension/error/invalidmanifestentry.md)
  Indicates that an invalid manifest entry was encountered.
- [static var invalidResourceCodeSignature: WKWebExtension.Error.Code](wkwebextension/error/invalidresourcecodesignature.md)
  Indicates that a resource failed the bundle’s code signature checks.
- [static var resourceNotFound: WKWebExtension.Error.Code](wkwebextension/error/resourcenotfound.md)
  Indicates that a specified resource was not found on disk.
- [static var unknown: WKWebExtension.Error.Code](wkwebextension/error/unknown.md)
  Indicates that an unknown error occurred.
- [static var unsupportedManifestVersion: WKWebExtension.Error.Code](wkwebextension/error/unsupportedmanifestversion.md)
  Indicates that the manifest version is not supported.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [WKWebExtension.DataType](wkwebextension/datatype.md)
  Constants for specifying data types for a [`WKWebExtension.DataRecord`](wkwebextension/datarecord.md).
- [WKWebExtension.Permission](wkwebextension/permission.md)
  Constants for specifying permission in a [`WKWebExtensionContext`](wkwebextensioncontext.md).
- [WKWebExtension.TabChangedProperties](wkwebextension/tabchangedproperties.md)
  Constants the web extension controller and web extension context use to indicate tab changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/error)*