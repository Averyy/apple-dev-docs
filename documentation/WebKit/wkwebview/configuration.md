# configuration

**Framework**: Webkit  
**Kind**: property

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
@MainActor var configuration: WKWebViewConfiguration { get }
```

#### Discussion

Use the object in this property to obtain information about your web view’s configuration. Because this property returns a copy of the configuration object, changes you make to that object don’t affect the web view’s configuration.

If you didn’t create your web view using the [`init(frame:configuration:)`](wkwebview/init(frame:configuration:).md) method, this property contains a default configuration object.

## See Also

- [class WKWebViewConfiguration](wkwebviewconfiguration.md)
  A collection of properties that you use to initialize a web view.
- [init(frame: CGRect, configuration: WKWebViewConfiguration)](wkwebview/init(frame:configuration:).md)
  Creates a web view and initializes it with the specified frame and configuration data.
- [init?(coder: NSCoder)](wkwebview/init(coder:).md)
  Returns an object initialized from data in the specified coder object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/configuration)*