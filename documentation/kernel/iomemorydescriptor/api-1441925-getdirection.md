# getDirection

**Framework**: Kernel  
**Kind**: instm

Gets the direction of memory transfers associated with the descriptor. 

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IODirection getDirection(void);
```

#### Return_value

The transfer direction. 

#### Discussion

This method returns the direction with which the memory descriptor was created.

## See Also

- [getDirection](iomemorydescriptor/1812765-getdirection.md)
  Gets the direction of memory transfers associated with the descriptor. 
- [getLength](iomemorydescriptor/1812776-getlength.md)
  Accessor to get the length of the memory descriptor (over all its ranges).
- [- getLength](iomemorydescriptor/1442036-getlength.md)
  Accessor to get the length of the memory descriptor (over all its ranges).
- [- GetLength](../driverkit/iomemorydescriptor/getlength.md)
  Returns the length of the memory block represented by this object.
- [- getDMAMapLength](iomemorydescriptor/3553361-getdmamaplength.md)
- [- getFlags](iomemorydescriptor/2870265-getflags.md)
  Returns the options used to create the memory descriptor.
- [- getMetaClass](iomemorydescriptor/1442096-getmetaclass.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/1441925-getdirection)*