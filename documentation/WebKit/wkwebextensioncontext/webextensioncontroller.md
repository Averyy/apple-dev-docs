# webExtensionController

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The extension controller this context is loaded in, otherwise `nil` if it isn’t loaded.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
weak var webExtensionController: WKWebExtensionController? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) WKWebExtensionController * webExtensionController;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/webextensioncontroller)*