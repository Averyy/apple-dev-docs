# PassFields.SecondaryFields

**Framework**: Wallet Passes  
**Kind**: dictionary

An object that represents the fields that display supporting information on the front of a pass.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- watchOS 1.0+

## Declaration

```swift
object PassFields.SecondaryFields
```

## Mentions

- [Creating an airline boarding pass using semantic tags](creating-an-airline-boarding-pass-using-semantic-tags.md)
- [Creating a poster event pass using semantic tags](creating-an-event-pass-using-semantic-tags.md)
- [Supporting semantic tags in Wallet passes](supporting-semantic-tags-in-wallet-passes.md)

#### Discussion

Use this field to provide information that people might not need every time they use the pass, for example, the flight number on a boarding pass, or a coupon expiration date.

Depending on the type of pass, you can use the secondary and auxiliary fields interchangeably. Coupons, store cards, and generic passes with a square barcode can have a combined total of up to four secondary and auxiliary fields.

## Relationships

### Inherits From
- [PassFieldContent](passfieldcontent.md)

## See Also

- [object PassFields.PrimaryFields](passfields/primaryfields-data.dictionary.md)
  An object that represents the fields that display the most important information on the front of a pass.
- [object PassFields.AuxiliaryFields](passfields/auxiliaryfields-data.dictionary.md)
  An object that represents the fields that display additional information on the front of a pass.
- [object PassFields.HeaderFields](passfields/headerfields-data.dictionary.md)
  An object that represents the fields that display information at the top of a pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/passfields/secondaryfields-data.dictionary)*