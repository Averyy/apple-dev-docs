# local

**Framework**: WebKit  
**Kind**: property  
**Role**: Type Property

Specifies local storage, including `browser.storage.local`.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
nonisolated
static let local: WKWebExtension.DataType
```

```c
extern WKWebExtensionDataType const WKWebExtensionDataTypeLocal;
```

## See Also

### Constants
- [static let session: WKWebExtension.DataType](./session.md)
  Specifies session storage, including `browser.storage.session`.
- [static let synchronized: WKWebExtension.DataType](./synchronized.md)
  Specifies synchronized storage, including `browser.storage.sync`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/datatype/local)*