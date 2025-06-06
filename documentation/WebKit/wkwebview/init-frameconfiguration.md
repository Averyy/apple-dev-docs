# init(frame:configuration:)

**Framework**: Webkit  
**Kind**: init

Creates a web view and initializes it with the specified frame and configuration data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(frame: CGRect, configuration: WKWebViewConfiguration)
```

#### Return Value

An initialized web view, or `nil` if the view couldn’t be initialized.

#### Discussion

This method is the designated initializer for the class. Use this method to create a web view that requires custom configuration. For example, use it when you need to specify custom cookies or content filters for the web content.

To create a web view with default configuration values, call the inherited [`init(frame:)`](https://developer.apple.com/documentation/UIKit/UIView/init(frame:)) method.

## Parameters

- `frame`: The frame rectangle for the new web view.
- `configuration`: The configuration of the new web view. This method saves a copy of your configuration object. Changes you make to your original object after calling this method have no effect on the web view’s configuration. For a list of configuration options and their default values, see  .

## See Also

- [init?(coder: NSCoder)](wkwebview/init(coder:).md)
  Returns an object initialized from data in the specified coder object.
- [var configuration: WKWebViewConfiguration](wkwebview/configuration.md)
  The object that contains the configuration details for the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/init(frame:configuration:))*