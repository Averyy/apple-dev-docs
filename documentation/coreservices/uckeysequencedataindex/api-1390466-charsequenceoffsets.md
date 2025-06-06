# charSequenceOffsets

**Framework**: Core Services  
**Kind**: structp

An array of offsets from the beginning of the `UCKeySequenceDataIndex` structure to the Unicode character sequences that follow it. Because a given offset indicates both the beginning of a new character sequence and the end of the sequence that precedes it, the length of each sequence is determined by the difference between the offset to that sequence and the value of the next offset in the array. The array contains one more entry than the number of character sequences; the final entry is the offset to the end of the final character sequence.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var charSequenceOffsets: UInt16
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/uckeysequencedataindex/1390466-charsequenceoffsets)*