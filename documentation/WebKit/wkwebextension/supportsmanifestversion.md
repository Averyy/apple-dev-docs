# supportsManifestVersion(_:)

**Framework**: WebKit  
**Kind**: method

Checks if a manifest version is supported by the extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func supportsManifestVersion(_ manifestVersion: Double) -> Bool
```

#### Return Value

Returns `YES` if the extension specified a manifest version that is greater than or equal to `manifestVersion`.

## Parameters

- `manifestVersion`: The version number to check.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/supportsmanifestversion(_:))*