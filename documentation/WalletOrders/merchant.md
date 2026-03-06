# Merchant

**Framework**: Wallet Orders  
**Kind**: dictionary

The merchant associated with the order.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+

## Declaration

```swift
object Merchant
```

## Properties

- `address` (Address): The contact address of the merchant.
- `businessChatURL` (uri): An Apple Messages for Business URL the customer uses to contact the merchant. For more information, see [`Starting a Message from a URL`](https://developer.apple.comhttps://register.apple.com/resources/messages/messaging-documentation/message-with-customers#starting-a-message-from-a-url).
- `contactURL` (uri): The URL where the customer can contact the merchant.
- `displayName` (string) *(required)*: The localized display name of the merchant.
- `emailAddress` (string): The email address where the customer can contact the merchant.
- `logo` (string): The name for an image representing the merchant’s logo.
- `merchantIdentifier` (string) *(required)*: The Apple Merchant Identifier for this merchant, generated at [`developer.apple.com`](https://developer.apple.comhttps://developer.apple.com).
- `phoneNumber` (string): The telephone number where the customer can contact the merchant.
- `url` (uri) *(required)*: The URL for the merchant’s website or landing page.

## See Also

- [object Customer](customer.md)
  The details of the order’s customer.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletorders/merchant)*