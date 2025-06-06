# OSSet

**Framework**: Kernel  
**Kind**: cl

OSSet provides an unordered set store of objects.

**Availability**:
- DriverKit 21.0+
- macOS 10.0+

## Declaration

```swift
class OSSet : OSCollection
```

#### Overview

OSSet is a container for Libkern C++ objects (those derived from OSMetaClassBase, in particular OSObject). Storage and access follow basic set logic: you can add or remove an object, and test whether the set contains a particular object. A given object is only stored in the set once, and there is no ordering of objects in the set. A subclass OSOrderedSet, provides for ordered set logic.

As with all Libkern collection classes, OSSet retains objects added to it, and releases objects removed from it. An OSSet also grows as necessary to accommodate new objects,  Core Foundation collections (it does not, however, shrink).

With very few exceptions in the I/O Kit, all Libkern-based C++ classes, functions, and macros are  to use in a primary interrupt context. Consult the I/O Kit documentation related to primary interrupts for more information.

OSSet provides no concurrency protection; it's up to the usage context to provide any protection necessary. Some portions of the I/O Kit, such as IORegistryEntry, handle synchronization via defined member functions for setting properties.

## Topics

### Miscellaneous
- [containsObject](osset/1808031-containsobject.md)
  Checks the set for the presence of an object.
- [copyCollection](osset/1808046-copycollection.md)
  Creates a deep copy of this set and its child collections.
- [ensureCapacity](osset/1808068-ensurecapacity.md)
  Ensures the set has enough space to store the requested number of distinct objects.
- [flushCollection](osset/1808084-flushcollection.md)
  Removes and releases all objects within the set.
- [free](osset/1808104-free.md)
  Deallocates or releases any resources used by the OSSet instance.
- [getAnyObject](osset/1808128-getanyobject.md)
  Returns an arbitrary (not random) object from the set.
- [getCapacity](osset/1808152-getcapacity.md)
  Returns the number of objects the set can store without reallocating.
- [getCapacityIncrement](osset/1808173-getcapacityincrement.md)
  Returns the storage increment of the set.
- [getCount](osset/1808189-getcount.md)
  Returns the current number of objects within the set.
- [initWithArray](osset/1808200-initwitharray.md)
  Initializes a new OSSet populated with the contents of an OSArray.
- [initWithCapacity](osset/1808213-initwithcapacity.md)
  Initializes a new instance of OSSet.
- [initWithObjects](osset/1808221-initwithobjects.md)
  Initializes a new OSSet populated with objects provided.
- [initWithSet](osset/1808228-initwithset.md)
  Initializes a new OSSet populated with the contents of another OSSet.
- [isEqualTo(const OSMetaClassBase *)](osset/1808235-isequalto.md)
  Tests the equality of an OSSet against an arbitrary object.
- [isEqualTo(const OSSet *)](osset/1808239-isequalto.md)
  Tests the equality of two OSSet objects.
- [member](osset/1808245-member.md)
  Checks the set for the presence of an object.
- [merge(const OSArray *)](osset/1808250-merge.md)
  Adds the contents of an OSArray to the set.
- [merge(const OSSet *)](osset/1808253-merge.md)
  Adds the contents of an OSet to the set.
- [removeObject](osset/1808257-removeobject.md)
  Removes an object from the set.
- [serialize](osset/1808260-serialize.md)
  Archives the receiver into the provided OSSerialize object.
- [setCapacityIncrement](osset/1808264-setcapacityincrement.md)
  Sets the storage increment of the set.
- [setObject](osset/1808269-setobject.md)
  Adds an object to the OSSet if it is not already present.
- [withArray](osset/1808277-witharray.md)
  Creates and initializes an OSSet populated with the contents of an OSArray.
- [withCapacity](osset/1808282-withcapacity.md)
  Creates and initializes an empty OSSet.
- [withObjects](osset/1808287-withobjects.md)
  Creates and initializes an OSSet populated with objects provided.
- [withSet](osset/1808291-withset.md)
  Creates and initializes an OSSet populated with the contents of another OSSet.
### Instance Methods
- [- containsObject](osset/1535170-containsobject.md)
- [- copyCollection](osset/1535199-copycollection.md)
- [- ensureCapacity](osset/1535195-ensurecapacity.md)
- [- flushCollection](osset/1535159-flushcollection.md)
- [- free](osset/1535175-free.md)
- [- getAnyObject](osset/1535166-getanyobject.md)
- [- getCapacity](osset/1535197-getcapacity.md)
- [- getCapacityIncrement](osset/1535169-getcapacityincrement.md)
- [- getCount](osset/1535182-getcount.md)
- [- getMetaClass](osset/1535185-getmetaclass.md)
- [- getNextObjectForIterator](osset/1535167-getnextobjectforiterator.md)
- [- init](../driverkit/osset/3758352-init.md)
- [- initIterator](osset/1535164-inititerator.md)
- [- initWithArray](osset/1535174-initwitharray.md)
- [- initWithCapacity](osset/1535162-initwithcapacity.md)
- [- initWithObjects](osset/1535189-initwithobjects.md)
- [- initWithSet](osset/1535161-initwithset.md)
- [- isEqualTo](osset/1535171-isequalto.md)
- [- isEqualTo](osset/3516842-isequalto.md)
- [- iteratorSize](osset/1535180-iteratorsize.md)
- [- member](osset/1535179-member.md)
- [- merge](osset/1535168-merge.md)
- [- merge](osset/3516843-merge.md)
- [- removeObject](osset/1535183-removeobject.md)
- [- removeObject](osset/3567176-removeobject.md)
- [- serialize](osset/1535191-serialize.md)
- [- setCapacityIncrement](osset/1535173-setcapacityincrement.md)
- [- setObject](osset/1535188-setobject.md)
- [- setObject](osset/3567177-setobject.md)
- [- setOptions](osset/1535177-setoptions.md)
  Recursively sets option bits in the set and all child collections.
### Type Methods
- [+ withArray](osset/1535176-witharray.md)
- [+ withCapacity](osset/1535163-withcapacity.md)
- [+ withObjects](osset/1535193-withobjects.md)
- [+ withSet](osset/1535186-withset.md)

## Relationships

### Inherits From
- [OSArray](../driverkit/osarray.md)
- [OSCollection](oscollection.md)

## See Also

- [OSArray](osarray.md)
  OSArray provides an indexed store of objects.
- [OSDictionary](osdictionary.md)
  OSDictionary provides an associative store using strings for keys.
- [OSOrderedSet](osorderedset.md)
  OSOrderedSet provides an ordered set store of objects.
- [OSCollection](oscollection.md)
  The abstract superclass for Libkern collections.
- [OSCollectionIterator](oscollectioniterator.md)
- [OSIterator](ositerator.md)
  The abstract superclass for Libkern iterators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osset)*