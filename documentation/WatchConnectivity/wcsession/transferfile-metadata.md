# transferFile(_:metadata:)

**Framework**: Watchconnectivity  
**Kind**: method

Sends the specified file and optional dictionary to the counterpart.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func transferFile(_ file: URL, metadata: [String : Any]?) -> WCSessionFileTransfer
```

#### Return Value

A file transfer object containing the file and dictionary being sent. You can use this object to cancel the file transfer at a later time.

#### Discussion

Use this method to send a file that’s local to the current device. Files are transferred to the counterpart asynchronously on a background thread. The system attempts to send files as quickly as possible but may throttle delivery speeds to accommodate performance and power concerns. Use the [`outstandingFileTransfers`](wcsession/outstandingfiletransfers.md) method to get a list of files that are queued for delivery but have not yet been delivered to the counterpart.

If the file and its accompanying dictionary can’t be sent, the session object calls the session:fileTransfer:didFinishWithError: method of its delegate and reports an error. Errors may occur if the dictionary contains non-property list object types or if the specified URL doesn’t contain a valid file.

This method can only be called while the session is active (the [`activationState`](wcsession/activationstate.md) property is set to [`WCSessionActivationState.activated`](wcsessionactivationstate/activated.md)). Calling this method for an inactive or deactivated session is a programmer error.

> ⚠️ **Warning**:  Always test Watch Connectivity file transfers on paired devices. The Simulator app doesn’t support the [`transferFile(_:metadata:)`](wcsession/transferfile(_:metadata:).md) method.

 Always test Watch Connectivity file transfers on paired devices. The Simulator app doesn’t support the [`transferFile(_:metadata:)`](wcsession/transferfile(_:metadata:).md) method.

## Parameters

- `file`: A file-based URL that identifies the file to send. The specified file must be readable by the current app. This parameter must not be  .
- `metadata`: An optional dictionary containing additional data to send. The values of the dictionary must all be property list object types. You may specify   for this parameter.

## See Also

- [var outstandingFileTransfers: [WCSessionFileTransfer]](wcsession/outstandingfiletransfers.md)
  An array of in-progress file transfers.
- [var hasContentPending: Bool](wcsession/hascontentpending.md)
  A Boolean value that indicates whether the session has more content to deliver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/transferfile(_:metadata:))*