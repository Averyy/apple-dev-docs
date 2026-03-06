# Return

**Framework**: Wallet Orders  
**Kind**: dictionary

The details of a return order.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 14.2+
- macOS 14.2+

## Declaration

```swift
object Return
```

## Properties

- `returnIdentifier` (string) *(required)*: A unique identifier for the return. This isn’t displayed to the user, and is only used for identifying changes and user notifications.
- `status` (string) *(required)*: The status of the return.
- `carrier` (string): The carrier used to return the products.
- `dropOffBy` (date-time): The date and time for the product drop-off. Use `ISO 8601` format.
- `initiatedAt` (date-time): The date and time for the initated return. Use `ISO 8601` format.
- `lineItems` ([LineItem]): An array of line items for the customer to return, displayed in the order provided.
- `notes` (string): Additional information about the return.
- `returnedAt` (date-time): The return date and time of a product. Use `ISO 8601` format.
- `returnLabel` (string): A printable filename of a label within the bundle used to mail the products back. The total size of the bundle must be below 5 MB. - Supports, `PDF`, `JPG`, and `PNG` labels.
- `returnManagementURL` (uri): A URL where the customer can manage the return.
- `returnNumber` (string): The number of the return displayed to the customer.
- `statusDescription` (string): A localized message describing the return status.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletorders/return)*