# manifestVersion

**Framework**: Webkit  
**Kind**: property

The parsed manifest version, or `0` if there is no version specified in the manifest.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var manifestVersion: Double { get }
```

#### Discussion

> **Note**: A [`unsupportedManifestVersion`](wkwebextension/error/unsupportedmanifestversion.md) error will be reported if the manifest version isn’t specified.

A [`unsupportedManifestVersion`](wkwebextension/error/unsupportedmanifestversion.md) error will be reported if the manifest version isn’t specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/manifestversion)*