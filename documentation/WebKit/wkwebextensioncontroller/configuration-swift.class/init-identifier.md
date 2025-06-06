# init(identifier:)

**Framework**: Webkit  
**Kind**: init

Returns a new configuration that is persistent and unique for the specified identifier.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
convenience init(identifier: UUID)
```

#### Discussion

If a [`WKWebExtensionController`](wkwebextensioncontroller.md) is associated with a unique persistent configuration, data will be written to the file system in a unique location based on the specified identifier.

## See Also

- [class func `default`() -> Self](wkwebextensioncontroller/configuration-swift.class/default.md)
  Returns a new default configuration that is persistent and not unique.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/configuration-swift.class/init(identifier:))*