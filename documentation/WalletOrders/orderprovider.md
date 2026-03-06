# OrderProvider

**Framework**: Wallet Orders  
**Kind**: dictionary

Information about the platform providing the order data.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.4+

## Declaration

```swift
object OrderProvider
```

## Properties

- `displayName` (string) *(required)*: The localized display name of the order provider platform.
- `trackingLogoNameDarkColorScheme` (string) *(required)*: The name of the logo image for the order provider that’s intended for the dark color scheme. When the shipping fulfilment has a `trackingURL`, it uses this image.
- `trackingLogoNameLightColorScheme` (string) *(required)*: The name of the logo image for the order provider that’s intended for the light color scheme. When the shipping fulfilment has a `trackingURL`, it uses this image.
- `url` (uri) *(required)*: The URL of the order provder platform.

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

*[View on Apple Developer](https://developer.apple.com/documentation/walletorders/orderprovider)*