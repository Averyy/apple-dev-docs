# WebOpenPanelResultListener

**Framework**: WebKit  
**Kind**: protocol  
**Role**: Protocol

`WebView` user interface delegates that implement the webView:runOpenPanelForFileButtonWithResultListener: method use the methods defined in this protocol to communicate with the listener object. The methods allow the delegate to send a cancel message, or set the selected file name.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
protocol WebOpenPanelResultListener : NSObjectProtocol
```

```objc
@protocol WebOpenPanelResultListener <NSObject>
```

## Topics

### Setting a File Name
- [func chooseFilename(String!)](./webopenpanelresultlistener/choosefilename%28_%29.md)
  Displays a file open panel and returns the selected filename.
- [func chooseFilenames([Any]!)](./webopenpanelresultlistener/choosefilenames%28_%29.md)
  Displays a file open panel and returns the multiple selected filenames.
### Cancelling a File Open Operation
- [func cancel()](./webopenpanelresultlistener/cancel%28%29.md)
  Invoked when a file open operation was cancelled.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webopenpanelresultlistener)*