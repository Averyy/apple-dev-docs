# complete

**Framework**: Kernel  
**Kind**: instm

Complete processing of the memory after an I/O transfer finishes.

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOReturn complete(IODirection forDirection);
```

#### Return_value

An IOReturn code.

#### Discussion

This method should not be called unless a prepare was previously issued; the prepare() and complete() must occur in pairs, before and after an I/O transfer involving pageable memory. In 10.3 or greater systems the direction argument to complete is not longer respected. The direction is totally determined at prepare() time.

## Parameters

- `forDirection`: DEPRECATED The direction of the I/O just completed, or kIODirectionNone for the direction specified by the memory descriptor.

## See Also

- [prepare](iomemorydescriptor/1812845-prepare.md)
  Prepare the memory for an I/O transfer.
- [- prepare](iomemorydescriptor/1442024-prepare.md)
  Prepare the memory for an I/O transfer.
- [complete](iomemorydescriptor/1812740-complete.md)
  Complete processing of the memory after an I/O transfer finishes.
- [- getPreparationID](iomemorydescriptor/1441964-getpreparationid.md)
- [- setPreparationID](iomemorydescriptor/1442011-setpreparationid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/1442043-complete)*