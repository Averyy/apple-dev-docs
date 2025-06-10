# startDownload(using:completionHandler:)

**Framework**: WebKit  
**Kind**: method

Starts to download the resource at the URL in the request.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func startDownload(using request: URLRequest) async -> WKDownload
```

#### Discussion

To receive progress updates, set the delegate of the download object in the completion handler.

## Parameters

- `request`: An object that encapsulates a URL and other parameters that you need to download a resource from a webpage.
- `completionHandler`: A closure the system executes when it has started to download the resource.

## See Also

- [func resumeDownload(fromResumeData: Data, completionHandler: (WKDownload) -> Void)](wkwebview/resumedownload(fromresumedata:completionhandler:).md)
  Resumes a failed or canceled download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/startdownload(using:completionhandler:))*