# OSObject

**Framework**: Kernel  
**Kind**: cl

OSObject is the concrete root class of the Libkern and I/O Kit C++ class hierarchy.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class OSObject : OSMetaClassBase
```

#### Overview

OSObject defines the minimal functionality required of Libkern and I/O Kit C++ classes: tie-in to the run-time type information facility, the dynamic allocation/initialization paradigm, and reference counting. While kernel extensions are free to use their own C++ classes internally, any interaction they have with Libkern or the I/O Kit will require classes ultimately derived from OSObject.

OSObject is derived from the abstract root class OSMetaClassBase, which declares (and defines many of) the primitives on which the run-time type information facility is based. A parallel inheritance hierarchy of metaclass objects provides run-time introspection, including access to class names, inheritance, and safe type-casting. See OSMetaClass for more information.

The kernel-resident C++ runtime does not support exceptions, so Libkern classes cannot use standard C++ object constructors and destructors, which use exceptions to report errors. To support error-handling during instance creation, then, OSObject separates object allocation from initialization. You can create a new OSObject-derived instance with the `new` operator, but this does nothing more than allocate memory and initialize the reference count to 1. Following this, you must call a designated initialization function and check its `bool` return value. If the initialization fails, you must immediately call release on the instance and handle the failure in whatever way is appropriate. Many Libkern and I/O Kit classes define static instance-creation functions (beginning with the word "with") to make construction a one-step process for clients.

OSObject provides reference counting services using the retain, release(), release(int freeWhen) and free functions. The public interface to the reference counting is retain, and release; release(int freeWhen) is provided for objects that have internal retain cycles.

In general, a subclass is expected to only override free. It may also choose to override release(int freeWhen) if the object has a circular retain count, as noted above.

With very few exceptions in the I/O Kit, all Libkern-based C++ classes, functions, and macros are  to use in a primary interrupt context. Consult the I/O Kit documentation related to primary interrupts for more information.

The basic features of OSObject are thread-safe. Most Libkern subclasses are not, and require locking or other protection if instances are shared between threads. I/O Kit driver objects are either designed for use within thread-safe contexts or designed to inherently be thread-safe. Always check the individual class documentation to see what steps are necessary for concurrent use of instances.

## Topics

### Miscellaneous
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
- [taggedRelease(const void *)](osobject/1941156-taggedrelease.md)
  Releases a tagged reference to an object, freeing it immediately if the reference count drops to zero.
- [taggedRelease(const void *, const int)](osobject/1941157-taggedrelease.md)
  Releases a tagged reference to an object, freeing it immediately if the reference count drops below the specified threshold.
- [taggedRetain](osobject/1941158-taggedretain.md)
  Retains a reference to the object with an optional tag used for reference-tracking.
### Instance Methods
- [- CopyDispatchQueue](../driverkit/osobject/copydispatchqueue.md)
- [- Dispatch](osobject/3180941-dispatch.md)
- [- SetDispatchQueue](../driverkit/osobject/setdispatchqueue.md)
- [- free](../driverkit/osobject/free.md)
- [- getMetaClass](osobject/1546718-getmetaclass.md)
- [- getRetainCount](osobject/1546715-getretaincount.md)
- [- init](../driverkit/osobject/init.md)
- [- release](osobject/1546709-release.md)
- [- release](../driverkit/osobject/release.md)
  Releases the OSObject instance
- [- retain](../driverkit/osobject/retain.md)
  Retains the OSObject instance
- [- serialize](osobject/1546714-serialize.md)
- [- taggedRelease](osobject/1546712-taggedrelease.md)
- [- taggedRelease](osobject/3516839-taggedrelease.md)
- [- taggedRetain](osobject/1546708-taggedretain.md)
### Type Methods
- [+ CopyDispatchQueue_Invoke](osobject/3075311-copydispatchqueue_invoke.md)
- [+ SetDispatchQueue_Invoke](osobject/3075323-setdispatchqueue_invoke.md)

## Relationships

### Inherits From
- [OSMetaClassBase](osmetaclassbase.md)

## See Also

- [OSSymbol](ossymbol.md)
  OSSymbol wraps a C string in a unique C++ object for use as keys in Libkern collections.
- [OSMetaClass](osmetaclass.md)
- [OSMetaClassBase](osmetaclassbase.md)
  OSMetaClassBase is the abstract bootstrap class for the Libkern and I/O Kit run-time type information system.
- [OSObjectPtr](osobjectptr.md)
- [OSObjectRef](osobjectref.md)
- [Additional Types](libkern/data_types/additional_types.md)
  Find custom type definitions and pointer types for standard classes. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osobject)*