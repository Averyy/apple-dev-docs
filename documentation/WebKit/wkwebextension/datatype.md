# WKWebExtension.DataType

**Framework**: WebKit  
**Kind**: struct

Constants for specifying data types for a [`WKWebExtension.DataRecord`](wkwebextension/datarecord.md).

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
struct DataType
```

## Topics

### Constants
- [static let local: WKWebExtension.DataType](wkwebextension/datatype/local.md)
  Specifies local storage, including `browser.storage.local`.
- [static let session: WKWebExtension.DataType](wkwebextension/datatype/session.md)
  Specifies session storage, including `browser.storage.session`.
- [static let synchronized: WKWebExtension.DataType](wkwebextension/datatype/synchronized.md)
  Specifies synchronized storage, including `browser.storage.sync`.
### Initializers
- [init(rawValue: String)](wkwebextension/datatype/init(rawvalue:).md)
  Creates a data type from a raw value you provide.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [WKWebExtension.Error](wkwebextension/error.md)
  Constants that indicate errors in the [`WKWebExtension`](wkwebextension.md) domain.
- [WKWebExtension.Permission](wkwebextension/permission.md)
  Constants for specifying permission in a [`WKWebExtensionContext`](wkwebextensioncontext.md).
- [WKWebExtension.TabChangedProperties](wkwebextension/tabchangedproperties.md)
  Constants the web extension controller and web extension context use to indicate tab changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/datatype)*