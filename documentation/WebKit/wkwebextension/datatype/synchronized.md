# synchronized

**Framework**: WebKit  
**Kind**: property  
**Role**: Type Property

Specifies synchronized storage, including `browser.storage.sync`.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
nonisolated
static let synchronized: WKWebExtension.DataType
```

```c
extern WKWebExtensionDataType const WKWebExtensionDataTypeSynchronized;
```

## See Also

### Constants
- [static let local: WKWebExtension.DataType](./local.md)
  Specifies local storage, including `browser.storage.local`.
- [static let session: WKWebExtension.DataType](./session.md)
  Specifies session storage, including `browser.storage.session`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/datatype/synchronized)*