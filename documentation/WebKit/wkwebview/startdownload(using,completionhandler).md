# startDownload(using:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Starts to download the resource at the URL in the request.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
func startDownload(using request: URLRequest, completionHandler: @escaping @MainActor @Sendable (WKDownload) -> Void)
```

```swift
func startDownload(using request: URLRequest) async -> WKDownload
```

```objc
- (void) startDownloadUsingRequest:(NSURLRequest *) request completionHandler:(void (^)(WKDownload *)) completionHandler;
```

## Discussion

To receive progress updates, set the delegate of the download object in the completion handler.

## Parameters

- `request`: An object that encapsulates a URL and other parameters that you need to download a resource from a webpage.
- `completionHandler`: A closure the system executes when it has started to download the resource.

## See Also

### Managing downloads
- [func resumeDownload(fromResumeData: Data, completionHandler: (WKDownload) -> Void)](./resumedownload%28fromresumedata,completionhandler%29.md)
  Resumes a failed or canceled download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/startdownload(using:completionhandler:))*