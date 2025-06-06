# UCKeyToCharTableIndex

**Framework**: Core Services  
**Kind**: struct

Provides a count of, and offsets to, key-code-to-character tables in a `'uchr'` resource.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct UCKeyToCharTableIndex
```

#### Overview

The Unicode keyboard-layout (`'uchr'`) resource contains the data necessary to map virtual key codes to Unicode character codes for a given keyboard layout. The `'uchr'` format consists of a header information section and five key mapping data sections. The `UCKeyToCharTableIndex` type is used in the second key mapping section of the `'uchr'` resource. The `UCKeyToCharTableIndex` structure precedes the list of key-code-to-character tables, each of which maps a key code to a 16-bit value of type  [`UCKeyOutput`](uckeyoutput.md). 

## Topics

### Initializers
- [init()](uckeytochartableindex/1444832-init.md)
- [init(keyToCharTableIndexFormat: UInt16, keyToCharTableSize: UInt16, keyToCharTableCount: UInt32, keyToCharTableOffsets: UInt32)](uckeytochartableindex/1450385-init.md)
### Instance Properties
- [var keyToCharTableCount: UInt32](uckeytochartableindex/1390611-keytochartablecount.md)
  An unsigned 32-bit integer specifying the number of key-code-to-character tables, typically 6 to 12.
- [var keyToCharTableIndexFormat: UInt16](uckeytochartableindex/1390562-keytochartableindexformat.md)
  An unsigned 16-bit integer identifying the format of the `UCKeyToCharTableIndex` structure. Set to `kUCKeyToCharTableIndexFormat`.
- [var keyToCharTableOffsets: UInt32](uckeytochartableindex/1390388-keytochartableoffsets.md)
  An array of offsets from the beginning of the `'uchr'` resource to each of the `UCKeyOutput` key-code-to-character tables in the `keyToCharData[]` array that follows this structure in the resource.
- [var keyToCharTableSize: UInt16](uckeytochartableindex/1390382-keytochartablesize.md)
  An unsigned 16-bit integer specifying the number of virtual key codes supported by this resource; for ADB keyboards this is 128 (with virtual key codes ranging from 0 to 127).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/uckeytochartableindex)*