# IOFreeContiguous

**Framework**: Kernel  
**Kind**: func

Deprecated - use IOBufferMemoryDescriptor. Frees memory allocated with IOMallocContiguous.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```swift
void IOFreeContiguous(void *address, vm_size_t size);
```

#### Discussion

This function frees memory allocated with IOMallocContiguous, it may block and so should not be called from interrupt level or while a simple lock is held.

## Parameters

- `address`: Virtual address of the allocated memory.
- `size`: Size of the memory allocated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1575295-iofreecontiguous)*