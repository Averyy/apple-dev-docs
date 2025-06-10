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