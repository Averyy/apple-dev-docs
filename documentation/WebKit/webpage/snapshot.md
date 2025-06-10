# snapshot(_:)

**Framework**: WebKit  
**Kind**: method

Generates an image from the web view’s contents.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
final func snapshot(_ configuration: WKSnapshotConfiguration = .init()) async throws -> Image?
```

#### Return Value

An image that contains the specified portion of the webpage.

## Parameters

- `configuration`: The object that specifies the portion of the web page to capture, and other capture-related behaviors.

## See Also

- [func pdf(configuration: WKPDFConfiguration) async throws -> Data](webpage/pdf(configuration:).md)
  Generates PDF data from the webpage’s contents
- [func webArchiveData() async throws -> Data](webpage/webarchivedata.md)
  Creates a web archive of the webpage’s current contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/snapshot(_:))*