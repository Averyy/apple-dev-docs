# UpcomingPassInformationEntry.DateInformation

**Framework**: Wallet Passes  
**Kind**: dictionary

Information about the start and end time of the upcoming pass information entry.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- watchOS 26.0+

## Declaration

```swift
object UpcomingPassInformationEntry.DateInformation
```

## Properties

- `date` (ISO 8601 date as string): The start date of the upcoming pass information entry. If omitted, the entry lists the `Time` and `Date` as TBD.
- `ignoreTimeComponents` (boolean): Indicates whether the entry should ignore the time components of the date.
- `isAllDay` (boolean): Indicates whether the entry spans the entire day and that the time components should be ignored.
- `isUnannounced` (boolean): Indicates whether the provided time of the event hasn’t been announced (commonly referred to as TBA).
- `isUndetermined` (boolean): Indicates whether the provided time of the event hasn’t been determined (commonly referred to as TBD).
- `timeZone` (Time zone database identifier as string): The time zone to adjust the date into. If omitted, the entry uses the current time zone of the device.

## See Also

- [object UpcomingPassInformationEntry.AdditionalInfoFields](upcomingpassinformationentry/additionalinfofields-data.dictionary.md)
  The fields of information that display in the Additional Info section below a pass.
- [object UpcomingPassInformationEntry.BackFields](upcomingpassinformationentry/backfields-data.dictionary.md)
  The fields of information displayed in the details view  of the upcoming pass information entry.
- [object UpcomingPassInformationEntry.Images](upcomingpassinformationentry/images-data.dictionary.md)
  A collection of image names used to populate images in the details view.
- [object UpcomingPassInformationEntry.URLs](upcomingpassinformationentry/urls-data.dictionary.md)
  An object with links to information about the upcoming pass information entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/upcomingpassinformationentry/dateinformation-data.dictionary)*