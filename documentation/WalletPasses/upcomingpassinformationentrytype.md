# UpcomingPassInformationEntryType

**Framework**: Wallet Passes  
**Kind**: dictionary

An object that represents a upcoming pass information entry for an specific upcoming event.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- watchOS 26.0+

## Declaration

```swift
object UpcomingPassInformationEntryType
```

## Topics

### Adding data for the type of multievent pass entry
- [object UpcomingPassInformationEntryType.Image](upcomingpassinformationentrytype/image-data.dictionary.md)
  An object that represents the image shown within the detail views of upcoming pass information entries.
- [object UpcomingPassInformationEntryType.ImageURLEntry](upcomingpassinformationentrytype/imageurlentry-data.dictionary.md)
  An object that represents the image specifications for the upcoming pass information entry.

## Properties

- `image` (UpcomingPassInformationEntryType.Image): An object that represents the the image shown on the pass.
- `imageURLEntry` (UpcomingPassInformationEntryType.ImageURLEntry): An object that represents the image speficiations for the pass.

## See Also

- [Creating a poster event pass using semantic tags](creating-an-event-pass-using-semantic-tags.md)
  Use semantic tags to provide up-to-date information for event passes.
- [object Pass.EventTicket](pass/eventticket-data.dictionary.md)
  An object that represents the groups of fields that display the information for an event ticket.
- [object SemanticTags](semantictags.md)
  An object that contains machine-readable metadata the system uses to offer a pass and suggest related actions.
- [object SemanticTagType](semantictagtype.md)
  A compilation of data object types for semantic tags.
- [object UpcomingPassInformationEntry](upcomingpassinformationentry.md)
  An object that represents the ordered list of all upcoming pass information entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/upcomingpassinformationentrytype)*