# isEqualTo(const OSBoolean *)

**Framework**: Kernel  
**Kind**: instm

Tests the equality of two OSBoolean objects.

## Declaration

```cpp
virtual bool isEqualTo(
 const OSBoolean *aBoolean) const;
```

#### Return Value

`true` if the OSBoolean objects are equal, `false` if not.

#### Overview

Two OSBoolean objects are considered equal if they are the same exact object (pointer equality).

## Parameters

- `aBoolean`: The OSBoolean to be compared against the receiver.

## See Also

### Miscellaneous
- [free](./api-1808144-free.md)
  Overridden to prevent deallocation of the shared global instances.
- [getValue](./api-1808164-getvalue.md)
  Returns the C++ `bool` value for the OSBoolean object.
- [isEqualTo(const OSMetaClassBase *)](./api-1808201-isequalto.md)
  Tests the equality an OSBoolean to an arbitrary object.
- [isFalse](./api-1808215-isfalse.md)
  Checks whether the OSBoolean object represents a `false`` bool` value.
- [isTrue](./api-1808223-istrue.md)
  Checks whether the OSBoolean object represents a `true`` bool` value.
- [serialize](./api-1808232-serialize.md)
  Archives the receiver into the provided OSSerialize object.
- [taggedRelease](./api-1808241-taggedrelease.md)
  Overrides the reference counting mechanism for the shared global instances.
- [taggedRetain](./api-1808247-taggedretain.md)
  Overrides the reference counting mechanism for the shared global instances.
- [withBoolean](./api-1808251-withboolean.md)
  Returns one of the global instances of OSBoolean.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osboolean/1808182-isequalto)*