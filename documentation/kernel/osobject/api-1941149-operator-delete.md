# operator delete

**Framework**: Kernel  
**Kind**: instm

Frees the memory of the object itself.

## Declaration

```swift
static void operator delete(
 void *mem,
 size_tsize);
```

#### Overview

Never use `delete` on objects derived from OSObject; use release instead.

## Parameters

- `mem`: A pointer to the object's memory.
- `size`: The size of the object's block of memory.

## See Also

- [free](osobject/1941146-free.md)
  Deallocates/releases resources held by the object.
- [getRetainCount](osobject/1941147-getretaincount.md)
  Returns the reference count of the object.
- [init](osobject/1941148-init.md)
  Initializes a newly-allocated object.
- [operator new](osobject/1941150-operator_new.md)
  Allocates memory for an instance of the class.
- [release()](osobject/1941151-release.md)
  Releases a reference to the object, freeing it immediately if the reference count drops to zero.
- [release(int)](osobject/1941153-release.md)
  Releases a reference to an object, freeing it immediately if the reference count drops below the specified threshold.
- [retain](osobject/1941154-retain.md)
  Retains a reference to the object.
- [serialize](osobject/1941155-serialize.md)
  Overridden by subclasses to archive the receiver into the provided OSSerialize object.
- [taggedRelease(const void *)](osobject/1941156-taggedrelease.md)
  Releases a tagged reference to an object, freeing it immediately if the reference count drops to zero.
- [taggedRelease(const void *, const int)](osobject/1941157-taggedrelease.md)
  Releases a tagged reference to an object, freeing it immediately if the reference count drops below the specified threshold.
- [taggedRetain](osobject/1941158-taggedretain.md)
  Retains a reference to the object with an optional tag used for reference-tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osobject/1941149-operator_delete)*