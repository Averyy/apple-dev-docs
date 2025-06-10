# getTag

**Framework**: Kernel  
**Kind**: instm

Accessor to the retrieve the tag for the memory descriptor.

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOOptionBits getTag(void);
```

#### Return_value

The tag.

#### Discussion

This method returns the tag for the memory descriptor. Tag bits are not interpreted by IOMemoryDescriptor.

## See Also

- [getTag](iomemorydescriptor/1812815-gettag.md)
  Accessor to the retrieve the tag for the memory descriptor.
- [setTag](iomemorydescriptor/1812873-settag.md)
  Set the tag for the memory descriptor.
- [- setTag](iomemorydescriptor/1441787-settag.md)
  Set the tag for the memory descriptor.
- [- getVMTag](iomemorydescriptor/3131493-getvmtag.md)
- [- setVMTags](iomemorydescriptor/3131494-setvmtags.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/1442070-gettag)*