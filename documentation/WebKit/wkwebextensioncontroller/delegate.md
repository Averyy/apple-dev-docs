# delegate

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The extension controller delegate.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
weak var delegate: (any WKWebExtensionControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak) id<WKWebExtensionControllerDelegate> delegate;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/delegate)*