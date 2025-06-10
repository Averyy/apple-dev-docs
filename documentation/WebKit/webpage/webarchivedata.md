# webArchiveData()

**Framework**: WebKit  
**Kind**: method

Creates a web archive of the webpage’s current contents.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
final func webArchiveData() async throws -> Data
```

## See Also

- [func snapshot(WKSnapshotConfiguration) async throws -> Image?](webpage/snapshot(_:).md)
  Generates an image from the web view’s contents.
- [func pdf(configuration: WKPDFConfiguration) async throws -> Data](webpage/pdf(configuration:).md)
  Generates PDF data from the webpage’s contents


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/webarchivedata())*