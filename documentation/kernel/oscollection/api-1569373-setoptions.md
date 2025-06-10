# setOptions

**Framework**: Kernel  
**Kind**: instm

Recursively sets option bits in this collection and all child collections.

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

The only option currently in use is kImmutable.

Subclasses should override this function to recursively apply the options to their contents if the options actually change.

## Parameters

- `options`: A bitfield whose values turn the options on (1) or off (0).
- `mask`: A mask indicating which bits in   to change. Pass 0 to get the whole current options bitfield without changing any settings.
- `context`: Unused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/oscollection/1569373-setoptions)*