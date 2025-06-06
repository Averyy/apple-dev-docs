# UCKeyModifiersToTableNum

**Framework**: Core Services  
**Kind**: struct

Maps a modifier key combination to a particular key-code-to-character table number in a `'uchr'` resource.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct UCKeyModifiersToTableNum
```

#### Overview

The Unicode keyboard-layout (`'uchr'`) resource contains the data necessary to map virtual key codes to Unicode character codes for a given keyboard layout. The `'uchr'` format consists of a header information section and five key mapping data sections. The `UCKeyModifiersToTableNum` type is used in the first key mapping section of the `'uchr'` resource. It maps a modifier key combination to a particular key-code-to-character table number. 

## Topics

### Initializers
- [init()](uckeymodifierstotablenum/1443345-init.md)
- [init(keyModifiersToTableNumFormat: UInt16, defaultTableNum: UInt16, modifiersCount: UInt32, tableNum: UInt8)](uckeymodifierstotablenum/1444613-init.md)
### Instance Properties
- [var defaultTableNum: UInt16](uckeymodifierstotablenum/1390542-defaulttablenum.md)
  An unsigned 16-bit integer identifying the table number to use for modifier combinations that are outside of the range included in the `tableNum` field.
- [var keyModifiersToTableNumFormat: UInt16](uckeymodifierstotablenum/1390556-keymodifierstotablenumformat.md)
  An unsigned 16-bit integer identifying the format of the `UCKeyModifiersToTableNum` structure. Set to `kUCKeyModifiersToTableNumFormat`.
- [var modifiersCount: UInt32](uckeymodifierstotablenum/1390509-modifierscount.md)
  An unsigned 32-bit integer specifying the range of modifier bit combinations for which there are entries in the `tableNum[]` field.
- [var tableNum: UInt8](uckeymodifierstotablenum/1390564-tablenum.md)
  An array of unsigned 8-bit integers that map modifier bit combinations to table numbers. These values are indexes into the `keyToCharTableOffsets` array in a [`UCKeyToCharTableIndex`](uckeytochartableindex.md)structure; these, in turn, are offsets to the actual key-code-to character tables, which follow the `UCKeyToCharTableIndex` structure in the `'uchr'` resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/uckeymodifierstotablenum)*