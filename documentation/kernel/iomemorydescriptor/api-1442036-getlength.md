# getLength

**Framework**: Kernel  
**Kind**: instm

Accessor to get the length of the memory descriptor (over all its ranges).

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOByteCount getLength(void);
```

#### Return_value

The byte count.

#### Discussion

This method returns the total length of the memory described by the descriptor, ie. the sum of its ranges' lengths.

## See Also

- [getDirection](iomemorydescriptor/1812765-getdirection.md)
  Gets the direction of memory transfers associated with the descriptor. 
- [- getDirection](iomemorydescriptor/1441925-getdirection.md)
  Gets the direction of memory transfers associated with the descriptor. 
- [getLength](iomemorydescriptor/1812776-getlength.md)
  Accessor to get the length of the memory descriptor (over all its ranges).
- [- GetLength](../driverkit/iomemorydescriptor/getlength.md)
  Returns the length of the memory block represented by this object.
- [- getDMAMapLength](iomemorydescriptor/3553361-getdmamaplength.md)
- [- getFlags](iomemorydescriptor/2870265-getflags.md)
  Returns the options used to create the memory descriptor.
- [- getMetaClass](iomemorydescriptor/1442096-getmetaclass.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/1442036-getlength)*