# configuration

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The object that contains the configuration details for the web view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var configuration: WKWebViewConfiguration { get }
```

```objc
@property (nonatomic, copy, readonly) WKWebViewConfiguration * configuration;
```

#### Discussion

Use the object in this property to obtain information about your web view’s configuration. Because this property returns a copy of the configuration object, changes you make to that object don’t affect the web view’s configuration.

If you didn’t create your web view using the [`init(frame:configuration:)`](./init%28frame,configuration%29.md) method, this property contains a default configuration object.

## See Also

### Related Documentation
- [class WKWebViewConfiguration](../wkwebviewconfiguration.md)
  A collection of properties that you use to initialize a web view.
### Creating a web view
- [init(frame: CGRect, configuration: WKWebViewConfiguration)](./init%28frame,configuration%29.md)
  Creates a web view and initializes it with the specified frame and configuration data.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Returns an object initialized from data in the specified coder object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/configuration)*