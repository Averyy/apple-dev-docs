# PhonemeInfo

**Framework**: Application Services  
**Kind**: struct

Defines a structure that stores information about a phoneme.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct PhonemeInfo
```

#### Overview

Ordinarily, you use a phoneme information structure to show the user how to enter text to represent a particular phoneme when the `'PHON'` input mode is activated.

You might use the information contained in the `hiliteStart` and `hiliteEnd` fields to highlight the characters in the example word that represent the phoneme.

To obtain a phoneme information structure for an individual phoneme, you must obtain a list of phonemes through a phoneme descriptor structure. 

## Topics

### Initializers
- [init()](phonemeinfo/1461979-init.md)
- [init(opcode: Int16, phStr: Str15, exampleStr: Str31, hiliteStart: Int16, hiliteEnd: Int16)](phonemeinfo/1459158-init.md)
### Instance Properties
- [var exampleStr: Str31](phonemeinfo/1460341-examplestr.md)
  An example word that illustrates use of the phoneme.
- [var hiliteEnd: Int16](phonemeinfo/1464802-hiliteend.md)
  The number of characters between the beginning of the example word and the end of the portion of that word representing the phoneme.
- [var hiliteStart: Int16](phonemeinfo/1464138-hilitestart.md)
  The number of characters in the example word that precede the portion of that word representing the phoneme.
- [var opcode: Int16](phonemeinfo/1459025-opcode.md)
  The opcode for the phoneme.
- [var phStr: Str15](phonemeinfo/1461253-phstr.md)
  The string used to represent the phoneme. The string does not necessarily have a phonetic connection to the phoneme, but might simply be an abstract textual representation of it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/phonemeinfo)*