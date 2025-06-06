# session(_:didFinish:error:)

**Framework**: Watchconnectivity  
**Kind**: method

Tells the delegate that a file transfer has finished successfully or ended because of an error.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func session(_ session: WCSession, didFinish fileTransfer: WCSessionFileTransfer, error: (any Error)?)
```

#### Discussion

The session object calls this method when a file transfer initiated by the current app finished, either successfully or unsuccessfully. Use this method to note that the transfer completed or to respond to errors, perhaps by trying to send the file again at a later time.

This method is called on a background thread of your app.

## Parameters

- `session`: The session object of the current process.
- `fileTransfer`: An object containing information about the file that was transferred.
- `error`: An error object if a problem occurred.

## See Also

- [func session(WCSession, didReceive: WCSessionFile)](wcsessiondelegate/session(_:didreceive:).md)
  Tells the delegate that the session successfully received a file from its counterpart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/session(_:didfinish:error:)-6dtcu)*