# createPDF(configuration:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Generates PDF data from the web view’s contents asynchronously.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func createPDF(configuration: WKPDFConfiguration = .init(), completionHandler: @escaping @MainActor @Sendable (Result<Data, any Error>) -> Void)
```

## Parameters

- `configuration`: The object that specifies the portion of the web view to capture as PDF data.
- `completionHandler`: The completion handler to call when the data is ready. This block has no return value and takes the following parameters:

  - **pdfDocumentData**: A data object that contains the PDF data to use for rendering the contents of the web view.
  - **error**: An error object if a problem occurred, or `nil` on success.

## See Also

### Capturing the web view’s content
- [func takeSnapshot(with: WKSnapshotConfiguration?, completionHandler: (UIImage?, (any Error)?) -> Void)](./takesnapshot%28with,completionhandler%29.md)
  Generates a platform-native image from the web view’s contents asynchronously.
- [func pdf(configuration: WKPDFConfiguration) async throws -> Data](./pdf%28configuration%29.md)
  Generates PDF data from the web view’s contents asynchronously.
- [func createWebArchiveData(completionHandler: (Result<Data, any Error>) -> Void)](./createwebarchivedata%28completionhandler%29.md)
  Creates a web archive of the web view’s current contents asynchronously.
- [func printOperation(with: NSPrintInfo) -> NSPrintOperation](./printoperation%28with%29.md)
  Returns the print operation object to use when printing the contents of the web view.
- [class WKSnapshotConfiguration](../wksnapshotconfiguration.md)
  The configuration data to use when generating an image from a web view’s contents.
- [class WKPDFConfiguration](../wkpdfconfiguration.md)
  The configuration data to use when generating a PDF representation of a web view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/createpdf(configuration:completionhandler:))*