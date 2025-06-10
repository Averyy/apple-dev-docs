# Pass

**Framework**: Wallet Passes  
**Kind**: dictionary

An object that represents a pass.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- watchOS 1.0+

## Declaration

```swift
object Pass
```

## Mentions

- [Supporting semantic tags in Wallet passes](supporting-semantic-tags-in-wallet-passes.md)
- [Showing a Pass on the Lock Screen](showing-a-pass-on-the-lock-screen.md)
- [Adding a Web Service to Update Passes](adding-a-web-service-to-update-passes.md)
- [Building a Pass](building-a-pass.md)
- [Creating the Source for a Pass](creating-the-source-for-a-pass.md)
- [Distributing and updating a pass](distributing-and-updating-a-pass.md)

## Topics

### Setting the pass type
- [object Pass.BoardingPass](pass/boardingpass-data.dictionary.md)
  An object that represents the groups of fields that display the information for a boarding pass.
- [object Pass.Coupon](pass/coupon-data.dictionary.md)
  An object that represents the groups of fields that display the information for a coupon.
- [object Pass.EventTicket](pass/eventticket-data.dictionary.md)
  An object that represents the groups of fields that display the information for an event ticket.
- [object Pass.Generic](pass/generic-data.dictionary.md)
  An object that represents the groups of fields that display the information for a generic pass.
### Adding content
- [object PassFields](passfields.md)
  An object that represents the groups of fields that display information on the front and back of a pass.
- [object PassFieldContent](passfieldcontent.md)
  An object that represents the information to display in a field on a pass.
### Adding system suggestions
- [Supporting semantic tags in Wallet passes](supporting-semantic-tags-in-wallet-passes.md)
  Enable the system to offer suggestions for actions related to passes by adding machine-readable metadata.
- [object SemanticTags](semantictags.md)
  An object that contains machine-readable metadata the system uses to offer a pass and suggest related actions.
- [object SemanticTagType](semantictagtype.md)
  A compilation of data object types for semantic tags.
### Adding barcodes
- [object Pass.Barcodes](pass/barcodes-data.dictionary.md)
  An object that represents a barcode on a pass.
- [object Pass.Barcode](pass/barcode-data.dictionary.md)
  An object that represents a barcode shown on a pass.
### Adding relevance
- [Showing a Pass on the Lock Screen](showing-a-pass-on-the-lock-screen.md)
  Add information to your pass so the system can display it on the Lock Screen at a relevant time and place.
- [object Pass.Locations](pass/locations-data.dictionary.md)
  An object that represents a location that the system uses to show a relevant pass.
- [object Pass.Beacons](pass/beacons-data.dictionary.md)
  An object that represents the identifier of a Bluetooth Low Energy beacon the system uses to show a relevant pass.
- [object Pass.RelevantDates](pass/relevantdates-data.dictionary.md)
  An object that represents a date interval that the system uses to show a relevant pass.
### Adding near-field communications
- [object Pass.NFC](pass/nfc-data.dictionary.md)
  An object that represents the near-field communication (NFC) payload the device passes to an Apple Pay terminal.
### Adding personalization information
- [object Pass.StoreCard](pass/storecard-data.dictionary.md)
  An object that represents groups of fields that show the information for a store card.
- [object Personalize](personalize.md)
  An object that contains the personalization information for a rewards pass.

## See Also

- [Creating the Source for a Pass](creating-the-source-for-a-pass.md)
  Create the directory structure and add source files and images to define a pass.
- [Building a Pass](building-a-pass.md)
  Build a distributable pass.
- [Distributing and updating a pass](distributing-and-updating-a-pass.md)
  Distribute a pass to your users or update an existing pass.
- [Creating the Source for a Pass](creating-the-source-for-a-pass.md)
  Create the directory structure and add source files and images to define a pass.
- [Building a Pass](building-a-pass.md)
  Build a distributable pass.
- [Distributing and updating a pass](distributing-and-updating-a-pass.md)
  Distribute a pass to your users or update an existing pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/pass)*