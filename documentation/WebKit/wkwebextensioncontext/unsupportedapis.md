# unsupportedAPIs

**Framework**: WebKit  
**Kind**: property

Specifies unsupported APIs for this extension, making them `undefined` in JavaScript.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var unsupportedAPIs: Set<String>! { get set }
```

#### Discussion

This property allows the app to specify a subset of web extension APIs that it chooses not to support, effectively making these APIs `undefined` within the extension’s JavaScript contexts. This enables extensions to employ feature detection techniques for unsupported APIs, allowing them to adapt their behavior based on the APIs actually supported by the app. Setting is only allowed when the context is not loaded. Only certain APIs can be specified here, particularly those within the `browser` namespace and other dynamic functions and properties, anything else will be silently ignored.

> **Note**: For example, specifying `"browser.windows.create"` and `"browser.storage"` in this set will result in the `browser.windows.create()` function and `browser.storage` property being `undefined`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/unsupportedapis)*