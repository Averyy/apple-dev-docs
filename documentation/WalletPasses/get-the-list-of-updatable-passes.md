# Get the List of Updatable Passes

**Framework**: Wallet Passes  
**Kind**: httpRequest

Send the serial numbers for updated passes to a device.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- watchOS 3.0+

## Mentions

- [Adding a Web Service to Update Passes](adding-a-web-service-to-update-passes.md)

## Endpoint

`GET https://yourpasshost.example.com/v1/devices/{deviceLibraryIdentifier}/registrations/{passTypeIdentifier}?passesUpdatedSince={previousLastUpdated}`

## Parameters

- `deviceLibraryIdentifier` (string) *(required)*: The unique identifier for the device.
- `passTypeIdentifier` (string) *(required)*: The pass type identifier of the pass to check for updates. This value corresponds to the value of the `passTypeIdentifier` key of the pass.
- `previousLastUpdated` (string) *(required)*: The value of the `lastUpdated` key from the [`SerialNumbers`](serialnumbers.md) object returned in a previous request. This value limits the results of the current request to the passes updated since that previous request.

## See Also

- [Adding a Web Service to Update Passes](adding-a-web-service-to-update-passes.md)
  Implement a web server to register, update, and unregister a pass on a device.
- [Register a Pass for Update Notifications](register-a-pass-for-update-notifications.md)
  Set up change notifications for a pass on a device.
- [Send an Updated Pass](send-an-updated-pass.md)
  Create and sign an updated pass, and send it to the device.
- [Unregister a Pass for Update Notifications](unregister-a-pass-for-update-notifications.md)
  Stop sending update notifications for a pass on a device.
- [Log a Message](log-a-message.md)
  Record a message on your server.
- [object PushToken](pushtoken.md)
  An object that contains the push notification token for a registered pass on a device.
- [object SerialNumbers](serialnumbers.md)
  An object that contains serial numbers for the updatable passes on a device.
- [object LogEntries](logentries.md)
  An object that contains an array of messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/get-the-list-of-updatable-passes)*