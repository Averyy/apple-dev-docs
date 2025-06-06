# nonPersistent()

**Framework**: Webkit  
**Kind**: method

Returns a new non-persistent configuration.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
class func nonPersistent() -> Self
```

#### Discussion

If a [`WKWebExtensionController`](wkwebextensioncontroller.md) is associated with a non-persistent configuration, no data will be written to the file system. This is useful for extensions in “private browsing” situations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/configuration-swift.class/nonpersistent())*