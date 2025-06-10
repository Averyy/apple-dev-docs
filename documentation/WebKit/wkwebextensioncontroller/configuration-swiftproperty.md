# configuration

**Framework**: WebKit  
**Kind**: property

A copy of the configuration with which the web extension controller was initialized.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@NSCopying
@MainActor var configuration: WKWebExtensionController.Configuration { get }
```

#### Discussion

Mutating the configuration has no effect on the web extension controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/configuration-swift.property)*