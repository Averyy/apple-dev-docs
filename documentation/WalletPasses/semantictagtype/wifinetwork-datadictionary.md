# SemanticTagType.WifiNetwork

**Framework**: Wallet Passes  
**Kind**: dictionary

An object that contains information required to connect to a Wi-Fi network. Optionally, this object may contain keys required to perform authentication with captive portal.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- watchOS 5.0+

## Declaration

```swift
object SemanticTagType.WifiNetwork
```

## Properties

- `password` (string) *(required)*: The password for the Wi-Fi network.
- `ssid` (string) *(required)*: The name for the Wi-Fi network.
- `captiveToken` (string): Token credential required to log in to Captive Portal.
- `captiveTokenAuthURL` (string): The URL of the authentication server that verifies the client using a token credential.

## See Also

- [object SemanticTagType.CurrencyAmount](semantictagtype/currencyamount-data.dictionary.md)
  An object that represents an amount of money and type of currency.
- [object SemanticTagType.EventDateInfo](semantictagtype/eventdateinfo-data.dictionary.md)
  An object that represents a date for an event.
- [object SemanticTagType.Location](semantictagtype/location-data.dictionary.md)
  An object that represents the coordinates of a location.
- [object SemanticTagType.PersonNameComponents](semantictagtype/personnamecomponents-data.dictionary.md)
  An object that represents the parts of a person’s name.
- [object SemanticTagType.Seat](semantictagtype/seat-data.dictionary.md)
  An object that represents the identification of a seat for a transit journey or an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/semantictagtype/wifinetwork-data.dictionary)*