# WKWebExtension.DataType

**Framework**: WebKit  
**Kind**: struct  
**Role**: Structure

Constants for specifying data types for a [`WKWebExtension.DataRecord`](./datarecord.md).

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

```c
typedef NSString * WKWebExtensionDataType;
```

## Topics

### Constants
- [static let local: WKWebExtension.DataType](./datatype/local.md)
  Specifies local storage, including `browser.storage.local`.
- [static let session: WKWebExtension.DataType](./datatype/session.md)
  Specifies session storage, including `browser.storage.session`.
- [static let synchronized: WKWebExtension.DataType](./datatype/synchronized.md)
  Specifies synchronized storage, including `browser.storage.sync`.
### Initializers
- [init(rawValue: String)](./datatype/init%28rawvalue%29.md)
  Creates a data type from a raw value you provide.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Structures
- [WKWebExtension.Error](./error.md)
  Constants that indicate errors in the [`WKWebExtension`](../wkwebextension.md) domain.
- [WKWebExtension.Permission](./permission.md)
  Constants for specifying permission in a [`WKWebExtensionContext`](../wkwebextensioncontext.md).
- [WKWebExtension.TabChangedProperties](./tabchangedproperties.md)
  Constants the web extension controller and web extension context use to indicate tab changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/datatype)*