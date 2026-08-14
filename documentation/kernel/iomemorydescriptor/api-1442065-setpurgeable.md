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

- `newState`: - the desired new purgeable state of the memory: kIOMemoryPurgeableKeepCurrent - make no changes to the memory's purgeable state. kIOMemoryPurgeableVolatile - make the memory volatile - the memory may be reclaimed by the VM system without saving its contents to backing store. kIOMemoryPurgeableNonVolatile - make the memory nonvolatile - the memory is treated as with usual allocations and must be saved to backing store if paged. kIOMemoryPurgeableEmpty - make the memory volatile, and discard any pages allocated to it.
- `oldState`: - if non-NULL, the previous purgeable state of the memory is returned here: kIOMemoryPurgeableNonVolatile - the memory was nonvolatile. kIOMemoryPurgeableVolatile - the memory was volatile but its content has not been discarded by the VM system. kIOMemoryPurgeableEmpty - the memory was volatile and has been discarded by the VM system.

## See Also

- [- setOwnership](iomemorydescriptor/3142952-setownership.md)
  Set the task that owns the descriptor’s memory. 
- [setPurgeable](iomemorydescriptor/1812865-setpurgeable.md)
  Control the purgeable status of a memory descriptors memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/1442065-setpurgeable)*