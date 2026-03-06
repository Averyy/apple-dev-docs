# Address

**Framework**: Wallet Orders  
**Kind**: dictionary

The physical address for an order.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+

## Declaration

```swift
object Address
```

## Properties

- `addressLines` ([string]): The street portion of the address.
- `administrativeArea` (string): The state or administrative area of the address.
- `countryCode` (string): The country of the address, in ISO-3166 two-letter format.
- `locality` (string): The city of the address.
- `postalCode` (string): The ZIP or postal code, where applicable, of the address.
- `subAdministrativeArea` (string): The subadministrative area (such as county or other region) of the address.
- `subLocality` (string): Additional information associated with the location, such as a district or neighborhood.

## See Also

- [object Customer](customer.md)
  The details of the order’s customer.
- [object Merchant](merchant.md)
  The merchant associated with the order.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletorders/address)*