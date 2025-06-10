# init(configuration:)

**Framework**: WebKit  
**Kind**: init

Returns a web extension controller initialized with the specified configuration.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
init(configuration: WKWebExtensionController.Configuration)
```

#### Return Value

An initialized web extension controller, or nil if the object could not be initialized.

#### Discussion

This is a designated initializer. You can use [`init()`](wkwebextensioncontroller/init().md) to initialize an instance with the default configuration. The initializer copies the specified configuration, so mutating the configuration after invoking the initializer has no effect on the web extension controller.

## Parameters

- `configuration`: The configuration for the new web extension controller.

## See Also

- [init()](wkwebextensioncontroller/init.md)
  Returns a web extension controller initialized with the default configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/init(configuration:))*