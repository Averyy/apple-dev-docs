# init()

**Framework**: Webkit  
**Kind**: init

Returns a web extension controller initialized with the default configuration.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
init()
```

#### Return Value

An initialized web extension controller, or nil if the object could not be initialized.

#### Discussion

This is a designated initializer. You can use [`init(configuration:)`](wkwebextensioncontroller/init(configuration:).md) to initialize an instance with a configuration.

## See Also

- [init(configuration: WKWebExtensionController.Configuration)](wkwebextensioncontroller/init(configuration:).md)
  Returns a web extension controller initialized with the specified configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/init())*