# UCKeyCharSeq

**Framework**: Core Services  
**Kind**: tdef

Specifies the output of a dead-key state in a `'uchr'` resource.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias UCKeyCharSeq = UInt16
```

#### Discussion

The Unicode keyboard-layout ( `'uchr'`) resource contains the data necessary to map virtual key codes to Unicode character codes for a given keyboard layout. The `'uchr'` format consists of a header information section and five key mapping data sections. The `UCKeyCharSeq` type is a 16-bit value used in the third key mapping section of the `'uchr'` resource to specify the output of a dead-key state.

Specifically, the dead-key state record—a structure of type  [`UCKeyStateRecord`](uckeystaterecord.md) —uses a `UCKeyCharSeq` value to contain the character output that results from the resolution of a given dead-key state. You can use a `UCKeyCharSeq` value in a dead-key state record to represent either an index to a Unicode character sequence or a single Unicode character. The `UCKeyCharSeq` type is similar to the type  [`UCKeyOutput`](uckeyoutput.md) , but does not itself support indices into dead-key state records.

The interpretation of `UCKeyCharSeq` depends on bits 15 and 14.

If they are 10 (that is, for values in the range of 0x8000–0xBFFF), then bits 0–13 are an index into the `charSequenceOffsets`[ field of a structure of type  [`UCKeySequenceDataIndex`](uckeysequencedataindex.md) , which contains offsets to a separate resource-wide list of Unicode character sequences. If a `UCKeySequenceDataIndex` structure is not present in the resource or the index is beyond the end of the list, then the entire value (that is, bits 0–15) is a single Unicode character to emit. Otherwise (for values in the range of 0x0000–0x7FFF and 0xC000–0xFFFD), bits 0–15 are a single Unicode character, with the exception that a value of 0xFFFE–0xFFFF means no character output (these are invalid Unicode codes). 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/uckeycharseq)*