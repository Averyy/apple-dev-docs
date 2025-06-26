# init(resourceBaseURL:)

**Framework**: WebKit  
**Kind**: init

Creates a web extension initialized with a specified resource base URL, which can point to either a directory or a ZIP archive.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(resourceBaseURL: URL) async throws
```

#### Discussion

The URL must be a file URL that points to either a directory with a `manifest.json` file or a ZIP archive containing a `manifest.json` file. If the manifest is invalid or missing, or the URL points to an unsupported format or invalid archive, an error will be returned.

> **Note**: An error if the manifest is invalid or missing, or the URL points to an unsupported format or invalid archive.

## Parameters

- `resourceBaseURL`: The file URL to use for the new web extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/init(resourcebaseurl:))*