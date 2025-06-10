# setPurgeable

**Framework**: Kernel  
**Kind**: instm

Control the purgeable status of a memory descriptors memory.

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOReturn setPurgeable(IOOptionBits newState, IOOptionBits *oldState);
```

#### Return_value

An IOReturn code.

#### Discussion

Buffers may be allocated with the ability to have their purgeable status changed - IOBufferMemoryDescriptor with the kIOMemoryPurgeable option, VM_FLAGS_PURGEABLE may be passed to vm_allocate() in user space to allocate such buffers. The purgeable status of such a buffer may be controlled with setPurgeable(). The process of making a purgeable memory descriptor non-volatile and determining its previous state is atomic - if a purgeable memory descriptor is made nonvolatile and the old state is returned as kIOMemoryPurgeableVolatile, then the memory's previous contents are completely intact and will remain so until the memory is made volatile again. If the old state is returned as kIOMemoryPurgeableEmpty then the memory was reclaimed while it was in a volatile state and its previous contents have been lost.

## Parameters

- `newState`: kIOMemoryPurgeableEmpty - make the memory volatile, and discard any pages allocated to it.
- `oldState`: kIOMemoryPurgeableEmpty - the memory was volatile and has been discarded by the VM system.

## See Also

- [- setOwnership](iomemorydescriptor/3142952-setownership.md)
  Set the task that owns the descriptor’s memory. 
- [setPurgeable](iomemorydescriptor/1812865-setpurgeable.md)
  Control the purgeable status of a memory descriptors memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/1442065-setpurgeable)*