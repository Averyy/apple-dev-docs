# taggedRelease(const void *)

**Framework**: Kernel  
**Kind**: instm

Releases a tagged reference to an object, freeing it immediately if the reference count drops to zero.

## Declaration

```swift
virtual void taggedRelease(
 const void *tag = 0) const;
```

#### Overview

Kernel extensions should not use this function. It is for use by OSCollection and subclasses to track inclusion in collections.

## Parameters

- `tag`: Used for tracking collection references.

## See Also

- [free](osobject/1941146-free.md)
  Deallocates/releases resources held by the object.
- [getRetainCount](osobject/1941147-getretaincount.md)
  Returns the reference count of the object.
- [init](osobject/1941148-init.md)
  Initializes a newly-allocated object.
- [operator delete](osobject/1941149-operator_delete.md)
  Frees the memory of the object itself.
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
- [taggedRelease(const void *, const int)](osobject/1941157-taggedrelease.md)
  Releases a tagged reference to an object, freeing it immediately if the reference count drops below the specified threshold.
- [taggedRetain](osobject/1941158-taggedretain.md)
  Retains a reference to the object with an optional tag used for reference-tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osobject/1941156-taggedrelease)*