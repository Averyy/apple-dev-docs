# session(_:didReceive:)

**Framework**: Watchconnectivity  
**Kind**: method

Tells the delegate that the session successfully received a file from its counterpart.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func session(_ session: WCSession, didReceive file: WCSessionFile)
```

#### Discussion

The session object calls this method when it successfully receives a file from its counterpart. Implement this method to incorporate the file information into the current app. The system calls this method on a background thread.

Remember to move the file referenced by the `file` parameter if you intend to keep it. If you don’t move the file synchronously during your implementation of this method, the system deletes the file when the method returns.

> ⚠️ **Warning**:  Always test Watch Connectivity file transfers on paired devices. The system doesn’t call the [`session(_:didReceive:)`](wcsessiondelegate/session(_:didreceive:).md) method in Simulator.

 Always test Watch Connectivity file transfers on paired devices. The system doesn’t call the [`session(_:didReceive:)`](wcsessiondelegate/session(_:didreceive:).md) method in Simulator.

## Parameters

- `session`: The session object of the current process.
- `file`: The object containing the URL of the file and any additional information. If you want to keep the file referenced by this parameter, you must move it synchronously to a new location during your implementation of this method. If you don’t move the file, the system deletes it after this method returns.

## See Also

- [func session(WCSession, didFinish: WCSessionFileTransfer, error: (any Error)?)](wcsessiondelegate/session(_:didfinish:error:)-6dtcu.md)
  Tells the delegate that a file transfer has finished successfully or ended because of an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/session(_:didreceive:))*