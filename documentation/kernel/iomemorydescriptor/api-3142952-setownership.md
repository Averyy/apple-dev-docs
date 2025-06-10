# setOwnership

**Framework**: Kernel  
**Kind**: instm

Set the task that owns the descriptor’s memory. 

**Availability**:
- macOS 10.15+

## Declaration

```swift
IOReturn setOwnership(task_t newOwner, int newLedgerTag, IOOptionBits newLedgerOptions);
```

## See Also

- [setPurgeable](iomemorydescriptor/1812865-setpurgeable.md)
  Control the purgeable status of a memory descriptors memory.
- [- setPurgeable](iomemorydescriptor/1442065-setpurgeable.md)
  Control the purgeable status of a memory descriptors memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/3142952-setownership)*