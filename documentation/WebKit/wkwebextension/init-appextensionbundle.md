# init(appExtensionBundle:)

**Framework**: WebKit  
**Kind**: init

Creates a web extension initialized with a specified app extension bundle.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(appExtensionBundle: Bundle) async throws
```

#### Discussion

The app extension bundle must contain a `manifest.json` file in its resources directory. If the manifest is invalid or missing, or the bundle is otherwise improperly configured, an error will be thrown.

> **Note**: An error if the manifest is invalid or missing, or the bundle is otherwise improperly configured.

## Parameters

- `appExtensionBundle`: The bundle to use for the new web extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/init(appextensionbundle:))*