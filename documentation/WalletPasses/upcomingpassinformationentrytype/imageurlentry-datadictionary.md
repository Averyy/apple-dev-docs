# UpcomingPassInformationEntryType.ImageURLEntry

**Framework**: Wallet Passes  
**Kind**: dictionary

An object that represents the image specifications for the upcoming pass information entry.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- watchOS 26.0+

## Declaration

```swift
object UpcomingPassInformationEntryType.ImageURLEntry
```

## Properties

- `SHA256` (string) *(required)*: The SHA256 hash of the image.
- `URL` (string) *(required)*: The URL that points to the image asset to be downloaded. This must be an https link.
- `scale` (double): The scale of the image. If unspecified, defaults to 1.
- `size` (number): Size of the image asset in bytes. The maximum allowed size is 2 megabytes.

## See Also

- [object UpcomingPassInformationEntryType.Image](upcomingpassinformationentrytype/image-data.dictionary.md)
  An object that represents the image shown within the detail views of upcoming pass information entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/upcomingpassinformationentrytype/imageurlentry-data.dictionary)*