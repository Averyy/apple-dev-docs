# Send an Updated Pass

**Framework**: Wallet Passes  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create and sign an updated pass, and send it to the device.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- watchOS 3.0+

## Endpoint

`GET https://yourpasshost.example.com/v1/passes/{passTypeIdentifier}/{serialNumber}`

## Parameters

### Path Parameters

- `passTypeIdentifier` (string) *(required)*: The pass type identifier of the pass to update. This value corresponds to the value of the `passTypeIdentifier` key of the pass.
- `serialNumber` (string) *(required)*: The serial number of the pass to update. This value corresponds to the `serialNumber` key of the pass.

### Header Parameters

- `Authorization` (string): The authentication for a pass. The value is the word `ApplePass`, followed by a space, followed by the `authenticationToken` key of the pass.

  **Allowed Values**: `ApplePass {passAuthorizationToken}`

## Responses

- `200` OK (`application/vnd.apple.pkpass`): The request is successful and returns the updated pass.
- `401` Request Not Authorized: The request isn’t authorized.

## See Also

### Pass updates
- [Adding a Web Service to Update Passes](./adding-a-web-service-to-update-passes.md)
  Implement a web server to register, update, and unregister a pass on a device.
- [Register a Pass for Update Notifications](./register-a-pass-for-update-notifications.md)
  Set up change notifications for a pass on a device.
- [Get the List of Updatable Passes](./get-the-list-of-updatable-passes.md)
  Send the serial numbers for updated passes to a device.
- [Unregister a Pass for Update Notifications](./unregister-a-pass-for-update-notifications.md)
  Stop sending update notifications for a pass on a device.
- [Log a Message](./log-a-message.md)
  Record a message on your server.
- [object PushToken](./pushtoken.md)
  An object that contains the push notification token for a registered pass on a device.
- [object SerialNumbers](./serialnumbers.md)
  An object that contains serial numbers for the updatable passes on a device.
- [object LogEntries](./logentries.md)
  An object that contains an array of messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/send-an-updated-pass)*