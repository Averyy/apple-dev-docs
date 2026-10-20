# operator new

**Framework**: Kernel  
**Kind**: instm

Allocates memory for an instance of the class.

## Declaration

```cpp
static void * operator new(
 size_tsize);
```

#### Return Value

A pointer to block of memory if available, `NULL` otherwise.

## Parameters

- `size`: The number of bytes to allocate

## See Also

### Miscellaneous
- [free](./api-1941146-free.md)
  Deallocates/releases resources held by the object.
- [getRetainCount](./api-1941147-getretaincount.md)
  Returns the reference count of the object.
- [init](./api-1941148-init.md)
  Initializes a newly-allocated object.
- [operator delete](./api-1941149-operator_delete.md)
  Frees the memory of the object itself.
- [release()](./api-1941151-release.md)
  Releases a reference to the object, freeing it immediately if the reference count drops to zero.
- [release(int)](./api-1941153-release.md)
  Releases a reference to an object, freeing it immediately if the reference count drops below the specified threshold.
- [retain](./api-1941154-retain.md)
  Retains a reference to the object.
- [serialize](./api-1941155-serialize.md)
  Overridden by subclasses to archive the receiver into the provided OSSerialize object.
- [taggedRelease(const void *)](./api-1941156-taggedrelease.md)
  Releases a tagged reference to an object, freeing it immediately if the reference count drops to zero.
- [taggedRelease(const void *, const int)](./api-1941157-taggedrelease.md)
  Releases a tagged reference to an object, freeing it immediately if the reference count drops below the specified threshold.
- [taggedRetain](./api-1941158-taggedretain.md)
  Retains a reference to the object with an optional tag used for reference-tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osobject/1941150-operator_new)*