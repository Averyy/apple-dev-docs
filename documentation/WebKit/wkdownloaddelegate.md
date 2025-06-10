# WKDownloadDelegate

**Framework**: WebKit  
**Kind**: protocol

A protocol you implement to track download progress and handle redirects, authentication challenges, and failures.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol WKDownloadDelegate : NSObjectProtocol
```

## Topics

### Tracking Download Progress
- [func download(WKDownload, decideDestinationUsing: URLResponse, suggestedFilename: String, completionHandler: (URL?) -> Void)](wkdownloaddelegate/download(_:decidedestinationusing:suggestedfilename:completionhandler:).md)
  Asks the delegate to provide a file destination where the system should write the download data.
- [func downloadDidFinish(WKDownload)](wkdownloaddelegate/downloaddidfinish(_:).md)
  Tells the delegate that the download finished.
- [func download(WKDownload, didFailWithError: any Error, resumeData: Data?)](wkdownloaddelegate/download(_:didfailwitherror:resumedata:).md)
  Tells the delegate that the download failed, with error information and data you can use to restart the download.
### Responding to Authorization Challenges
- [func download(WKDownload, didReceive: URLAuthenticationChallenge, completionHandler: (URLSession.AuthChallengeDisposition, URLCredential?) -> Void)](wkdownloaddelegate/download(_:didreceive:completionhandler:).md)
  Asks the delegate to respond to an authentication challenge.
- [WKDownload.RedirectPolicy](wkdownload/redirectpolicy.md)
  An enumeration with cases that indicate whether to proceed with a redirect.
### Responding to Redirects
- [func download(WKDownload, willPerformHTTPRedirection: HTTPURLResponse, newRequest: URLRequest, decisionHandler: (WKDownload.RedirectPolicy) -> Void)](wkdownloaddelegate/download(_:willperformhttpredirection:newrequest:decisionhandler:).md)
  Asks the delegate to respond to the download’s redirect response.
- [WKDownload.RedirectPolicy](wkdownload/redirectpolicy.md)
  An enumeration with cases that indicate whether to proceed with a redirect.
### Instance Methods
- [func download(WKDownload, decidePlaceholderPolicy: (WKDownload.PlaceholderPolicy, URL?) -> Void)](wkdownloaddelegate/download(_:decideplaceholderpolicy:).md)
- [func download(WKDownload, didReceiveFinalURL: URL)](wkdownloaddelegate/download(_:didreceivefinalurl:).md)
- [func download(WKDownload, didReceivePlaceholderURL: URL, completionHandler: () -> Void)](wkdownloaddelegate/download(_:didreceiveplaceholderurl:completionhandler:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class WKDownload](wkdownload.md)
  An object that represents the download of a web resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdownloaddelegate)*