# PassFieldContent

**Framework**: Wallet Passes  
**Kind**: dictionary

An object that represents the information to display in a field on a pass.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- watchOS 1.0+

## Declaration

```swift
object PassFieldContent
```

## Mentions

- [Building a Pass](building-a-pass.md)
- [Creating the Source for a Pass](creating-the-source-for-a-pass.md)

#### Discussion

> **Note**:  Wallet uses data detectors to add links for text shown on the back of the pass.

## Properties

- `attributedValue` (localizable string, ISO 8601 date, or number): The value of the field, including HTML markup for links. The only supported tag is the `<a>` tag and its `href` attribute. The value of this key overrides that of the `value` key. For example, the following is a key-value pair that specifies a link with the text “Edit my profile”: `”attributedValue”: “<a href=’http://example.com/customers/123’>Edit my profile</a>”` The attributed value isn’t used for watchOS; use the `value` field instead.
- `changeMessage` (Localizable format string): A format string for the alert text to display when the pass updates. The format string needs to contain the escape `%@`, which the field’s new value replaces. For example, `Gate changed to %@`. You need to provide a value for the system to show a change notification. This field isn’t used for watchOS.
- `currencyCode` (ISO 4217 currency code as a string): The currency code to use for the value of the field.
- `dataDetectorTypes` ([string]): The data detectors to apply to the value of a field on the back of the pass. The default is to apply all data detectors. To use no data detectors, specify an empty array. You don’t use data detectors for fields on the front of the pass. This field isn’t used for watchOS.
- `dateStyle` (string): The style of the date to display in the field.
- `ignoresTimeZone` (boolean): A Boolean value that controls the time zone for the time and date to display in the field. The default value is `false`, which displays the time and date using the current device’s time zone. Otherwise, the time and date appear in the time zone associated with the date and time of `value`. This key doesn’t affect the pass relevance calculation.
- `isRelative` (boolean): A Boolean value that controls whether the date appears as a relative date. The default value is `false`, which displays the date as an absolute date. This key doesn’t affect  the pass relevance calculation.
- `key` (string) *(required)*: A unique key that identifies a field in the pass; for example, `“departure-gate”`.
- `label` (localizable string): The text for a field label.
- `numberStyle` (string): The style of the number to display in the field. Formatter styles have the same meaning as the formats with corresponding names in doc://com.apple.documentation/documentation/foundation/numberformatter/style.
- `textAlignment` (string): The alignment for the content of a field. The default is natural alignment, which aligns the text based on its script direction. This key is invalid for primary and back fields.
- `timeStyle` (string): The style of the time displayed in the field.
- `value` (localizable string, ISO 8601 date, or number) *(required)*: The value to use for the field; for example, `42`. A date or time value needs to include a time zone.

## Relationships

### Inherited By
- [PassFields.AdditionalInfoFields](passfields/additionalinfofields-data.dictionary.md)
- [PassFields.AuxiliaryFields](passfields/auxiliaryfields-data.dictionary.md)
- [PassFields.BackFields](passfields/backfields-data.dictionary.md)
- [PassFields.HeaderFields](passfields/headerfields-data.dictionary.md)
- [PassFields.PrimaryFields](passfields/primaryfields-data.dictionary.md)
- [PassFields.SecondaryFields](passfields/secondaryfields-data.dictionary.md)
- [UpcomingPassInformationEntry.AdditionalInfoFields](upcomingpassinformationentry/additionalinfofields-data.dictionary.md)
- [UpcomingPassInformationEntry.BackFields](upcomingpassinformationentry/backfields-data.dictionary.md)

## See Also

- [object PassFields](passfields.md)
  An object that represents the groups of fields that display information on the front and back of a pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/passfieldcontent)*