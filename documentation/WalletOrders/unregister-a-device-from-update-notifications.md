# Unregister a device from update notifications

**Framework**: Wallet Orders  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Unregisters a device from receiving update notifications for an order.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+

## Endpoint

`DELETE https://your-web-service.com/v1/devices/{deviceIdentifier}/registrations/{orderTypeIdentifier}/{orderIdentifier}`

## Parameters

### Path Parameters

- `orderIdentifier` (string) *(required)*: The order identifier. This value corresponds to the value of the `orderIdentifier` key of the [`Order`](./order.md).
- `orderTypeIdentifier` (string) *(required)*: The order type identifier of the order. This value corresponds to the value of the `orderTypeIdentifier` key of the [`Order`](./order.md).
- `deviceIdentifier` (string) *(required)*: A unique identifier for the device.

### Header Parameters

- `Authorization` (string) *(required)*: The authentication for an order. The scheme is `AppleOrder` with the order’s value for the `authenticationToken` key as parameter. For example, `AppleOrder {authenticationToken}`.

  **Allowed Values**: `AppleOrder {authenticationToken}`

## Responses

- `200` Device Unregistered: The device successfully unregistered.
- `401` Request Not Authorized: The request isn’t authorized.

## See Also

### Notifications
- [Register a device for update notifications](./register-a-device-for-update-notifications.md)
  Registers a device to receive update notifications for an order.
- [object PushToken](./pushtoken.md)
  The push token APNS uses to send update notifications to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletorders/unregister-a-device-from-update-notifications)*