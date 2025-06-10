# WebOpenPanelResultListener

**Framework**: WebKit  
**Kind**: protocol

`WebView` user interface delegates that implement the webView:runOpenPanelForFileButtonWithResultListener: method use the methods defined in this protocol to communicate with the listener object. The methods allow the delegate to send a cancel message, or set the selected file name.

**Availability**:
- macOS 10.3+

## Declaration

```swift
protocol WebOpenPanelResultListener : NSObjectProtocol
```

## Topics

### Setting a File Name
- [func chooseFilename(String!)](webopenpanelresultlistener/choosefilename(_:).md)
  Displays a file open panel and returns the selected filename.
- [func chooseFilenames([Any]!)](webopenpanelresultlistener/choosefilenames(_:).md)
  Displays a file open panel and returns the multiple selected filenames.
### Cancelling a File Open Operation
- [func cancel()](webopenpanelresultlistener/cancel.md)
  Invoked when a file open operation was cancelled.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webopenpanelresultlistener)*