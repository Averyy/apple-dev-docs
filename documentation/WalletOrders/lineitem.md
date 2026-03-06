# LineItem

**Framework**: Wallet Orders  
**Kind**: dictionary

An item associated with the order.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+

## Declaration

```swift
object LineItem
```

## Properties

- `image` (string): The name for an image representing the item.
- `price` (CurrencyAmount): The price of the line item.
- `quantity` (number) *(required)*: The number of items ordered.
- `subtitle` (string): A localized secondary display title for the item.
- `title` (string) *(required)*: A localized title for the item.
- `gtin` (string): The Global Trade Item Number of the item, if available. This could be an EAN, ISBN, or other value.
- `sku` (string): A merchant-specific unique product identifier.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletorders/lineitem)*