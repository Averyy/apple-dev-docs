# applicationIdentifier

**Framework**: Webkit  
**Kind**: property

The unique identifier for the app to which this port should be connected.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var applicationIdentifier: String? { get }
```

#### Discussion

This identifier is provided by the web extension and may or may not be used by the app. It’s up to the app to decide how to interpret this identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/messageport/applicationidentifier)*