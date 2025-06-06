# OSBoolean

**Framework**: Kernel  
**Kind**: cl

OSBoolean wraps a boolean value in a C++ object for use in Libkern collections.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class OSBoolean : OSObject
```

#### Overview

OSBoolean represents a boolean `true`/`false` value as a Libkern C++ object. There are only two instances of OSBoolean, [`kOSBooleanTrue`](kosbooleantrue.md) and [`kOSBooleanFalse`](kosbooleanfalse.md). These are shared globally and returned by the instance-creation function withBoolean. Thus, you can use pointer comparison to test whether two OSBoolean objects are equal.

## Topics

### Miscellaneous
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
- [isTrue](osboolean/1808223-istrue.md)
  Checks whether the OSBoolean object represents a `true`` bool` value.
- [serialize](osboolean/1808232-serialize.md)
  Archives the receiver into the provided OSSerialize object.
- [taggedRelease](osboolean/1808241-taggedrelease.md)
  Overrides the reference counting mechanism for the shared global instances.
- [taggedRetain](osboolean/1808247-taggedretain.md)
  Overrides the reference counting mechanism for the shared global instances.
- [withBoolean](osboolean/1808251-withboolean.md)
  Returns one of the global instances of OSBoolean.
### Instance Methods
- [- free](../driverkit/osboolean/free.md)
- [- getMetaClass](osboolean/1585812-getmetaclass.md)
- [- getValue](osboolean/1585816-getvalue.md)
- [- isEqualTo](osboolean/1585824-isequalto.md)
- [- isEqualTo](osboolean/3516832-isequalto.md)
- [- isFalse](osboolean/1585823-isfalse.md)
- [- isTrue](osboolean/1585819-istrue.md)
- [- serialize](osboolean/1585822-serialize.md)
- [- taggedRelease](osboolean/1585815-taggedrelease.md)
- [- taggedRetain](osboolean/1585818-taggedretain.md)
### Type Methods
- [+ initialize](osboolean/1585817-initialize.md)
- [+ withBoolean](osboolean/1585813-withboolean.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [OSString](osstring.md)
  OSString wraps a C string in a C++ object for use in Libkern collections.
- [OSNumber](osnumber.md)
  OSNumber wraps an integer value in a C++ object for use in Libkern collections.
- [OSData](osdata.md)
  OSData wraps an array of bytes in a C++ object for use in Libkern collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osboolean)*