# WKDownloadDelegate

**Framework**: WebKit  
**Kind**: protocol  
**Role**: Protocol

A protocol you implement to track download progress and handle redirects, authentication challenges, and failures.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
@MainActor
protocol WKDownloadDelegate : NSObjectProtocol
```

```objc
@protocol WKDownloadDelegate <NSObject>
```

## Topics

### Tracking Download Progress
- [func download(WKDownload, decideDestinationUsing: URLResponse, suggestedFilename: String, completionHandler: (URL?) -> Void)](./wkdownloaddelegate/download%28_,decidedestinationusing,suggestedfilename,completionhandler%29.md)
  Asks the delegate to provide a file destination where the system should write the download data.
- [func downloadDidFinish(WKDownload)](./wkdownloaddelegate/downloaddidfinish%28_%29.md)
  Tells the delegate that the download finished.
- [func download(WKDownload, didFailWithError: any Error, resumeData: Data?)](./wkdownloaddelegate/download%28_,didfailwitherror,resumedata%29.md)
  Tells the delegate that the download failed, with error information and data you can use to restart the download.
### Responding to Authorization Challenges
- [func download(WKDownload, didReceive: URLAuthenticationChallenge, completionHandler: (URLSession.AuthChallengeDisposition, URLCredential?) -> Void)](./wkdownloaddelegate/download%28_,didreceive,completionhandler%29.md)
  Asks the delegate to respond to an authentication challenge.
- [WKDownload.RedirectPolicy](./wkdownload/redirectpolicy.md)
  An enumeration with cases that indicate whether to proceed with a redirect.
### Responding to Redirects
- [func download(WKDownload, willPerformHTTPRedirection: HTTPURLResponse, newRequest: URLRequest, decisionHandler: (WKDownload.RedirectPolicy) -> Void)](./wkdownloaddelegate/download%28_,willperformhttpredirection,newrequest,decisionhandler%29.md)
  Asks the delegate to respond to the download’s redirect response.
- [WKDownload.RedirectPolicy](./wkdownload/redirectpolicy.md)
  An enumeration with cases that indicate whether to proceed with a redirect.
### Instance Methods
- [func download(WKDownload, decidePlaceholderPolicy: (WKDownload.PlaceholderPolicy, URL?) -> Void)](./wkdownloaddelegate/download%28_,decideplaceholderpolicy%29.md)
- [func download(WKDownload, didReceiveFinalURL: URL)](./wkdownloaddelegate/download%28_,didreceivefinalurl%29.md)
- [func download(WKDownload, didReceivePlaceholderURL: URL, completionHandler: () -> Void)](./wkdownloaddelegate/download%28_,didreceiveplaceholderurl,completionhandler%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Downloads
- [class WKDownload](./wkdownload.md)
  An object that represents the download of a web resource.
- [WKDownload.PlaceholderPolicy](./wkdownload/placeholderpolicy.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkdownloaddelegate)*