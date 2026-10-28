# init()

**Framework**: WebKit  
**Kind**: init  
**Role**: Initializer

Returns a web extension controller initialized with the default configuration.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
init()
```

```objc
- (instancetype) init;
```

## Return Value

An initialized web extension controller, or nil if the object could not be initialized.

## Discussion

This is a designated initializer. You can use [`init(configuration:)`](./init%28configuration%29.md) to initialize an instance with a configuration.

## See Also

### Related Documentation
- [init(configuration: WKWebExtensionController.Configuration)](./init%28configuration%29.md)
  Returns a web extension controller initialized with the specified configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/init())*