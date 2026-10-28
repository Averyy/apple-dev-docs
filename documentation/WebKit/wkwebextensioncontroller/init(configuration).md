# init(configuration:)

**Framework**: WebKit  
**Kind**: init  
**Role**: Initializer

Returns a web extension controller initialized with the specified configuration.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
init(configuration: WKWebExtensionController.Configuration)
```

```objc
- (instancetype) initWithConfiguration:(WKWebExtensionControllerConfiguration *) configuration;
```

## Return Value

An initialized web extension controller, or nil if the object could not be initialized.

## Discussion

This is a designated initializer. You can use [`init()`](./init%28%29.md) to initialize an instance with the default configuration. The initializer copies the specified configuration, so mutating the configuration after invoking the initializer has no effect on the web extension controller.

## Parameters

- `configuration`: The configuration for the new web extension controller.

## See Also

### Related Documentation
- [init()](./init%28%29.md)
  Returns a web extension controller initialized with the default configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/init(configuration:))*