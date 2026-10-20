# SemanticTagType.CurrencyAmount

**Framework**: Wallet Passes  
**Kind**: dictionary  
**Role**: Object

An object that represents an amount of money and type of currency.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- watchOS 5.0+

## Declaration

```
object SemanticTagType.CurrencyAmount
```

## Properties

- `amount` (string): The amount of money.
- `currencyCode` (ISO 4217 currency code as a string): The currency code for `amount`.

## See Also

### Using semantic tag data types
- [object SemanticTagType.EventDateInfo](./eventdateinfo-data.dictionary.md)
  An object that represents a date for an event.
- [object SemanticTagType.Location](./location-data.dictionary.md)
  An object that represents the coordinates of a location.
- [object SemanticTagType.PersonNameComponents](./personnamecomponents-data.dictionary.md)
  An object that represents the parts of a person’s name.
- [object SemanticTagType.Seat](./seat-data.dictionary.md)
  An object that represents the identification of a seat for a transit journey or an event.
- [object SemanticTagType.WifiNetwork](./wifinetwork-data.dictionary.md)
  An object that contains information required to connect to a Wi-Fi network. Optionally, this object may contain keys required to perform authentication with captive portal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/semantictagtype/currencyamount-data.dictionary)*