# Pass.BoardingPass

**Framework**: Wallet Passes  
**Kind**: dictionary

An object that represents the groups of fields that display the information for a boarding pass.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- watchOS 1.0+

## Declaration

```swift
object Pass.BoardingPass
```

## Mentions

- [Creating an airline boarding pass using semantic tags](creating-an-airline-boarding-pass-using-semantic-tags.md)

#### Discussion

Use the boarding pass type for transit passes like airline boarding passes, train tickets, and bus tickets.

## Properties

- `transitType` (string) *(required)*: The type of transit for a boarding pass. This key is invalid for other types of passes. The system may use the value to display more information, such as showing an airplane icon for the pass on watchOS when the value is set to `PKTransitTypeAir`.

## Relationships

### Inherits From
- [PassFields](passfields.md)

## See Also

- [Creating an airline boarding pass using semantic tags](creating-an-airline-boarding-pass-using-semantic-tags.md)
  Update your semantic tags to provide live and interactive passenger information for boarding passes.
- [object SemanticTags](semantictags.md)
  An object that contains machine-readable metadata the system uses to offer a pass and suggest related actions.
- [object SemanticTagType](semantictagtype.md)
  A compilation of data object types for semantic tags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/pass/boardingpass-data.dictionary)*