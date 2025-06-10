# OSCheckTypeInst

**Framework**: Kernel  
**Kind**: macro

Checks whether two objects are type-compatible.

**Availability**:
- macOS 10.12+

## Declaration

```swift
#define OSCheckTypeInst(typeinst, inst)
```

#### Return_value

`true` if both `inst` and `typeinst` are non-`NULL` and `inst` is derived from the class of `typeinst`; otherwise `false`.

## Parameters

- `typeinst`: The reference object.
- `inst`: The object to check for type compatibility.

## See Also

- [OSDynamicCast](osdynamiccast.md)
- [OSMemberFunctionCast](osmemberfunctioncast.md)
  Converts a C++ member function pointer, relative to an instance, to a C-style pointer to function.
- [OSSafeRelease](ossaferelease.md)
  Release an object if not `NULL`.
- [OSSafeReleaseNULL](ossafereleasenull.md)
- [OSTypeAlloc](ostypealloc.md)
- [OSTypeID](ostypeid.md)
- [OSTypeIDInst](ostypeidinst.md)
- [checkTypeInst](osmetaclassbase/1808042-checktypeinst.md)
  Checks whether an object instance is of the same class as another object instance (or a subclass of that class).
- [getMetaClass](osmetaclassbase/1808051-getmetaclass.md)
  Returns the OSMetaClass representing an OSMetaClassBase subclass.
- [getRetainCount](osmetaclassbase/1808060-getretaincount.md)
  Abstract declaration of getRetainCount().
- [isEqualTo](osmetaclassbase/1808069-isequalto.md)
  Checks whether another object is equal to the receiver.
- [metaCast(const char *)](osmetaclassbase/1808075-metacast.md)
  Casts this object is to the class managed by the named OSMetaClass.
- [metaCast(const OSMetaClass *)](osmetaclassbase/1808082-metacast.md)
  Casts this object is to the class managed by the given OSMetaClass.
- [metaCast(const OSString *)](osmetaclassbase/1808090-metacast.md)
  Casts this object is to the class managed by the named OSMetaClass.
- [metaCast(const OSSymbol *)](osmetaclassbase/1808095-metacast.md)
  Casts this object is to the class managed by the named OSMetaClass.
- [release()](osmetaclassbase/1808103-release.md)
  Abstract declaration of release.
- [release(int)](osmetaclassbase/1808109-release.md)
  Abstract declaration of release(int freeWhen).
- [retain](osmetaclassbase/1808117-retain.md)
  Abstract declaration of retain().
- [safeMetaCast](osmetaclassbase/1808126-safemetacast.md)
  Casts an object is to the class managed by the given OSMetaClass.
- [serialize](osmetaclassbase/1808135-serialize.md)
  Abstract declaration of serialize.
- [taggedRelease(const void *)](osmetaclassbase/1808142-taggedrelease.md)
  Abstract declaration of taggedRelease(const void *).
- [taggedRelease(const void *, const int)](osmetaclassbase/1808151-taggedrelease.md)
  Abstract declaration of taggedRelease(const void *, const int freeWhen).
- [taggedRetain](osmetaclassbase/1808161-taggedretain.md)
  Abstract declaration of taggedRetain(const void *).


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/oschecktypeinst)*