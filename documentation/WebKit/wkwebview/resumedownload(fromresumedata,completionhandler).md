# resumeDownload(fromResumeData:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Resumes a failed or canceled download.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
func resumeDownload(fromResumeData resumeData: Data, completionHandler: @escaping @MainActor @Sendable (WKDownload) -> Void)
```

```swift
func resumeDownload(fromResumeData resumeData: Data) async -> WKDownload
```

```objc
- (void) resumeDownloadFromResumeData:(NSData *) resumeData completionHandler:(void (^)(WKDownload *)) completionHandler;
```

#### Discussion

To receive progress updates, set the delegate of the download object in the completion handler.

## Parameters

- `resumeData`: An object with data that you use to resume a failed or canceled download.
- `completionHandler`: A closure the system executes when it has resumed a download.

## See Also

### Managing downloads
- [func startDownload(using: URLRequest, completionHandler: (WKDownload) -> Void)](./startdownload%28using,completionhandler%29.md)
  Starts to download the resource at the URL in the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/resumedownload(fromresumedata:completionhandler:))*