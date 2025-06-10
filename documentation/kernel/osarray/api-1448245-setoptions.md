# setOptions

**Framework**: Kernel  
**Kind**: instm

Recursively sets option bits in an array and all child collections.

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual unsigned int setOptions(unsigned int options, unsigned int mask, void *context);
```

#### Return_value

The options bitfield as it was before the set operation.

#### Discussion

Kernel extensions should not call this function.

Child collections' options are changed only if the receiving array's options actually change.

## Parameters

- `options`: A bitfield whose values turn the options on (1) or off (0).
- `mask`: A mask indicating which bits in   to change. Pass 0 to get the whole current options bitfield without changing any settings.
- `context`: Unused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osarray/1448245-setoptions)*