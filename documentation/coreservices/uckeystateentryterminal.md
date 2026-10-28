# UCKeyStateEntryTerminal

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

Maps from a dead-key state to the Unicode character(s) produced when that state is terminated by a given character key for a `'uchr'` resource.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct UCKeyStateEntryTerminal
```

```c
typedef struct UCKeyStateEntryTerminal {
    ...
} UCKeyStateEntryTerminal;
```

## Overview

The `UCKeyStateEntryTerminal` type is used in the `stateEntryData[]` field of a structure of type  [`UCKeyStateRecord`](./uckeystaterecord.md). You should use the `UCKeyStateEntryTerminal` format for simple dead-key states that are terminated by a single keystroke, as in the U.S. keyboard layout. Each entry maps from the current dead-key state to the Unicode character(s) produced when a given character key is pressed that terminates the dead-key state. 

## Topics

### Initializers
- [init()](./uckeystateentryterminal/api-1443469-init.md)
- [init(curState: UInt16, charData: UCKeyCharSeq)](./uckeystateentryterminal/api-1446872-init.md)
### Instance Properties
- [var charData: UCKeyCharSeq](./uckeystateentryterminal/api-1390590-chardata.md)
  A value of type `UCKeyCharSeq` specifying the Unicode character(s) produced when a given character key is pressed. 
- [var curState: UInt16](./uckeystateentryterminal/api-1390480-curstate.md)
  An unsigned 16-bit integer specifying the current dead-key state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/uckeystateentryterminal)*