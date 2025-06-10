# pdf(configuration:)

**Framework**: WebKit  
**Kind**: method

Generates PDF data from the web view’s contents asynchronously.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func pdf(configuration: WKPDFConfiguration = .init()) async throws -> Data
```

#### Return Value

A data object that contains the PDF data to use for rendering the contents of the web view.

## Parameters

- `configuration`: The object that specifies the portion of the web view to capture as PDF data.

## See Also

- [func takeSnapshot(with: WKSnapshotConfiguration?, completionHandler: (UIImage?, (any Error)?) -> Void)](wkwebview/takesnapshot(with:completionhandler:).md)
  Generates a platform-native image from the web view’s contents asynchronously.
- [func createPDF(configuration: WKPDFConfiguration, completionHandler: (Result<Data, any Error>) -> Void)](wkwebview/createpdf(configuration:completionhandler:).md)
  Generates PDF data from the web view’s contents asynchronously.
- [func createWebArchiveData(completionHandler: (Result<Data, any Error>) -> Void)](wkwebview/createwebarchivedata(completionhandler:).md)
  Creates a web archive of the web view’s current contents asynchronously.
- [func printOperation(with: NSPrintInfo) -> NSPrintOperation](wkwebview/printoperation(with:).md)
  Returns the print operation object to use when printing the contents of the web view.
- [class WKSnapshotConfiguration](wksnapshotconfiguration.md)
  The configuration data to use when generating an image from a web view’s contents.
- [class WKPDFConfiguration](wkpdfconfiguration.md)
  The configuration data to use when generating a PDF representation of a web view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/pdf(configuration:))*