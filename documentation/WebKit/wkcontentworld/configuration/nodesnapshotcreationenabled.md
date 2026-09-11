# nodeSnapshotCreationEnabled

**Framework**: WebKit  
**Kind**: property

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var nodeSnapshotCreationEnabled: Bool { get set }
```

#### Discussion

A boolean indicating whether or not `window.webkit.createNodeSnapshot` is available.

JavaScript can call `window.webkit.createNodeSnapshot` with a return value to create a `WKDOMNodeSnapshot` object for the application to use in future JavaScript programs. Refer to the `WKDOMNodeSnapshot` documentation for more information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkcontentworld/configuration/nodesnapshotcreationenabled)*