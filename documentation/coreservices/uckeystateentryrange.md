# UCKeyStateEntryRange

**Framework**: Core Services  
**Kind**: struct

Maps from a dead-key state to either the resultant Unicode character(s) or the new dead key state produced when the current state is terminated by a given character key for a `'uchr'` resource.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct UCKeyStateEntryRange
```

#### Overview

The `UCKeyStateEntryRange` type is used in the `stateEntryData[]` field of a structure of type  [`UCKeyStateRecord`](uckeystaterecord.md). You should use the `UCKeyStateEntryRange` format for complex (multiple) dead-key states.

For each virtual key code, an entry in its dead-key state record maps from the current dead-key state to the Unicode character(s) produced or to the next dead-key state, as follows.

If the current dead-key state is within a valid dead-key state range for the given input character—that is, if its value is greater than or equal to `curStateStart` and less than or equal to `curStateStart + curStateRange`—then

- If the base `charData` value for the given dead-key state range is in the range of valid Unicode characters, a character is produced and the dead-key state may be terminated. 

and/or

- If the base `nextState` value is not 0, a new dead-key state is produced. 

In the first case, the output character is determined as follows: The base `charData` value is incremented by the resulting product of (the difference between the current state and the start of that state’s range) and (a multiplier). That is:

`charData += (curState - curStateStart) * deltaMultiplier `

Similarly, in the second case, the resulting dead-key state, which is the new `curState` value, is determined as follows: The base `nextState` value is incremented by the resulting product of (the difference between the current state and the start of that state’s range) and (a multiplier). That is:

`nextState += (curState - curStateStart) * deltaMultiplier `

## Topics

### Initializers
- [init()](uckeystateentryrange/1448909-init.md)
- [init(curStateStart: UInt16, curStateRange: UInt8, deltaMultiplier: UInt8, charData: UCKeyCharSeq, nextState: UInt16)](uckeystateentryrange/1446762-init.md)
### Instance Properties
- [var charData: UCKeyCharSeq](uckeystateentryrange/1390454-chardata.md)
  A value of type `UCKeyCharSeq`. This base character value is used to determine the actual Unicode character(s) produced when a given dead-key state terminates. 
- [var curStateRange: UInt8](uckeystateentryrange/1390515-curstaterange.md)
  An unsigned 8-bit integer specifying the number of entries in a given dead-key state range.
- [var curStateStart: UInt16](uckeystateentryrange/1390496-curstatestart.md)
  An unsigned 16-bit integer specifying the beginning of a given dead-key state range.
- [var deltaMultiplier: UInt8](uckeystateentryrange/1390570-deltamultiplier.md)
  An unsigned 8-bit integer.
- [var nextState: UInt16](uckeystateentryrange/1390484-nextstate.md)
  An unsigned 16-bit integer. This base dead-key state value is used to determine the following dead-key state, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/uckeystateentryrange)*