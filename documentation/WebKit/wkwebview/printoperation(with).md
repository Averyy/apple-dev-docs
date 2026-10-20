# printOperation(with:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns the print operation object to use when printing the contents of the web view.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func printOperation(with printInfo: NSPrintInfo) -> NSPrintOperation
```

```objc
- (NSPrintOperation *) printOperationWithPrintInfo:(NSPrintInfo *) printInfo;
```

#### Return Value

The print operation object to use when printing the web view, or `nil` if printing is not supported.

## Parameters

- `printInfo`: The printer information object to use when configuring the print operation.

## See Also

### Capturing the web view’s content
- [func takeSnapshot(with: WKSnapshotConfiguration?, completionHandler: (UIImage?, (any Error)?) -> Void)](./takesnapshot%28with,completionhandler%29.md)
  Generates a platform-native image from the web view’s contents asynchronously.
- [func createPDF(configuration: WKPDFConfiguration, completionHandler: (Result<Data, any Error>) -> Void)](./createpdf%28configuration,completionhandler%29.md)
  Generates PDF data from the web view’s contents asynchronously.
- [func pdf(configuration: WKPDFConfiguration) async throws -> Data](./pdf%28configuration%29.md)
  Generates PDF data from the web view’s contents asynchronously.
- [func createWebArchiveData(completionHandler: (Result<Data, any Error>) -> Void)](./createwebarchivedata%28completionhandler%29.md)
  Creates a web archive of the web view’s current contents asynchronously.
- [class WKSnapshotConfiguration](../wksnapshotconfiguration.md)
  The configuration data to use when generating an image from a web view’s contents.
- [class WKPDFConfiguration](../wkpdfconfiguration.md)
  The configuration data to use when generating a PDF representation of a web view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/printoperation(with:))*