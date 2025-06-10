# createWebArchiveData(completionHandler:)

**Framework**: WebKit  
**Kind**: method

Creates a web archive of the web view’s current contents asynchronously.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func createWebArchiveData(completionHandler: @escaping @MainActor (Result<Data, any Error>) -> Void)
```

## Parameters

- `completionHandler`: The completion handler block to call when the web archive data is ready. This block has no return value and takes the following parameters:

## See Also

- [func takeSnapshot(with: WKSnapshotConfiguration?, completionHandler: (UIImage?, (any Error)?) -> Void)](wkwebview/takesnapshot(with:completionhandler:).md)
  Generates a platform-native image from the web view’s contents asynchronously.
- [func createPDF(configuration: WKPDFConfiguration, completionHandler: (Result<Data, any Error>) -> Void)](wkwebview/createpdf(configuration:completionhandler:).md)
  Generates PDF data from the web view’s contents asynchronously.
- [func pdf(configuration: WKPDFConfiguration) async throws -> Data](wkwebview/pdf(configuration:).md)
  Generates PDF data from the web view’s contents asynchronously.
- [func printOperation(with: NSPrintInfo) -> NSPrintOperation](wkwebview/printoperation(with:).md)
  Returns the print operation object to use when printing the contents of the web view.
- [class WKSnapshotConfiguration](wksnapshotconfiguration.md)
  The configuration data to use when generating an image from a web view’s contents.
- [class WKPDFConfiguration](wkpdfconfiguration.md)
  The configuration data to use when generating a PDF representation of a web view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/createwebarchivedata(completionhandler:))*