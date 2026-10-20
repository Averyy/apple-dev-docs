# OSDictionary

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

OSDictionary provides an associative store using strings for keys.

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class OSDictionary : OSCollection
```

#### Overview

OSDictionary is a container for Libkern C++ objects (those derived from OSMetaClassBase, in particular OSObject). Storage and access are associative, based on string-valued keys (C string, `OSString`, or [`OSSymbol`](./ossymbol.md)). When adding an object to an OSDictionary, you provide a string identifier, which can then used to retrieve that object or remove it from the dictionary. Setting an object with a key that already has an associated object replaces the original object.

You must generally cast retrieved objects from [`OSObject`](./osobject.md) to the desired class using OSDynamicCast. This macro returns the object cast to the desired class, or `NULL` if the object isn't derived from that class.

When iterating an OSDictionary using OSCollectionIterator, the objects returned from getNextObject are dictionary keys (not the object values for those keys). You can use the keys to retrieve their associated object values.

As with all Libkern collection classes, OSDictionary retains keys and objects added to it, and releases keys and objects removed from it (or replaced). An OSDictionary also grows as necessary to accommodate new key/value pairs, *unlike* Core Foundation collections (it does not, however, shrink).

**Note:** OSDictionary currently uses a linear search algorithm, and is not designed for high-performance access of many values. It is intended as a simple associative-storage mechanism only.

**Use Restrictions**

With very few exceptions in the I/O Kit, all Libkern-based C++ classes, functions, and macros are **unsafe** to use in a primary interrupt context. Consult the I/O Kit documentation related to primary interrupts for more information.

OSDictionary provides no concurrency protection; it's up to the usage context to provide any protection necessary. Some portions of the I/O Kit, such as IORegistryEntry, handle synchronization via defined member functions for setting properties.

## Topics

### Miscellaneous
- [copyCollection](./osdictionary/api-1808081-copycollection.md)
  Creates a deep copy of the dictionary and its child collections.
- [ensureCapacity](./osdictionary/api-1808087-ensurecapacity.md)
  Ensures the dictionary has enough space to store the requested number of key/object pairs.
- [flushCollection](./osdictionary/api-1808092-flushcollection.md)
  Removes and releases all keys and objects within the dictionary.
- [free](./osdictionary/api-1808101-free.md)
  Deallocates or releases any resources used by the OSDictionary instance.
- [getCapacity](./osdictionary/api-1808107-getcapacity.md)
  Returns the number of objects the dictionary can store without reallocating.
- [getCapacityIncrement](./osdictionary/api-1808116-getcapacityincrement.md)
  Returns the storage increment of the dictionary.
- [getCount](./osdictionary/api-1808124-getcount.md)
  Returns the current number of key/object pairs contained within the dictionary.
- [getObject](./osdictionary/api-1808133-getobject.md)
  Returns the object stored under a given key.
- [getObject(const OSString *)](./osdictionary/api-1808139-getobject.md)
  Returns the object stored under a given key.
- [getObject(const OSSymbol *)](./osdictionary/api-1808148-getobject.md)
  Returns the object stored under a given key.
- [initWithCapacity](./osdictionary/api-1808159-initwithcapacity.md)
  Initializes a new instance of OSDictionary.
- [initWithDictionary](./osdictionary/api-1808166-initwithdictionary.md)
  Initializes a new OSDictionary with the contents of another dictionary.
- [initWithObjects(const OSObject *, const OSString *, unsigned int, unsigned int)](./osdictionary/api-1808177-initwithobjects.md)
  Initializes a new OSDictionary with keys and objects provided.
- [initWithObjects(const OSObject *, const OSSymbol *, unsigned int, unsigned int)](./osdictionary/api-1808181-initwithobjects.md)
  Initializes a new OSDictionary with keys and objects provided.
- [isEqualTo](./osdictionary/api-1808187-isequalto.md)
  Tests the equality of an OSDictionary to an arbitrary object.
- [isEqualTo(const OSDictionary *)](./osdictionary/api-1808191-isequalto.md)
  Tests the equality of two OSDictionary objects.
- [isEqualTo(const OSDictionary *, const OSCollection *)](./osdictionary/api-1808194-isequalto.md)
  Tests the equality of two OSDictionary objects over a subset of keys.
- [merge](./osdictionary/api-1808198-merge.md)
  Merges the contents of a dictionary into the receiver.
- [removeObject](./osdictionary/api-1808205-removeobject.md)
  Removes a key/object pair from the dictionary.
- [removeObject(const OSString *)](./osdictionary/api-1808207-removeobject.md)
  Removes a key/object pair from the dictionary.
- [removeObject(const OSSymbol *)](./osdictionary/api-1808209-removeobject.md)
  Removes a key/object pair from the dictionary.
- [serialize](./osdictionary/api-1808214-serialize.md)
  Archives the receiver into the provided OSSerialize object.
- [setCapacityIncrement](./osdictionary/api-1808218-setcapacityincrement.md)
  Sets the storage increment of the dictionary.
- [setObject](./osdictionary/api-1808220-setobject.md)
  Stores an object in the dictionary under a key.
- [setObject(const OSString *, const OSMetaClassBase *)](./osdictionary/api-1808224-setobject.md)
  Stores an object in the dictionary under a key.
- [setObject(const OSSymbol *, const OSMetaClassBase *)](./osdictionary/api-1808227-setobject.md)
  Stores an object in the dictionary under a key.
- [withCapacity](./osdictionary/api-1808230-withcapacity.md)
  Creates and initializes an empty OSDictionary.
- [withDictionary](./osdictionary/api-1808234-withdictionary.md)
  Creates and initializes an OSDictionary populated with the contents of another dictionary.
- [withObjects(const OSObject *, const OSString *, unsigned int, unsigned int)](./osdictionary/api-1808237-withobjects.md)
  Creates and initializes an OSDictionary populated with keys and objects provided.
- [withObjects(const OSObject *, const OSSymbol *, unsigned int, unsigned int)](./osdictionary/api-1808240-withobjects.md)
  Creates and initializes an OSDictionary populated with keys and objects provided.
### Instance Methods
- [- copyCollection](./osdictionary/api-1412868-copycollection.md)
- [- ensureCapacity](./osdictionary/api-3180896-ensurecapacity.md)
  Allocates capacity for members in dictionary.
- [- flushCollection](./osdictionary/api-3180897-flushcollection.md)
  Removes and drops references to all members of dictionary.
- [- free](./osdictionary/api-3180898-free.md)
- [- getCapacity](./osdictionary/api-3180899-getcapacity.md)
  Returns count of currently allocated capacity for members in dictionary.
- [- getCapacityIncrement](./osdictionary/api-1412877-getcapacityincrement.md)
- [- getCount](./osdictionary/api-3180900-getcount.md)
  Returns count of members in dictionary.
- [- getMetaClass](./osdictionary/api-1412876-getmetaclass.md)
- [- getNextObjectForIterator](./osdictionary/api-1412886-getnextobjectforiterator.md)
- [- getObject](./osdictionary/api-1412897-getobject.md)
- [- getObject](./osdictionary/api-3180901-getobject.md)
  Returns a member of the dictionary.
- [- getObject](./osdictionary/api-3433846-getobject.md)
  Returns a member of the dictionary.
- [- initIterator](./osdictionary/api-1412888-inititerator.md)
- [- initWithCapacity](./osdictionary/api-1412883-initwithcapacity.md)
- [- initWithDictionary](./osdictionary/api-1412866-initwithdictionary.md)
- [- initWithObjects](./osdictionary/api-1412860-initwithobjects.md)
- [- initWithObjects](./osdictionary/api-3516835-initwithobjects.md)
- [- isEqualTo](./osdictionary/api-3180902-isequalto.md)
  Compares certain members of two dictionaries with isEqualTo().
- [- isEqualTo](./osdictionary/api-3433847-isequalto.md)
  Compares all members of two dictionaries with isEqualTo().
- [- isEqualTo](./osdictionary/api-3433848-isequalto.md)
  Compares the dictionary with an OSObject
- [- iterateObjects](./osdictionary/api-2967352-iterateobjects.md)
- [- iterateObjects](./osdictionary/api-3516836-iterateobjects.md)
- [- iteratorSize](./osdictionary/api-1412862-iteratorsize.md)
- [- merge](./osdictionary/api-3180904-merge.md)
  Adds all members of a dictionary to this dictionary.
- [- removeObject](./osdictionary/api-1412855-removeobject.md)
- [- removeObject](./osdictionary/api-3180905-removeobject.md)
  Remove an object by key from the dictionary.
- [- removeObject](./osdictionary/api-3433849-removeobject.md)
  Remove an object by key from the dictionary.
- [- serialize](./osdictionary/api-1412870-serialize.md)
- [- setCapacityIncrement](./osdictionary/api-1412885-setcapacityincrement.md)
- [- setObject](./osdictionary/api-1412895-setobject.md)
- [- setObject](./osdictionary/api-3180906-setobject.md)
  Add or replace an object in the dictionary.
- [- setObject](./osdictionary/api-3433850-setobject.md)
  Add or replace an object in the dictionary.
- [- setObject](./osdictionary/api-3567168-setobject.md)
- [- setObject](./osdictionary/api-3567169-setobject.md)
- [- setObject](./osdictionary/api-3567170-setobject.md)
- [- setOptions](./osdictionary/api-1412891-setoptions.md)
  Recursively sets option bits in the dictionary and all child collections.
### Type Methods
- [+ withCapacity](./osdictionary/api-3180907-withcapacity.md)
  Allocates an OSDictionary object with preallocated capacity.
- [+ withDictionary](./osdictionary/api-3180908-withdictionary.md)
  Allocates an OSDictionary object with given members and preallocated capacity.
- [+ withObjects](./osdictionary/api-1412890-withobjects.md)
- [+ withObjects](./osdictionary/api-3180909-withobjects.md)
  Allocates an OSDictionary object with given members and preallocated capacity.

## Relationships

### Inherits From
- [OSCollection](./oscollection.md)

## See Also

### Collections
- [OSArray](./osarray.md)
  OSArray provides an indexed store of objects.
- [OSSet](./osset.md)
  OSSet provides an unordered set store of objects.
- [OSOrderedSet](./osorderedset.md)
  OSOrderedSet provides an ordered set store of objects.
- [OSCollection](./oscollection.md)
  The abstract superclass for Libkern collections.
- [OSCollectionIterator](./oscollectioniterator.md)
- [OSIterator](./ositerator.md)
  The abstract superclass for Libkern iterators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdictionary)*