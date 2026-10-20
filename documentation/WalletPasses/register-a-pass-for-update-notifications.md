# Register a Pass for Update Notifications

**Framework**: Wallet Passes  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Set up change notifications for a pass on a device.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- watchOS 3.0+

## Endpoint

`POST https://yourpasshost.example.com/v1/devices/{deviceLibraryIdentifier}/registrations/{passTypeIdentifier}/{serialNumber}`

## Parameters

### Path Parameters

- `deviceLibraryIdentifier` (string) *(required)*: A unique identifier you use to identify and authenticate the device.
- `passTypeIdentifier` (string) *(required)*: The pass type identifier of the pass to register for update notifications. This value corresponds to the value of the `passTypeIdentifier` key of the pass.
- `serialNumber` (string) *(required)*: The serial number of the pass to register. This value corresponds to the `serialNumber` key of the pass.

### Header Parameters

- `Authorization` (string): The authentication for a pass. The value is the word `ApplePass`, followed by a space, followed by the `authenticationToken` key of the pass.

  **Allowed Values**: `ApplePass {passAuthorizationToken}`

## Request Body

**Content-Type**: `application/json`  
**Type**: `PushToken`

An object that contains the push notification token for the registered pass on the device.

## Responses

- `200` Serial Number Already Registered for Device: The serial number is already registered for the device.
- `201` Registration Successful: The registration is successful.
- `401` Request Not Authorized: The request isn’t authorized.

## See Also

### Pass updates
- [Adding a Web Service to Update Passes](./adding-a-web-service-to-update-passes.md)
  Implement a web server to register, update, and unregister a pass on a device.
- [Get the List of Updatable Passes](./get-the-list-of-updatable-passes.md)
  Send the serial numbers for updated passes to a device.
- [Send an Updated Pass](./send-an-updated-pass.md)
  Create and sign an updated pass, and send it to the device.
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

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/register-a-pass-for-update-notifications)*