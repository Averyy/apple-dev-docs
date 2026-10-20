# UpcomingPassInformationEntryType.Image

**Framework**: Wallet Passes  
**Kind**: dictionary  
**Role**: Object

An object that represents the image shown within the detail views of upcoming pass information entries.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- watchOS 26.0+

## Declaration

```
object UpcomingPassInformationEntryType.Image
```

## Properties

- `URLs` ([UpcomingPassInformationEntryType.ImageURLEntry]): A list of URLs used to retreive an image. The upcoming pass information entry uses the item that best matches the device’s scale.
- `reuseExisting` (boolean): Indicates whether to use the local equivalent image instead of the image specified by `URLs`.

## See Also

### Adding data for the type of multievent pass entry
- [object UpcomingPassInformationEntryType.ImageURLEntry](./imageurlentry-data.dictionary.md)
  An object that represents the image specifications for the upcoming pass information entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/upcomingpassinformationentrytype/image-data.dictionary)*