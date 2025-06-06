# download(_:didFailWithError:resumeData:)

**Framework**: Webkit  
**Kind**: method

Tells the delegate that the download failed, with error information and data you can use to restart the download.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func download(_ download: WKDownload, didFailWithError error: any Error, resumeData: Data?)
```

#### Discussion

To restart a failed download, call [`resumeDownload(fromResumeData:completionHandler:)`](wkwebview/resumedownload(fromresumedata:completionhandler:).md) with `resumeData`.

## Parameters

- `download`: The download that failed.
- `error`: An error describing what caused the download to fail.
- `resumeData`: A data object you use to restart the download.

## See Also

- [func download(WKDownload, decideDestinationUsing: URLResponse, suggestedFilename: String, completionHandler: (URL?) -> Void)](wkdownloaddelegate/download(_:decidedestinationusing:suggestedfilename:completionhandler:).md)
  Asks the delegate to provide a file destination where the system should write the download data.
- [func downloadDidFinish(WKDownload)](wkdownloaddelegate/downloaddidfinish(_:).md)
  Tells the delegate that the download finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdownloaddelegate/download(_:didfailwitherror:resumedata:))*