# SemanticTagType.Seat

**Framework**: Wallet Passes  
**Kind**: dictionary

An object that represents the identification of a seat for a transit journey or an event.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- watchOS 5.0+

## Declaration

```swift
object SemanticTagType.Seat
```

## Properties

- `seatAisle` (localizable string): The aisle that contains the seat.
- `seatDescription` (localizable string): A description of the seat, such as `A flat bed seat`.
- `seatIdentifier` (localizable string): The identifier code for the seat.
- `seatLevel` (localizable string): The level that contains the seat.
- `seatNumber` (localizable string): The number of the seat.
- `seatRow` (localizable string): The row that contains the seat.
- `seatSection` (localizable string): The section that contains the seat.
- `seatSectionColor` (RGB triple as string): A color associated with identifying the seat, specified as a CSS-style RGB triple, such as `rgb(23, 187, 82)`.
- `seatType` (localizable string): The type of seat, such as `Reserved seating`.

## See Also

- [object SemanticTagType.CurrencyAmount](semantictagtype/currencyamount-data.dictionary.md)
  An object that represents an amount of money and type of currency.
- [object SemanticTagType.EventDateInfo](semantictagtype/eventdateinfo-data.dictionary.md)
  An object that represents a date for an event.
- [object SemanticTagType.Location](semantictagtype/location-data.dictionary.md)
  An object that represents the coordinates of a location.
- [object SemanticTagType.PersonNameComponents](semantictagtype/personnamecomponents-data.dictionary.md)
  An object that represents the parts of a person’s name.
- [object SemanticTagType.WifiNetwork](semantictagtype/wifinetwork-data.dictionary.md)
  An object that contains information required to connect to a Wi-Fi network. Optionally, this object may contain keys required to perform authentication with captive portal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/semantictagtype/seat-data.dictionary)*