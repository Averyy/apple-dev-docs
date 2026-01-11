# PassFields.AuxiliaryFields

**Framework**: Wallet Passes  
**Kind**: dictionary

An object that represents the fields that display additional information on the front of a pass.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- watchOS 1.0+

## Declaration

```swift
object PassFields.AuxiliaryFields
```

## Mentions

- [Creating an airline boarding pass using semantic tags](creating-an-airline-boarding-pass-using-semantic-tags.md)
- [Supporting semantic tags in Wallet passes](supporting-semantic-tags-in-wallet-passes.md)

#### Discussion

Use this field to provide information that people might not need every time they use the pass.

Depending on the type of pass, you can interchange the auxiliary and secondary fields. Coupons, store cards, and generic passes with a square barcode can have a combined total of up to four secondary and auxiliary fields.

## Relationships

### Inherits From
- [PassFieldContent](passfieldcontent.md)

## See Also

- [object PassFields.PrimaryFields](passfields/primaryfields-data.dictionary.md)
  An object that represents the fields that display the most important information on the front of a pass.
- [object PassFields.SecondaryFields](passfields/secondaryfields-data.dictionary.md)
  An object that represents the fields that display supporting information on the front of a pass.
- [object PassFields.HeaderFields](passfields/headerfields-data.dictionary.md)
  An object that represents the fields that display information at the top of a pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/passfields/auxiliaryfields-data.dictionary)*