# OSDictionary

**Framework**: Kernel  
**Kind**: cl

OSDictionary provides an associative store using strings for keys.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class OSDictionary : OSCollection
```

#### Overview

OSDictionary is a container for Libkern C++ objects (those derived from OSMetaClassBase, in particular OSObject). Storage and access are associative, based on string-valued keys (C string, `OSString`, or [`OSSymbol`](ossymbol.md)). When adding an object to an OSDictionary, you provide a string identifier, which can then used to retrieve that object or remove it from the dictionary. Setting an object with a key that already has an associated object replaces the original object.

You must generally cast retrieved objects from [`OSObject`](osobject.md) to the desired class using OSDynamicCast. This macro returns the object cast to the desired class, or `NULL` if the object isn't derived from that class.

When iterating an OSDictionary using OSCollectionIterator, the objects returned from getNextObject are dictionary keys (not the object values for those keys). You can use the keys to retrieve their associated object values.

As with all Libkern collection classes, OSDictionary retains keys and objects added to it, and releases keys and objects removed from it (or replaced). An OSDictionary also grows as necessary to accommodate new key/value pairs,  Core Foundation collections (it does not, however, shrink).

 OSDictionary currently uses a linear search algorithm, and is not designed for high-performance access of many values. It is intended as a simple associative-storage mechanism only.

With very few exceptions in the I/O Kit, all Libkern-based C++ classes, functions, and macros are  to use in a primary interrupt context. Consult the I/O Kit documentation related to primary interrupts for more information.

OSDictionary provides no concurrency protection; it's up to the usage context to provide any protection necessary. Some portions of the I/O Kit, such as IORegistryEntry, handle synchronization via defined member functions for setting properties.

## Topics

### Miscellaneous
- [copyCollection](osdictionary/1808081-copycollection.md)
  Creates a deep copy of the dictionary and its child collections.
- [ensureCapacity](osdictionary/1808087-ensurecapacity.md)
  Ensures the dictionary has enough space to store the requested number of key/object pairs.
- [flushCollection](osdictionary/1808092-flushcollection.md)
  Removes and releases all keys and objects within the dictionary.
- [free](osdictionary/1808101-free.md)
  Deallocates or releases any resources used by the OSDictionary instance.
- [getCapacity](osdictionary/1808107-getcapacity.md)
  Returns the number of objects the dictionary can store without reallocating.
- [getCapacityIncrement](osdictionary/1808116-getcapacityincrement.md)
  Returns the storage increment of the dictionary.
- [getCount](osdictionary/1808124-getcount.md)
  Returns the current number of key/object pairs contained within the dictionary.
- [getObject](osdictionary/1808133-getobject.md)
  Returns the object stored under a given key.
- [getObject(const OSString *)](osdictionary/1808139-getobject.md)
  Returns the object stored under a given key.
- [getObject(const OSSymbol *)](osdictionary/1808148-getobject.md)
  Returns the object stored under a given key.
- [initWithCapacity](osdictionary/1808159-initwithcapacity.md)
  Initializes a new instance of OSDictionary.
- [initWithDictionary](osdictionary/1808166-initwithdictionary.md)
  Initializes a new OSDictionary with the contents of another dictionary.
- [initWithObjects(const OSObject *, const OSString *, unsigned int, unsigned int)](osdictionary/1808177-initwithobjects.md)
  Initializes a new OSDictionary with keys and objects provided.
- [initWithObjects(const OSObject *, const OSSymbol *, unsigned int, unsigned int)](osdictionary/1808181-initwithobjects.md)
  Initializes a new OSDictionary with keys and objects provided.
- [isEqualTo](osdictionary/1808187-isequalto.md)
  Tests the equality of an OSDictionary to an arbitrary object.
- [isEqualTo(const OSDictionary *)](osdictionary/1808191-isequalto.md)
  Tests the equality of two OSDictionary objects.
- [isEqualTo(const OSDictionary *, const OSCollection *)](osdictionary/1808194-isequalto.md)
  Tests the equality of two OSDictionary objects over a subset of keys.
- [merge](osdictionary/1808198-merge.md)
  Merges the contents of a dictionary into the receiver.
- [removeObject](osdictionary/1808205-removeobject.md)
  Removes a key/object pair from the dictionary.
- [removeObject(const OSString *)](osdictionary/1808207-removeobject.md)
  Removes a key/object pair from the dictionary.
- [removeObject(const OSSymbol *)](osdictionary/1808209-removeobject.md)
  Removes a key/object pair from the dictionary.
- [serialize](osdictionary/1808214-serialize.md)
  Archives the receiver into the provided OSSerialize object.
- [setCapacityIncrement](osdictionary/1808218-setcapacityincrement.md)
  Sets the storage increment of the dictionary.
- [setObject](osdictionary/1808220-setobject.md)
  Stores an object in the dictionary under a key.
- [setObject(const OSString *, const OSMetaClassBase *)](osdictionary/1808224-setobject.md)
  Stores an object in the dictionary under a key.
- [setObject(const OSSymbol *, const OSMetaClassBase *)](osdictionary/1808227-setobject.md)
  Stores an object in the dictionary under a key.
- [withCapacity](osdictionary/1808230-withcapacity.md)
  Creates and initializes an empty OSDictionary.
- [withDictionary](osdictionary/1808234-withdictionary.md)
  Creates and initializes an OSDictionary populated with the contents of another dictionary.
- [withObjects(const OSObject *, const OSString *, unsigned int, unsigned int)](osdictionary/1808237-withobjects.md)
  Creates and initializes an OSDictionary populated with keys and objects provided.
- [withObjects(const OSObject *, const OSSymbol *, unsigned int, unsigned int)](osdictionary/1808240-withobjects.md)
  Creates and initializes an OSDictionary populated with keys and objects provided.
### Instance Methods
- [- copyCollection](osdictionary/1412868-copycollection.md)
- [- ensureCapacity](../driverkit/osdictionary/ensurecapacity.md)
  Allocates capacity for members in dictionary.
- [- flushCollection](../driverkit/osdictionary/flushcollection.md)
  Removes and drops references to all members of dictionary.
- [- free](../driverkit/osdictionary/free.md)
- [- getCapacity](../driverkit/osdictionary/getcapacity.md)
  Returns count of currently allocated capacity for members in dictionary.
- [- getCapacityIncrement](osdictionary/1412877-getcapacityincrement.md)
- [- getCount](../driverkit/osdictionary/getcount.md)
  Returns count of members in dictionary.
- [- getMetaClass](osdictionary/1412876-getmetaclass.md)
- [- getNextObjectForIterator](osdictionary/1412886-getnextobjectforiterator.md)
- [- getObject](osdictionary/1412897-getobject.md)
- [- getObject](../driverkit/osdictionary/getobject-9ikoz.md)
  Returns a member of the dictionary.
- [- getObject](../driverkit/osdictionary/getobject-8k3ie.md)
  Returns a member of the dictionary.
- [- initIterator](osdictionary/1412888-inititerator.md)
- [- initWithCapacity](osdictionary/1412883-initwithcapacity.md)
- [- initWithDictionary](osdictionary/1412866-initwithdictionary.md)
- [- initWithObjects](osdictionary/1412860-initwithobjects.md)
- [- initWithObjects](osdictionary/3516835-initwithobjects.md)
- [- isEqualTo](../driverkit/osdictionary/isequalto-2p9or.md)
  Compares certain members of two dictionaries with isEqualTo().
- [- isEqualTo](../driverkit/osdictionary/isequalto-3c1k0.md)
  Compares all members of two dictionaries with isEqualTo().
- [- isEqualTo](../driverkit/osdictionary/isequalto-3kuk7.md)
  Compares the dictionary with an OSObject
- [- iterateObjects](osdictionary/2967352-iterateobjects.md)
- [- iterateObjects](osdictionary/3516836-iterateobjects.md)
- [- iteratorSize](osdictionary/1412862-iteratorsize.md)
- [- merge](../driverkit/osdictionary/merge.md)
  Adds all members of a dictionary to this dictionary.
- [- removeObject](osdictionary/1412855-removeobject.md)
- [- removeObject](../driverkit/osdictionary/removeobject-25qm5.md)
  Remove an object by key from the dictionary.
- [- removeObject](../driverkit/osdictionary/removeobject-156jh.md)
  Remove an object by key from the dictionary.
- [- serialize](osdictionary/1412870-serialize.md)
- [- setCapacityIncrement](osdictionary/1412885-setcapacityincrement.md)
- [- setObject](osdictionary/1412895-setobject.md)
- [- setObject](../driverkit/osdictionary/setobject-9b4z0.md)
  Add or replace an object in the dictionary.
- [- setObject](../driverkit/osdictionary/setobject-7q0u2.md)
  Add or replace an object in the dictionary.
- [- setObject](osdictionary/3567168-setobject.md)
- [- setObject](osdictionary/3567169-setobject.md)
- [- setObject](osdictionary/3567170-setobject.md)
- [- setOptions](osdictionary/1412891-setoptions.md)
  Recursively sets option bits in the dictionary and all child collections.
### Type Methods
- [+ withCapacity](../driverkit/osdictionary/withcapacity.md)
  Allocates an OSDictionary object with preallocated capacity.
- [+ withDictionary](../driverkit/osdictionary/withdictionary.md)
  Allocates an OSDictionary object with given members and preallocated capacity.
- [+ withObjects](osdictionary/1412890-withobjects.md)
- [+ withObjects](../driverkit/osdictionary/withobjects.md)
  Allocates an OSDictionary object with given members and preallocated capacity.

## Relationships

### Inherits From
- [OSCollection](oscollection.md)

## See Also

- [OSArray](osarray.md)
  OSArray provides an indexed store of objects.
- [OSSet](osset.md)
  OSSet provides an unordered set store of objects.
- [OSOrderedSet](osorderedset.md)
  OSOrderedSet provides an ordered set store of objects.
- [OSCollection](oscollection.md)
  The abstract superclass for Libkern collections.
- [OSCollectionIterator](oscollectioniterator.md)
- [OSIterator](ositerator.md)
  The abstract superclass for Libkern iterators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdictionary)*