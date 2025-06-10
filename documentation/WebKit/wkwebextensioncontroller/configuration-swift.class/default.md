# default()

**Framework**: WebKit  
**Kind**: method

Returns a new default configuration that is persistent and not unique.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
class func `default`() -> Self
```

#### Discussion

If a [`WKWebExtensionController`](wkwebextensioncontroller.md) is associated with a persistent configuration, data will be written to the file system in a common location. When using multiple extension controllers, each controller should use a unique configuration to avoid conflicts.

## See Also

- [convenience init(identifier: UUID)](wkwebextensioncontroller/configuration-swift.class/init(identifier:).md)
  Returns a new configuration that is persistent and unique for the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/configuration-swift.class/default())*