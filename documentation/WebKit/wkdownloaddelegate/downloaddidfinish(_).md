# downloadDidFinish(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the download finished.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
optional func downloadDidFinish(_ download: WKDownload)
```

```objc
- (void) downloadDidFinish:(WKDownload *) download;
```

## Parameters

- `download`: The download that finished.

## See Also

### Tracking Download Progress
- [func download(WKDownload, decideDestinationUsing: URLResponse, suggestedFilename: String, completionHandler: (URL?) -> Void)](./download%28_,decidedestinationusing,suggestedfilename,completionhandler%29.md)
  Asks the delegate to provide a file destination where the system should write the download data.
- [func download(WKDownload, didFailWithError: any Error, resumeData: Data?)](./download%28_,didfailwitherror,resumedata%29.md)
  Tells the delegate that the download failed, with error information and data you can use to restart the download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdownloaddelegate/downloaddidfinish(_:))*