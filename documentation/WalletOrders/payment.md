# Payment

**Framework**: Wallet Orders  
**Kind**: dictionary

The payment information associated with the order.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+

## Declaration

```swift
object Payment
```

## Topics

### Dictionaries
- [object Payment.SummaryItems](payment/summaryitems-data.dictionary.md)
  A breakdown of the total payment.

## Properties

- `total` (CurrencyAmount) *(required)*: The total amount to be paid.
- `summaryItems` ([Payment.SummaryItems]): A breakdown of the total payment. For example, shipping cost and taxes.
- `transactions` ([PaymentTransaction]): A list of [`PaymentTransaction`](paymenttransaction.md) dictionaries.
- `paymentMethods` ([string]): A list of methods used to pay. For example, MasterCard 1234 or Visa 5678.
- `status` (string) *(required)*: The status of the payment.
- `applePayTransactionIdentifiers` ([string]): An optional list of Apple Pay transaction identifiers relating to this order. Wallet links the original transaction to your order by default. If you charge a user multiple times, you can provide the relevant transaction identifiers here to enable additional linking.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletorders/payment)*