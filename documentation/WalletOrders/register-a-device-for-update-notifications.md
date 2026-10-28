# Register a device for update notifications

**Framework**: Wallet Orders  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Registers a device to receive update notifications for an order.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+

## Discussion

When the system modifies an order, use the [`PushToken`](./pushtoken.md) to send a push notification to the device. In the notification, set the push topic as the order type identifier and leave the payload empty.

## Endpoint

`POST https://your-web-service.com/v1/devices/{deviceIdentifier}/registrations/{orderTypeIdentifier}/{orderIdentifier}`

## Parameters

### Path Parameters

- `orderIdentifier` (string) *(required)*: The order identifier. This value corresponds to the value of the `orderIdentifier` key of the [`Order`](./order.md).
- `orderTypeIdentifier` (string) *(required)*: The order type identifier of the order. This value corresponds to the value of the `orderTypeIdentifier` key of the [`Order`](./order.md).
- `deviceIdentifier` (string) *(required)*: A unique identifier for the device.

### Header Parameters

- `Authorization` (string) *(required)*: The authentication for an order. The scheme is `AppleOrder` with the order’s value for the `authenticationToken` key as parameter. For example, `AppleOrder {authenticationToken}`.

  **Allowed Values**: `AppleOrder {authenticationToken}`

## Request Body

**Content-Type**: `application/json`  
**Type**: `PushToken`

The push token APNS uses to send update notifications to the device.

## Responses

- `200` Device Already Registered: The device is already registered for the order.
- `201` Device Registered: The device successfully registered for the order.
- `401` Request Not Authorized: The request isn’t authorized.

## See Also

### Notifications
- [Unregister a device from update notifications](./unregister-a-device-from-update-notifications.md)
  Unregisters a device from receiving update notifications for an order.
- [object PushToken](./pushtoken.md)
  The push token APNS uses to send update notifications to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletorders/register-a-device-for-update-notifications)*