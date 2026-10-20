# taggedRelease(const void *)

**Framework**: Kernel  
**Kind**: instm

Releases a tagged reference to an object, freeing it immediately if the reference count drops to zero.

## Declaration

```cpp
virtual void taggedRelease(
 const void *tag = 0) const;
```

#### Overview

Kernel extensions should not use this function. It is for use by OSCollection and subclasses to track inclusion in collections.

## Parameters

- `tag`: Used for tracking collection references.

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
- [operator new](./api-1941150-operator_new.md)
  Allocates memory for an instance of the class.
- [release()](./api-1941151-release.md)
  Releases a reference to the object, freeing it immediately if the reference count drops to zero.
- [release(int)](./api-1941153-release.md)
  Releases a reference to an object, freeing it immediately if the reference count drops below the specified threshold.
- [retain](./api-1941154-retain.md)
  Retains a reference to the object.
- [serialize](./api-1941155-serialize.md)
  Overridden by subclasses to archive the receiver into the provided OSSerialize object.
- [taggedRelease(const void *, const int)](./api-1941157-taggedrelease.md)
  Releases a tagged reference to an object, freeing it immediately if the reference count drops below the specified threshold.
- [taggedRetain](./api-1941158-taggedretain.md)
  Retains a reference to the object with an optional tag used for reference-tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osobject/1941156-taggedrelease)*