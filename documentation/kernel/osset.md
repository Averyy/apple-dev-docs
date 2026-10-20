# OSSet

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

OSSet provides an unordered set store of objects.

**Availability**:
- DriverKit 21.0+
- macOS 10.0+

## Declaration

*DriverKit*

```cpp
class OSSet : OSArray
```

*macOS*

```cpp
class OSSet : OSCollection
```

#### Overview

OSSet is a container for Libkern C++ objects (those derived from OSMetaClassBase, in particular OSObject). Storage and access follow basic set logic: you can add or remove an object, and test whether the set contains a particular object. A given object is only stored in the set once, and there is no ordering of objects in the set. A subclass OSOrderedSet, provides for ordered set logic.

As with all Libkern collection classes, OSSet retains objects added to it, and releases objects removed from it. An OSSet also grows as necessary to accommodate new objects, *unlike* Core Foundation collections (it does not, however, shrink).

**Use Restrictions**

With very few exceptions in the I/O Kit, all Libkern-based C++ classes, functions, and macros are **unsafe** to use in a primary interrupt context. Consult the I/O Kit documentation related to primary interrupts for more information.

OSSet provides no concurrency protection; it's up to the usage context to provide any protection necessary. Some portions of the I/O Kit, such as IORegistryEntry, handle synchronization via defined member functions for setting properties.

## Topics

### Miscellaneous
- [containsObject](./osset/api-1808031-containsobject.md)
  Checks the set for the presence of an object.
- [copyCollection](./osset/api-1808046-copycollection.md)
  Creates a deep copy of this set and its child collections.
- [ensureCapacity](./osset/api-1808068-ensurecapacity.md)
  Ensures the set has enough space to store the requested number of distinct objects.
- [flushCollection](./osset/api-1808084-flushcollection.md)
  Removes and releases all objects within the set.
- [free](./osset/api-1808104-free.md)
  Deallocates or releases any resources used by the OSSet instance.
- [getAnyObject](./osset/api-1808128-getanyobject.md)
  Returns an arbitrary (not random) object from the set.
- [getCapacity](./osset/api-1808152-getcapacity.md)
  Returns the number of objects the set can store without reallocating.
- [getCapacityIncrement](./osset/api-1808173-getcapacityincrement.md)
  Returns the storage increment of the set.
- [getCount](./osset/api-1808189-getcount.md)
  Returns the current number of objects within the set.
- [initWithArray](./osset/api-1808200-initwitharray.md)
  Initializes a new OSSet populated with the contents of an OSArray.
- [initWithCapacity](./osset/api-1808213-initwithcapacity.md)
  Initializes a new instance of OSSet.
- [initWithObjects](./osset/api-1808221-initwithobjects.md)
  Initializes a new OSSet populated with objects provided.
- [initWithSet](./osset/api-1808228-initwithset.md)
  Initializes a new OSSet populated with the contents of another OSSet.
- [isEqualTo(const OSMetaClassBase *)](./osset/api-1808235-isequalto.md)
  Tests the equality of an OSSet against an arbitrary object.
- [isEqualTo(const OSSet *)](./osset/api-1808239-isequalto.md)
  Tests the equality of two OSSet objects.
- [member](./osset/api-1808245-member.md)
  Checks the set for the presence of an object.
- [merge(const OSArray *)](./osset/api-1808250-merge.md)
  Adds the contents of an OSArray to the set.
- [merge(const OSSet *)](./osset/api-1808253-merge.md)
  Adds the contents of an OSet to the set.
- [removeObject](./osset/api-1808257-removeobject.md)
  Removes an object from the set.
- [serialize](./osset/api-1808260-serialize.md)
  Archives the receiver into the provided OSSerialize object.
- [setCapacityIncrement](./osset/api-1808264-setcapacityincrement.md)
  Sets the storage increment of the set.
- [setObject](./osset/api-1808269-setobject.md)
  Adds an object to the OSSet if it is not already present.
- [withArray](./osset/api-1808277-witharray.md)
  Creates and initializes an OSSet populated with the contents of an OSArray.
- [withCapacity](./osset/api-1808282-withcapacity.md)
  Creates and initializes an empty OSSet.
- [withObjects](./osset/api-1808287-withobjects.md)
  Creates and initializes an OSSet populated with objects provided.
- [withSet](./osset/api-1808291-withset.md)
  Creates and initializes an OSSet populated with the contents of another OSSet.
### Instance Methods
- [- containsObject](./osset/api-1535170-containsobject.md)
- [- copyCollection](./osset/api-1535199-copycollection.md)
- [- ensureCapacity](./osset/api-1535195-ensurecapacity.md)
- [- flushCollection](./osset/api-1535159-flushcollection.md)
- [- free](./osset/api-1535175-free.md)
- [- getAnyObject](./osset/api-1535166-getanyobject.md)
- [- getCapacity](./osset/api-1535197-getcapacity.md)
- [- getCapacityIncrement](./osset/api-1535169-getcapacityincrement.md)
- [- getCount](./osset/api-1535182-getcount.md)
- [- getMetaClass](./osset/api-1535185-getmetaclass.md)
- [- getNextObjectForIterator](./osset/api-1535167-getnextobjectforiterator.md)
- [- init](../DriverKit/osset/init.md)
- [- initIterator](./osset/api-1535164-inititerator.md)
- [- initWithArray](./osset/api-1535174-initwitharray.md)
- [- initWithCapacity](./osset/api-1535162-initwithcapacity.md)
- [- initWithObjects](./osset/api-1535189-initwithobjects.md)
- [- initWithSet](./osset/api-1535161-initwithset.md)
- [- isEqualTo](./osset/api-1535171-isequalto.md)
- [- isEqualTo](./osset/api-3516842-isequalto.md)
- [- iteratorSize](./osset/api-1535180-iteratorsize.md)
- [- member](./osset/api-1535179-member.md)
- [- merge](./osset/api-1535168-merge.md)
- [- merge](./osset/api-3516843-merge.md)
- [- removeObject](./osset/api-1535183-removeobject.md)
- [- removeObject](./osset/api-3567176-removeobject.md)
- [- serialize](./osset/api-1535191-serialize.md)
- [- setCapacityIncrement](./osset/api-1535173-setcapacityincrement.md)
- [- setObject](./osset/api-1535188-setobject.md)
- [- setObject](./osset/api-3567177-setobject.md)
- [- setOptions](./osset/api-1535177-setoptions.md)
  Recursively sets option bits in the set and all child collections.
### Type Methods
- [+ withArray](./osset/api-1535176-witharray.md)
- [+ withCapacity](./osset/api-1535163-withcapacity.md)
- [+ withObjects](./osset/api-1535193-withobjects.md)
- [+ withSet](./osset/api-1535186-withset.md)

## Relationships

### Inherits From
- [OSArray](../DriverKit/osarray.md)
- [OSCollection](./oscollection.md)

## See Also

### Collections
- [OSArray](./osarray.md)
  OSArray provides an indexed store of objects.
- [OSDictionary](./osdictionary.md)
  OSDictionary provides an associative store using strings for keys.
- [OSOrderedSet](./osorderedset.md)
  OSOrderedSet provides an ordered set store of objects.
- [OSCollection](./oscollection.md)
  The abstract superclass for Libkern collections.
- [OSCollectionIterator](./oscollectioniterator.md)
- [OSIterator](./ositerator.md)
  The abstract superclass for Libkern iterators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osset)*