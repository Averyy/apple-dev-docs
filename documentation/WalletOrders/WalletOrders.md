# Wallet Orders

**Framework**: Wallet Orders  
**Kind**: module

Create, distribute, and update orders in Wallet.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+

#### Overview

Use Wallet Orders to give users the ability to track and manage their purchases in Wallet. You can donate an order to Wallet seamlessly through Apple Pay after payment authorization.

To give people the ability to track their orders in Wallet, you need to:

- Add order details to the payment authorization result.
- Build an order package and provide access through your web service.
- Update the order when the order’s state has changed.

## Topics

### Essentials
- [Creating the source for an order](creating-the-source-for-an-order.md)
  Define an order by creating the directory structure, and adding source files and images.
- [Building a distributable order package](building-a-distributable-order-package.md)
  Prepare an order for distribution by building, signing, and compressing the source files.
- [Retrieve the registrations for a device](retrieve-the-registrations-for-a-device.md)
  Retrieves the identifiers of the orders that the device registered for.
- [Retrieve the latest version of an order](retrieve-the-latest-version-of-an-order.md)
  Retrieves the latest signed and compressed version of an order.
- [object Order](order.md)
  The order’s details, including information about the products or services rendered, customer service, and fulfillment.
- [Example Order Packages](example-order-packages.md)
  Edit, build, and add example order packages to Wallet.
### Notifications
- [Register a device for update notifications](register-a-device-for-update-notifications.md)
  Registers a device to receive update notifications for an order.
- [Unregister a device from update notifications](unregister-a-device-from-update-notifications.md)
  Unregisters a device from receiving update notifications for an order.
- [object PushToken](pushtoken.md)
  The push token APNS uses to send update notifications to the device.
### Message logs
- [Receive log messages](receive-log-messages.md)
  Records log messages on your server.
- [object LogEntries](logentries.md)
  An array of log messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/WalletOrders)*