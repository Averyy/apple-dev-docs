# UCKeyStateTerminators

**Framework**: Core Services  
**Kind**: struct

Lists the default terminators for each dead-key state handled by a `'uchr'` resource.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct UCKeyStateTerminators
```

#### Overview

The Unicode keyboard-layout ( `'uchr'`) resource contains the data necessary to map virtual key codes to Unicode character codes for a given keyboard layout. The `'uchr'` format consists of a header information section and five key mapping data sections. The `UCKeyStateTerminators` type is used in the fourth key mapping section of the `'uchr ` ' resource. 

The `UCKeyStateTerminators` structure contains the list of default terminators (characters or sequences) for each dead-key state that is handled by a `'uchr'` resource. When a dead-key state is in effect but a modifier-and-key combination is typed which has no special handling for that state, the default terminator for the state is output before the modifier-and-key combination is processed. If this table is not present or does not extend far enough to have a terminator for the state, nothing is output when the state terminates. 

## Topics

### Initializers
- [init()](uckeystateterminators/1448249-init.md)
- [init(keyStateTerminatorsFormat: UInt16, keyStateTerminatorCount: UInt16, keyStateTerminators: UCKeyCharSeq)](uckeystateterminators/1443209-init.md)
### Instance Properties
- [var keyStateTerminatorCount: UInt16](uckeystateterminators/1390511-keystateterminatorcount.md)
  An unsigned 16-bit integer specifying the number of default dead-key state terminators contained in the `keyStateTerminators[]` array.
- [var keyStateTerminators: UCKeyCharSeq](uckeystateterminators/1390409-keystateterminators.md)
  An array of default dead-key state terminators, described as values of type [`UCKeyCharSeq`](uckeycharseq.md); the value `keyStateTerminators[0]` is the terminator for state 1, and so on. 
- [var keyStateTerminatorsFormat: UInt16](uckeystateterminators/1390431-keystateterminatorsformat.md)
  An unsigned 16-bit integer identifying the format of the `UCKeyStateTerminators` structure. Set to `kUCKeyStateTerminatorsFormat`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/uckeystateterminators)*