# WKWebExtension.Error.Code

**Framework**: WebKit  
**Kind**: enum

Constants that indicate errors in the [`WKWebExtension`](wkwebextension.md) domain.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
enum Code
```

## Topics

### Enumeration Cases
- [WKWebExtension.Error.Code.invalidArchive](wkwebextension/error/code/invalidarchive.md)
  Indicates that the archive file is invalid or corrupt.
- [WKWebExtension.Error.Code.invalidBackgroundPersistence](wkwebextension/error/code/invalidbackgroundpersistence.md)
  Indicates that the extension specified background persistence that was not compatible with the platform or features requested.
- [WKWebExtension.Error.Code.invalidDeclarativeNetRequestEntry](wkwebextension/error/code/invaliddeclarativenetrequestentry.md)
  Indicates that an invalid declarative net request entry was encountered.
- [WKWebExtension.Error.Code.invalidManifest](wkwebextension/error/code/invalidmanifest.md)
  Indicates that an invalid `manifest.json` was encountered.
- [WKWebExtension.Error.Code.invalidManifestEntry](wkwebextension/error/code/invalidmanifestentry.md)
  Indicates that an invalid manifest entry was encountered.
- [WKWebExtension.Error.Code.invalidResourceCodeSignature](wkwebextension/error/code/invalidresourcecodesignature.md)
  Indicates that a resource failed the bundle’s code signature checks.
- [WKWebExtension.Error.Code.resourceNotFound](wkwebextension/error/code/resourcenotfound.md)
  Indicates that a specified resource was not found on disk.
- [WKWebExtension.Error.Code.unknown](wkwebextension/error/code/unknown.md)
  Indicates that an unknown error occurred.
- [WKWebExtension.Error.Code.unsupportedManifestVersion](wkwebextension/error/code/unsupportedmanifestversion.md)
  Indicates that the manifest version is not supported.
### Initializers
- [init?(rawValue: Int)](wkwebextension/error/code/init(rawvalue:).md)
  Creates an error code from a raw value you provide.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [WKWebExtensionContext.Error.Code](wkwebextensioncontext/error/code.md)
  Constants that indicate errors in the [`WKWebExtensionContext`](wkwebextensioncontext.md) domain.
- [WKWebExtension.DataRecord.Error.Code](wkwebextension/datarecord/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.DataRecord`](wkwebextension/datarecord.md) domain.
- [WKWebExtension.DataRecord.Error](wkwebextension/datarecord/error.md)
  Constants that indicate errors in the [`WKWebExtension.DataRecord`](wkwebextension/datarecord.md) domain.
- [WKWebExtension.MatchPattern.Error.Code](wkwebextension/matchpattern/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.MatchPattern`](wkwebextension/matchpattern.md) domain.
- [WKWebExtension.MessagePort.Error.Code](wkwebextension/messageport/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.MessagePort`](wkwebextension/messageport.md) domain.
- [WKWebExtension.MessagePort.Error](wkwebextension/messageport/error.md)
  Constants that indicate errors in the [`WKWebExtension.MessagePort`](wkwebextension/messageport.md) domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/error/code)*