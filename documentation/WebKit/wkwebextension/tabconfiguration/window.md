# window

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

Indicates the window where the tab should be opened.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var window: (any WKWebExtensionWindow)? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) id<WKWebExtensionWindow> window;
```

#### Discussion

If this property is `nil`, no window was specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/tabconfiguration/window)*