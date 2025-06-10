# prepare

**Framework**: Kernel  
**Kind**: instm

Prepare the memory for an I/O transfer.

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOReturn prepare(IODirection forDirection);
```

#### Return_value

An IOReturn code.

#### Discussion

This involves paging in the memory, if necessary, and wiring it down for the duration of the transfer. The complete() method completes the processing of the memory after the I/O transfer finishes. Note that the prepare call is not thread safe and it is expected that the client will more easily be able to guarantee single threading a particular memory descriptor.

## Parameters

- `forDirection`: The direction of the I/O just completed, or kIODirectionNone for the direction specified by the memory descriptor.

## See Also

- [prepare](iomemorydescriptor/1812845-prepare.md)
  Prepare the memory for an I/O transfer.
- [complete](iomemorydescriptor/1812740-complete.md)
  Complete processing of the memory after an I/O transfer finishes.
- [- complete](iomemorydescriptor/1442043-complete.md)
  Complete processing of the memory after an I/O transfer finishes.
- [- getPreparationID](iomemorydescriptor/1441964-getpreparationid.md)
- [- setPreparationID](iomemorydescriptor/1442011-setpreparationid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/1442024-prepare)*