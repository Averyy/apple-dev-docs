# printOperation(with:)

**Framework**: Webkit  
**Kind**: method

Returns the print operation object to use when printing the contents of the web view.

**Availability**:
- macOS 11.0+

## Declaration

```swift
@MainActor
func printOperation(with printInfo: NSPrintInfo) -> NSPrintOperation
```

#### Return Value

The print operation object to use when printing the web view, or `nil` if printing is not supported.

## Parameters

- `printInfo`: The printer information object to use when configuring the print operation.

## See Also

- [func takeSnapshot(with: WKSnapshotConfiguration?, completionHandler: (UIImage?, (any Error)?) -> Void)](wkwebview/takesnapshot(with:completionhandler:).md)
  Generates a platform-native image from the web view’s contents asynchronously.
- [func createPDF(configuration: WKPDFConfiguration, completionHandler: (Result<Data, any Error>) -> Void)](wkwebview/createpdf(configuration:completionhandler:).md)
  Generates PDF data from the web view’s contents asynchronously.
- [func pdf(configuration: WKPDFConfiguration) async throws -> Data](wkwebview/pdf(configuration:).md)
  Generates PDF data from the web view’s contents asynchronously.
- [func createWebArchiveData(completionHandler: (Result<Data, any Error>) -> Void)](wkwebview/createwebarchivedata(completionhandler:).md)
  Creates a web archive of the web view’s current contents asynchronously.
- [class WKSnapshotConfiguration](wksnapshotconfiguration.md)
  The configuration data to use when generating an image from a web view’s contents.
- [class WKPDFConfiguration](wkpdfconfiguration.md)
  The configuration data to use when generating a PDF representation of a web view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/printoperation(with:))*