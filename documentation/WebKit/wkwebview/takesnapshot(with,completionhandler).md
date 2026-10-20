# takeSnapshot(with:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Generates a platform-native image from the web view’s contents asynchronously.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
func takeSnapshot(with snapshotConfiguration: WKSnapshotConfiguration?, completionHandler: @escaping @MainActor @Sendable (UIImage?, (any Error)?) -> Void)
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
func takeSnapshot(configuration snapshotConfiguration: WKSnapshotConfiguration?) async throws -> UIImage
```

*macOS*

```swift
func takeSnapshot(with snapshotConfiguration: WKSnapshotConfiguration?, completionHandler: @escaping @MainActor @Sendable (NSImage?, (any Error)?) -> Void)
```

*macOS*

```swift
func takeSnapshot(configuration snapshotConfiguration: WKSnapshotConfiguration?) async throws -> NSImage
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
- (void) takeSnapshotWithConfiguration:(WKSnapshotConfiguration *) snapshotConfiguration completionHandler:(void (^)(UIImage *, NSError *)) completionHandler;
```

*macOS*

```objc
- (void) takeSnapshotWithConfiguration:(WKSnapshotConfiguration *) snapshotConfiguration completionHandler:(void (^)(NSImage *, NSError *)) completionHandler;
```

## Parameters

- `snapshotConfiguration`: The object that specifies the portion of the web view to capture, and other capture-related behaviors.
- `completionHandler`: The completion handler to call when the image is ready. This block has no return value and takes the following parameters:

  - **snapshotImage**: A platform-native image that contains the specified portion of the web view.
  - **error**: An error object if a problem occurred, or `nil` on success.

## See Also

### Capturing the web view’s content
- [func createPDF(configuration: WKPDFConfiguration, completionHandler: (Result<Data, any Error>) -> Void)](./createpdf%28configuration,completionhandler%29.md)
  Generates PDF data from the web view’s contents asynchronously.
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/takesnapshot(with:completionhandler:))*