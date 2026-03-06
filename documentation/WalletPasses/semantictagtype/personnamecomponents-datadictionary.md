# SemanticTagType.PersonNameComponents

**Framework**: Wallet Passes  
**Kind**: dictionary

An object that represents the parts of a person’s name.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- watchOS 5.0+

## Declaration

```swift
object SemanticTagType.PersonNameComponents
```

## Properties

- `familyName` (string): The person’s family name or last name.
- `givenName` (string): The person’s given name; also called the *forename* or *first name* in some countries.
- `middleName` (string): The person’s middle name.
- `namePrefix` (string): The prefix for the person’s name, such as `“Dr”`.
- `nameSuffix` (string): The suffix for the person’s name, such as `“Junior”`.
- `nickname` (string): The person’s nickname.
- `phoneticRepresentation` (string): The phonetic representation of the person’s name.

## See Also

- [object SemanticTagType.CurrencyAmount](semantictagtype/currencyamount-data.dictionary.md)
  An object that represents an amount of money and type of currency.
- [object SemanticTagType.EventDateInfo](semantictagtype/eventdateinfo-data.dictionary.md)
  An object that represents a date for an event.
- [object SemanticTagType.Location](semantictagtype/location-data.dictionary.md)
  An object that represents the coordinates of a location.
- [object SemanticTagType.Seat](semantictagtype/seat-data.dictionary.md)
  An object that represents the identification of a seat for a transit journey or an event.
- [object SemanticTagType.WifiNetwork](semantictagtype/wifinetwork-data.dictionary.md)
  An object that contains information required to connect to a Wi-Fi network. Optionally, this object may contain keys required to perform authentication with captive portal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/semantictagtype/personnamecomponents-data.dictionary)*