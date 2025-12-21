# exported(as:)

**Framework**: WebKit  
**Kind**: method

Using the type’s `Transferable` conformance implementation, exports a value as binary data, optionally with a specified configuration for that type of data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
final func exported(as representation: WebPage.ExportedContentConfiguration) async throws -> Data
```

#### Return Value

The data with the specified representation type.

#### Discussion

For example, you can export a 100 pt by 100 pt region of a webpage as a PDF, and allow it to have a transparent background:

```swift
let page = WebPage()
// Load web content and wait for navigation to complete.

let square = CGRect(x: 0, y: 0, width: 100, height: 100)
let pdf = try await page.exported(as: .pdf(region: .rect(square), allowTransparentBackground: true))
```

If no configuration is needed, use the `Transferable` conformance of [`WebPage`](webpage.md) directly:

```swift
let page = WebPage()
// Load web content and wait for navigation to complete.

let pdf = try await page.exported(as: .pdf)
```

> **Note**: An error if the specified representation cannot be created from the page.

## Parameters

- `representation`: A configuration for a representation for a specific type of data with optional customizable properties.

## See Also

- [WebPage.ExportedContentConfiguration](webpage/exportedcontentconfiguration.md)
  A specialized configuration of a specific exportable type that can have specific properties unique to the content type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/exported(as:))*