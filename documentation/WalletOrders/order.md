# Order

**Framework**: Wallet Orders  
**Kind**: dictionary

The order’s details, including information about the products or services rendered, customer service, and fulfillment.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+

## Declaration

```swift
object Order
```

## Mentions

- [Building a distributable order package](building-a-distributable-order-package.md)
- [Creating the source for an order](creating-the-source-for-an-order.md)

## Topics

### Supporting objects
- [object Customer](customer.md)
  The details of the order’s customer.
- [object Merchant](merchant.md)
  The merchant associated with the order.
- [object Address](address.md)
  The physical address for an order.
- [object Application](application.md)
  The details of an app in the App Store.
- [object Barcode](barcode.md)
  The details of a barcode for an order.
- [object CurrencyAmount](currencyamount.md)
  An amount of money.
- [object LineItem](lineitem.md)
  An item associated with the order.
- [object Location](location.md)
  A geographic location.
- [object OrderIdentifiers](orderidentifiers.md)
  The unique identifiers associated with orders.
- [object OrderProvider](orderprovider.md)
  Information about the platform providing the order data.
- [object Payment](payment.md)
  The payment information associated with the order.
- [object Payment.SummaryItems](payment/summaryitems-data.dictionary.md)
  A breakdown of the total payment.
- [object PaymentMethod](paymentmethod.md)
  The payment method for the transaction.
- [object PaymentTransaction](paymenttransaction.md)
  The details about a payment transaction.
- [object PickupFulfillment](pickupfulfillment.md)
  The details of a pickup order.
- [object Return](return.md)
  The details of a return order.
- [object ReturnInfo](returninfo.md)
  The information related to a partial or full return.
- [object ShippingFulfillment](shippingfulfillment.md)
  The details of a shipped order.
- [object ShippingFulfillment.Recipient](shippingfulfillment/recipient-data.dictionary.md)
  The recipient of the shipment.

## Properties

- `createdAt` (date-time) *(required)*: The date and time when the customer created the order, in RFC 3339 format.
- `merchant` (Merchant) *(required)*: The merchant for this order.
- `orderIdentifier` (string) *(required)*: A unique order identifier scoped to your order type identifier. In combination with the order type identifier, this uniquely identifies an order within the system and isn’t displayed to the user.
- `orderManagementURL` (uri) *(required)*: A URL where the customer can manage the order.
- `orderType` (string) *(required)*: The type of order this bundle represents. Currently the only supported value is `ecommerce`.
- `orderTypeIdentifier` (string) *(required)*: An identifier for the order type associated with the order. The value must correspond with your signing certificate and isn’t displayed to the user.
- `status` (string) *(required)*: A high-level status of the order, used for display purposes. The system considers orders with status `completed` or `cancelled` closed.
- `schemaVersion` (number) *(required)*: The version of the schema used for the order. The current version is `1`.
- `updatedAt` (date-time) *(required)*: The date and time when the order was last updated, in RFC 3339 format. This should equal the `createdAt` time, if the order hasn’t had any updates. Must be monotonically increasing. Consider using a hybrid logical clock if your web service can’t make that guarantee.
- `associatedApplications` ([Application]): A list of associated applications, in order of preference. The device uses the first available application.
- `associatedApplicationIdentifiers` ([string]): The application identifier associated with the order.
- `authenticationToken` (string): The authentication token supplied to your web service. Required if you provide a web service.
- `barcode` (Barcode): An identifier containing information about an order.
- `changeNotifications` (string): A property that describes whether the device notifies the user about relevant changes to the order. The default is `enabled`.
- `customer` (Customer): The customer for this order.
- `fulfillments` ([*]): A list of fulfillments. The device displays fulfillments in the order provided.
- `lineItems` ([LineItem]): The items contained in the order, displayed in the order provided.
- `orderNumber` (string): If available, an order number or reference suitable for display to the user.
- `orderProvider` (OrderProvider): Information about the platform providing the order data. Use this field if the order data isn’t provided by the merchant, but by a third party.
- `payment` (Payment): The payment for this order.
- `returnInfo` (ReturnInfo): The information related to a partial or full return.
- `returns` ([Return]): A list of returns. The device displays returns in the order provided.
- `statusDescription` (string): A localized message describing the order status.
- `webServiceURL` (uri): The URL of your web service. This must begin with `HTTPS://`.

## See Also

- [Creating the source for an order](creating-the-source-for-an-order.md)
  Define an order by creating the directory structure, and adding source files and images.
- [Building a distributable order package](building-a-distributable-order-package.md)
  Prepare an order for distribution by building, signing, and compressing the source files.
- [Retrieve the registrations for a device](retrieve-the-registrations-for-a-device.md)
  Retrieves the identifiers of the orders that the device registered for.
- [Retrieve the latest version of an order](retrieve-the-latest-version-of-an-order.md)
  Retrieves the latest signed and compressed version of an order.
- [Example Order Packages](example-order-packages.md)
  Edit, build, and add example order packages to Wallet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletorders/order)*