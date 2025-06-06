# OSMetaClassBase

**Framework**: Kernel  
**Kind**: cl

OSMetaClassBase is the abstract bootstrap class for the Libkern and I/O Kit run-time type information system.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class OSMetaClassBase
```

#### Overview

OSMetaClassBase is the abstract C++ root class underlying the entire Libkern and I/O Kit class hierarchy. It defines the run-time type information system, including dynamic class allocation and safe type-casting, as well as the abstract interface for reference counting and a few other utility functions. OSMetaClassBase is the immediate superclass of OSObject and OSMetaClass; no other class should derive from OSMetaClassBase.

For more information, see [`Introduction to I/O Kit Device Driver Design Guidelines`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingDeviceDriver/Introduction/Intro.html#//apple_ref/doc/uid/TP40002799).

Kernel Extensions should never interact directly with OSMetaClassBase, but they will find useful several macros that tie in to the run-time type information system, specifically:

- OSTypeAlloc - allocation of new instances
- OSDynamicCast - safe type casting
- OSCheckTypeInst - checking for inheritance/derivation
- OSMemberFunctionCast - casting C++ member functions to C function pointers for registration as callbacks

See OSMetaClass for more run-time type information interfaces.

OSMetaClassBase should not be subclassed by kernel extensions, nor should kernel extensions call its run-time type functions directly.

The run-time type functions and macros are  to call in a primary interrupt context.

The run-time type macros and functions of OSMetaClassBase are thread-safe.

## Topics

### Miscellaneous
- [OSCheckTypeInst](oschecktypeinst.md)
  Checks whether two objects are type-compatible.
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
### Instance Methods
- [- Dispatch](osmetaclassbase/3181053-dispatch.md)
  Runtime internals
- [- Invoke](osmetaclassbase/3181056-invoke.md)
  Runtime internals
- [- getMetaClass](osmetaclassbase/1452550-getmetaclass.md)
- [- getRetainCount](osmetaclassbase/1452539-getretaincount.md)
- [- isEqualTo](osmetaclassbase/1452440-isequalto.md)
- [- metaCast](osmetaclassbase/1452513-metacast.md)
- [- metaCast](osmetaclassbase/3437951-metacast.md)
- [- metaCast](osmetaclassbase/3437952-metacast.md)
- [- metaCast](osmetaclassbase/3437953-metacast.md)
- [- operator=](osmetaclassbase/1452581-operator.md)
- [- release](osmetaclassbase/1452460-release.md)
- [- release](osmetaclassbase/3438210-release.md)
- [- retain](osmetaclassbase/1452494-retain.md)
- [- serialize](osmetaclassbase/1452438-serialize.md)
- [- taggedRelease](osmetaclassbase/1452437-taggedrelease.md)
- [- taggedRelease](osmetaclassbase/3437954-taggedrelease.md)
- [- taggedRetain](osmetaclassbase/1452446-taggedretain.md)
### Type Methods
- [+ checkTypeInst](osmetaclassbase/1452569-checktypeinst.md)
- [+ initialize](osmetaclassbase/1452472-initialize.md)
- [+ requiredMetaCast](osmetaclassbase/3181821-requiredmetacast.md)
- [+ safeMetaCast](osmetaclassbase/1452515-safemetacast.md)

## See Also

- [OSSymbol](ossymbol.md)
  OSSymbol wraps a C string in a unique C++ object for use as keys in Libkern collections.
- [OSObject](osobject.md)
  OSObject is the concrete root class of the Libkern and I/O Kit C++ class hierarchy.
- [OSMetaClass](osmetaclass.md)
- [OSObjectPtr](osobjectptr.md)
- [OSObjectRef](osobjectref.md)
- [Additional Types](libkern/data_types/additional_types.md)
  Find custom type definitions and pointer types for standard classes. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osmetaclassbase)*