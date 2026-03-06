# UpcomingPassInformationEntry

**Framework**: Wallet Passes  
**Kind**: dictionary

An object that represents the ordered list of all upcoming pass information entries.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- watchOS 26.0+

## Declaration

```swift
object UpcomingPassInformationEntry
```

## Topics

### Adding information to multievent passes
- [object UpcomingPassInformationEntry.AdditionalInfoFields](upcomingpassinformationentry/additionalinfofields-data.dictionary.md)
  The fields of information that display in the Additional Info section below a pass.
- [object UpcomingPassInformationEntry.BackFields](upcomingpassinformationentry/backfields-data.dictionary.md)
  The fields of information displayed in the details view  of the upcoming pass information entry.
- [object UpcomingPassInformationEntry.DateInformation](upcomingpassinformationentry/dateinformation-data.dictionary.md)
  Information about the start and end time of the upcoming pass information entry.
- [object UpcomingPassInformationEntry.Images](upcomingpassinformationentry/images-data.dictionary.md)
  A collection of image names used to populate images in the details view.
- [object UpcomingPassInformationEntry.URLs](upcomingpassinformationentry/urls-data.dictionary.md)
  An object with links to information about the upcoming pass information entry.

## Properties

- `URLs` (UpcomingPassInformationEntry.URLs): A collection of URLs used to populate UI elements in the details view.
- `additionalInfoFields` (UpcomingPassInformationEntry.AdditionalInfoFields): The fields of information displayed on the `Additional Info` section below a pass.
- `auxiliaryStoreIdentifiers` ([number]): An array of App Store identifiers for apps associated with the upcoming pass information entry. The associated app on a device is the first item in the array that’s compatible with that device. This key works only for upcoming pass information entries for an event. A link to launch the app is in the event guide of the entry details view. If the app isn’t installed, the link opens to the App Store.
- `backFields` (UpcomingPassInformationEntry.BackFields): The fields of information displayed on the details view of the upcoming pass information entry.
- `dateInformation` (UpcomingPassInformationEntry.DateInformation): Information about the start and end time of the upcoming pass information entry. If omitted, the entry is labeled as `TBD`.
- `identifier` (string) *(required)*: A string that uniquely identifies the upcoming pass information entry. The identifier needs to be unique for each upcoming information entry.
- `images` (UpcomingPassInformationEntry.Images): A collection of image names used to populate images in the details view.
- `isActive` (boolean): Indicates whether the upcoming pass information entry is currently active. The default value is `false`.
- `name` (localizable string) *(required)*: The name of the upcoming pass information entry.
- `semantics` (SemanticTags): The semantic, machine-readable metadata about the upcoming pass information entry.
- `type` (string) *(required)*: The type of upcoming pass information entry.

## See Also

- [object UpcomingPassInformationEntryType](upcomingpassinformationentrytype.md)
  An object that represents a upcoming pass information entry for an specific upcoming event.
- [Creating a poster event pass using semantic tags](creating-an-event-pass-using-semantic-tags.md)
  Use semantic tags to provide up-to-date information for event passes.
- [object Pass.EventTicket](pass/eventticket-data.dictionary.md)
  An object that represents the groups of fields that display the information for an event ticket.
- [object SemanticTags](semantictags.md)
  An object that contains machine-readable metadata the system uses to offer a pass and suggest related actions.
- [object SemanticTagType](semantictagtype.md)
  A compilation of data object types for semantic tags.
- [object UpcomingPassInformationEntryType](upcomingpassinformationentrytype.md)
  An object that represents a upcoming pass information entry for an specific upcoming event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/upcomingpassinformationentry)*