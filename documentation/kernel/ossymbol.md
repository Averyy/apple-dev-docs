# OSSymbol

**Framework**: Kernel  
**Kind**: cl

OSSymbol wraps a C string in a unique C++ object for use as keys in Libkern collections.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class OSSymbol : OSString
```

#### Overview

OSSymbol is a container class for managing uniqued strings, for example, those used as dictionary keys. Its static instance-creation functions check for an existing instance of OSSymbol with the requested C string value before creating a new object. If an instance already exists in the pool of unique symbols, its reference count is incremented and the existing instance is returned.

While OSSymbol provides for uniquing of a given string value, it makes no effort to enforce immutability of that value. Altering the contents of an OSSymbol should be avoided.

With very few exceptions in the I/O Kit, all Libkern-based C++ classes, functions, and macros are  to use in a primary interrupt context. Consult the I/O Kit documentation related to primary interrupts for more information.

OSSymbol provides no concurrency protection; it's up to the usage context to provide any protection necessary. Some portions of the I/O Kit, such as IORegistryEntry, handle synchronization via defined member functions for setting properties.

## Topics

### Miscellaneous
- [free](ossymbol/1808021-free.md)
  Overrides OSObject::free to synchronize with the symbol pool.
- [initWithCString](ossymbol/1808026-initwithcstring.md)
  Overridden to prevent creation of duplicate symbols.
- [initWithCStringNoCopy](ossymbol/1808036-initwithcstringnocopy.md)
  Overridden to prevent creation of duplicate symbols.
- [initWithString](ossymbol/1808054-initwithstring.md)
  Overridden to prevent creation of duplicate symbols.
- [isEqualTo](ossymbol/1808078-isequalto.md)
  Tests the equality of an OSSymbol object to an arbitrary object.
- [isEqualTo(const char *)](ossymbol/1808093-isequalto.md)
  Tests the equality of an OSSymbol object with a C string.
- [isEqualTo(const OSSymbol *)](ossymbol/1808114-isequalto.md)
  Tests the equality of two OSSymbol objects.
- [taggedRelease(const void *)](ossymbol/1808137-taggedrelease.md)
  Overrides OSObject::taggedRelease(const void *) to synchronize with the symbol pool.
- [taggedRelease(const void *, const int)](ossymbol/1808154-taggedrelease.md)
  Overrides OSObject::taggedRelease(const void *, const int) to synchronize with the symbol pool.
- [withCString](ossymbol/1808171-withcstring.md)
  Returns an OSSymbol created from a C string, or the existing unique instance of the same value.
- [withCStringNoCopy](ossymbol/1808179-withcstringnocopy.md)
  Returns an OSSymbol created from a C string, without copying that string, or the existing unique instance of the same value.
- [withString](ossymbol/1808192-withstring.md)
  Returns an OSSymbol created from an OSString, or the existing unique instance of the same value.
### Instance Methods
- [- free](ossymbol/1399376-free.md)
- [- getMetaClass](ossymbol/1399366-getmetaclass.md)
- [- initWithCString](ossymbol/1399374-initwithcstring.md)
- [- initWithCStringNoCopy](ossymbol/1399383-initwithcstringnocopy.md)
- [- initWithString](ossymbol/1399368-initwithstring.md)
- [- isEqualTo](ossymbol/1399364-isequalto.md)
- [- isEqualTo](ossymbol/3516844-isequalto.md)
- [- isEqualTo](ossymbol/3516845-isequalto.md)
- [- taggedRelease](ossymbol/1399380-taggedrelease.md)
- [- taggedRelease](ossymbol/3516846-taggedrelease.md)
- [- taggedRetain](ossymbol/4143382-taggedretain.md)
### Type Methods
- [+ existingSymbolForCString](ossymbol/3143271-existingsymbolforcstring.md)
- [+ existingSymbolForString](ossymbol/3143272-existingsymbolforstring.md)
- [+ initialize](ossymbol/1399378-initialize.md)
- [+ withCString](ossymbol/1399370-withcstring.md)
- [+ withCStringNoCopy](ossymbol/1399385-withcstringnocopy.md)
- [+ withString](ossymbol/1399372-withstring.md)

## Relationships

### Inherits From
- [OSString](osstring.md)

## See Also

- [OSObject](osobject.md)
  OSObject is the concrete root class of the Libkern and I/O Kit C++ class hierarchy.
- [OSMetaClass](osmetaclass.md)
- [OSMetaClassBase](osmetaclassbase.md)
  OSMetaClassBase is the abstract bootstrap class for the Libkern and I/O Kit run-time type information system.
- [OSObjectPtr](osobjectptr.md)
- [OSObjectRef](osobjectref.md)
- [Additional Types](libkern/data_types/additional_types.md)
  Find custom type definitions and pointer types for standard classes. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ossymbol)*