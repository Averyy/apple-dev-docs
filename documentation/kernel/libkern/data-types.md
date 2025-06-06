# Data Types

**Framework**: Kernel

Create strings, numbers, collections, data objects, and the other standard types employed by drivers and kernel extensions.

## Topics

### Simple Types
- [OSBoolean](osboolean.md)
  OSBoolean wraps a boolean value in a C++ object for use in Libkern collections.
- [OSString](osstring.md)
  OSString wraps a C string in a C++ object for use in Libkern collections.
- [OSNumber](osnumber.md)
  OSNumber wraps an integer value in a C++ object for use in Libkern collections.
- [OSData](osdata.md)
  OSData wraps an array of bytes in a C++ object for use in Libkern collections.
### Collections
- [OSArray](osarray.md)
  OSArray provides an indexed store of objects.
- [OSDictionary](osdictionary.md)
  OSDictionary provides an associative store using strings for keys.
- [OSSet](osset.md)
  OSSet provides an unordered set store of objects.
- [OSOrderedSet](osorderedset.md)
  OSOrderedSet provides an ordered set store of objects.
- [OSCollection](oscollection.md)
  The abstract superclass for Libkern collections.
- [OSCollectionIterator](oscollectioniterator.md)
- [OSIterator](ositerator.md)
  The abstract superclass for Libkern iterators.
### Signed Integers
- [LittleSInt16](littlesint16.md)
- [LittleSInt32](littlesint32.md)
- [LittleSInt64](littlesint64.md)
- [BigSInt16](bigsint16.md)
- [BigSInt32](bigsint32.md)
- [BigSInt64](bigsint64.md)
### Unsigned Integers
- [LittleUInt16](littleuint16.md)
- [LittleUInt32](littleuint32.md)
- [LittleUInt64](littleuint64.md)
- [BigUInt16](biguint16.md)
- [BigUInt32](biguint32.md)
- [BigUInt64](biguint64.md)
- [U128](u128.md)
### Actions
- [OSAction](osaction.md)
- [OSActionInterface](osactioninterface.md)
### Callback Methods
- [OSActionAbortedHandler](osactionabortedhandler.md)
- [OSActionCancelHandler](osactioncancelhandler.md)
- [OSDispatchMethod](osdispatchmethod.md)
- [OSKextRequestResourceCallback](oskextrequestresourcecallback.md)
  Invoked to provide results for a kext resource request.
- [OSObjectApplierFunction](osobjectapplierfunction.md)
- [OSSerializerBlock](osserializerblock.md)
- [OSSerializerCallback](osserializercallback.md)
### Serialization
- [OSSerialize](osserialize.md)
  OSSerialize coordinates serialization of Libkern C++ objects into an XML stream.
- [OSSerializer](osserializer.md)
### Base Types
- [OSSymbol](ossymbol.md)
  OSSymbol wraps a C string in a unique C++ object for use as keys in Libkern collections.
- [OSObject](osobject.md)
  OSObject is the concrete root class of the Libkern and I/O Kit C++ class hierarchy.
- [OSMetaClass](osmetaclass.md)
- [OSMetaClassBase](osmetaclassbase.md)
  OSMetaClassBase is the abstract bootstrap class for the Libkern and I/O Kit run-time type information system.
- [OSObjectPtr](osobjectptr.md)
- [OSObjectRef](osobjectref.md)
- [Additional Types](libkern/data_types/additional_types.md)
  Find custom type definitions and pointer types for standard classes. 

## See Also

- [Memory](iokit_fundamentals/memory.md)
  Allocate, map, free, and manage memory in the kernel. 
- [Workflow and Control](iokit_fundamentals/workflow_and_control.md)
- [Locks](iokit_fundamentals/locks.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/libkern/data_types)*