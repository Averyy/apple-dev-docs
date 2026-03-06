# PaymentTransaction

**Framework**: Wallet Orders  
**Kind**: dictionary

The details about a payment transaction.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 16.0+
- macOS 14.0+

## Declaration

```swift
object PaymentTransaction
```

## Properties

- `amount` (CurrencyAmount) *(required)*: The amount of the transaction.
- `createdAt` (date-time) *(required)*: The date and time when the framework created the transaction, in RFC 3339 format.
- `paymentMethod` (PaymentMethod) *(required)*: A string that represents the payment, such as a payment pass or card used for the transaction.
- `status` (string) *(required)*: The fulfillment status.
- `applePayTransactionIdentifier` (string): A string that represents the Apple Pay transaction ID.
- `transactionType` (string) *(required)*: The type of transaction.
- `receipt` (string): The filename of a receipt within the bundle that’s associated with the transaction.

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
- [object PickupFulfillment](pickupfulfillment.md)
  The details of a pickup order.
- [object Return](return.md)
  The details of a return order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletorders/paymenttransaction)*