# OSMemberFunctionCast

**Framework**: Kernel  
**Kind**: macro

Converts a C++ member function pointer, relative to an instance, to a C-style pointer to function.

**Availability**:
- macOS 10.12+

## Declaration

```swift
#define OSMemberFunctionCast(cptrtype, self, func)
```

#### Return_value

A pointer to a function of the given type referencing `self`.

#### Discussion

This function is used to generate pointers to C++ functions for instances, such that they can be registered as callbacks with I/O Kit objects.

No warnings are generated.

This function will panic if an attempt is made to call it with a multiply-inheriting class.

## Parameters

- `cptrtype`: The function type declaration to cast to (typically provided as a   by I/O KitKit classes).
- `self`: The   pointer of the object whose function you wish to cache.
- `func`: The pointer to the member function itself, something like  .

## See Also

- [OSCheckTypeInst](oschecktypeinst.md)
  Checks whether two objects are type-compatible.
- [OSDynamicCast](osdynamiccast.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osmemberfunctioncast)*