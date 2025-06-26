# takeSnapshot(with:completionHandler:)

**Framework**: WebKit  
**Kind**: method

Generates a platform-native image from the web view’s contents asynchronously.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func takeSnapshot(configuration snapshotConfiguration: WKSnapshotConfiguration?) async throws -> NSImage
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func takeSnapshot(configuration snapshotConfiguration: WKSnapshotConfiguration?) async throws -> UIImage
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `snapshotConfiguration`: The object that specifies the portion of the web view to capture, and other capture-related behaviors.
- `completionHandler`: The completion handler to call when the image is ready. This block has no return value and takes the following parameters:

## See Also

- [func createPDF(configuration: WKPDFConfiguration, completionHandler: (Result<Data, any Error>) -> Void)](wkwebview/createpdf(configuration:completionhandler:).md)
  Generates PDF data from the web view’s contents asynchronously.
- [func pdf(configuration: WKPDFConfiguration) async throws -> Data](wkwebview/pdf(configuration:).md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/takesnapshot(with:completionhandler:))*