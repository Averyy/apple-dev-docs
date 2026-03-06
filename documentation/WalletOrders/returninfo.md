# ReturnInfo

**Framework**: Wallet Orders  
**Kind**: dictionary

The information related to a partial or full return.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- macOS 14.2+

## Declaration

```swift
object ReturnInfo
```

## Properties

- `returnPolicyURL` (uri) *(required)*: The URL where the customer can see the order return policy.
- `displayCountdown` (boolean): A Boolean value that indicates whether to display the return countdown until `returnDeadline` in the user interface. Use `true` if all of the items in the order are returnable until the `returnDeadline`. Default: `false`
- `returnDeadline` (date-time): The date where the products can be partially or fully returned. The merchant can provide updates to an order that has a completed status until this date. Use `ISO 8601` format.
- `returnManagementURL` (uri): The URL where the customer can initiate a return.
- `returnPolicyDescription` (string): A short description of the return policy. The merchant can include the common return window duration here.

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

*[View on Apple Developer](https://developer.apple.com/documentation/walletorders/returninfo)*