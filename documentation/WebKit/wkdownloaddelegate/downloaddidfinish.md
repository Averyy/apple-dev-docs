# downloadDidFinish(_:)

**Framework**: WebKit  
**Kind**: method

Tells the delegate that the download finished.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func downloadDidFinish(_ download: WKDownload)
```

## Parameters

- `download`: The download that finished.

## See Also

- [func download(WKDownload, decideDestinationUsing: URLResponse, suggestedFilename: String, completionHandler: (URL?) -> Void)](wkdownloaddelegate/download(_:decidedestinationusing:suggestedfilename:completionhandler:).md)
  Asks the delegate to provide a file destination where the system should write the download data.
- [func download(WKDownload, didFailWithError: any Error, resumeData: Data?)](wkdownloaddelegate/download(_:didfailwitherror:resumedata:).md)
  Tells the delegate that the download failed, with error information and data you can use to restart the download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdownloaddelegate/downloaddidfinish(_:))*