# init(coder:)

**Framework**: WebKit  
**Kind**: init  
**Role**: Initializer

Returns an object initialized from data in the specified coder object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## Parameters

- `coder`: The coder object that contains the object’s data.

## See Also

### Creating a web view
- [init(frame: CGRect, configuration: WKWebViewConfiguration)](./init%28frame,configuration%29.md)
  Creates a web view and initializes it with the specified frame and configuration data.
- [var configuration: WKWebViewConfiguration](./configuration.md)
  The object that contains the configuration details for the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/init(coder:))*