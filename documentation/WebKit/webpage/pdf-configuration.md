# pdf(configuration:)

**Framework**: WebKit  
**Kind**: method

Generates PDF data from the webpage’s contents.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
final func pdf(configuration: WKPDFConfiguration = .init()) async throws -> Data
```

#### Return Value

A data object that contains the PDF data to use for rendering the contents of the webpage.

#### Discussion

> **Note**: An error if a problem occurred.

## Parameters

- `configuration`: The object that specifies the portion of the web view to capture as PDF data.

## See Also

- [func snapshot(WKSnapshotConfiguration) async throws -> Image?](webpage/snapshot(_:).md)
  Generates an image from the web view’s contents.
- [func webArchiveData() async throws -> Data](webpage/webarchivedata.md)
  Creates a web archive of the webpage’s current contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/pdf(configuration:))*