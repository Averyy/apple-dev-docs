# isTrue

**Framework**: Kernel  
**Kind**: instm

Checks whether the OSBoolean object represents a `true`` bool` value.

## Declaration

```swift
virtual bool isTrue() const;
```

#### Return_value

`true` if the OSBoolean object is `true`, `false` otherwise.

#### Overview

You can also use `==` against [`kOSBooleanTrue`](kosbooleantrue.md).

## See Also

- [free](osboolean/1808144-free.md)
  Overridden to prevent deallocation of the shared global instances.
- [getValue](osboolean/1808164-getvalue.md)
  Returns the C++ `bool` value for the OSBoolean object.
- [isEqualTo(const OSBoolean *)](osboolean/1808182-isequalto.md)
  Tests the equality of two OSBoolean objects.
- [isEqualTo(const OSMetaClassBase *)](osboolean/1808201-isequalto.md)
  Tests the equality an OSBoolean to an arbitrary object.
- [isFalse](osboolean/1808215-isfalse.md)
  Checks whether the OSBoolean object represents a `false`` bool` value.
- [serialize](osboolean/1808232-serialize.md)
  Archives the receiver into the provided OSSerialize object.
- [taggedRelease](osboolean/1808241-taggedrelease.md)
  Overrides the reference counting mechanism for the shared global instances.
- [taggedRetain](osboolean/1808247-taggedretain.md)
  Overrides the reference counting mechanism for the shared global instances.
- [withBoolean](osboolean/1808251-withboolean.md)
  Returns one of the global instances of OSBoolean.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osboolean/1808223-istrue)*