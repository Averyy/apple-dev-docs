# OSArray

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

OSArray provides an indexed store of objects.

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class OSArray : OSCollection
```

#### Overview

OSArray is a container for Libkern C++ objects (those derived from OSMetaClassBase, in particular OSObject). Storage and access are by array index.

You must generally cast retrieved objects from [`OSObject`](./osobject.md) to the desired class using OSDynamicCast. This macro returns the object cast to the desired class, or `NULL` if the object isn't derived from that class.

As with all Libkern collection classes, OSArray retains objects added to it, and releases objects removed from it (or replaced). An OSArray also grows as necessary to accommodate new objects, *unlike* Core Foundation collections (it does not, however, shrink).

**Use Restrictions**

With very few exceptions in the I/O Kit, all Libkern-based C++ classes, functions, and macros are **unsafe** to use in a primary interrupt context. Consult the I/O Kit documentation related to primary interrupts for more information.

OSArray provides no concurrency protection; it's up to the usage context to provide any protection necessary. Some portions of the I/O Kit, such as IORegistryEntry, handle synchronization via defined member functions for setting properties.

## Topics

### Miscellaneous
- [copyCollection](./osarray/api-1808122-copycollection.md)
  Creates a deep copy of an array and its child collections.
- [ensureCapacity](./osarray/api-1808132-ensurecapacity.md)
  Ensures the array has enough space to store the requested number of objects.
- [flushCollection](./osarray/api-1808145-flushcollection.md)
  Removes and releases all objects within the array.
- [free](./osarray/api-1808156-free.md)
  Deallocates or releases any resources used by the OSArray instance.
- [getCapacity](./osarray/api-1808168-getcapacity.md)
  Returns the number of objects the array can store without reallocating.
- [getCapacityIncrement](./osarray/api-1808174-getcapacityincrement.md)
  Returns the storage increment of the array.
- [getCount](./osarray/api-1808184-getcount.md)
  Returns the current number of objects within the array.
- [getLastObject](./osarray/api-1808193-getlastobject.md)
  Returns the last object in the array.
- [getNextIndexOfObject](./osarray/api-1808202-getnextindexofobject.md)
  Scans the array for the next instance of a specific object at or beyond a given index.
- [getObject](./osarray/api-1808210-getobject.md)
  Return the object stored at a given index.
- [initWithArray](./osarray/api-1808216-initwitharray.md)
  Initializes a new OSArray populated with the contents of another array.
- [initWithCapacity](./osarray/api-1808222-initwithcapacity.md)
  Initializes a new instance of OSArray.
- [initWithObjects](./osarray/api-1808226-initwithobjects.md)
  Initializes a new OSArray populated with objects provided.
- [isEqualTo(const OSArray *)](./osarray/api-1808231-isequalto.md)
  Tests the equality of two OSArray objects.
- [isEqualTo(const OSMetaClassBase *)](./osarray/api-1808236-isequalto.md)
  Tests the equality of an OSArray to an arbitrary object.
- [merge](./osarray/api-1808242-merge.md)
  Appends the contents of an array onto the receiving array.
- [removeObject](./osarray/api-1808246-removeobject.md)
  Removes an object from the array.
- [replaceObject](./osarray/api-1808249-replaceobject.md)
  Replaces an object in an array at a given index.
- [serialize](./osarray/api-1808255-serialize.md)
  Archives the receiver into the provided OSSerialize object.
- [setCapacityIncrement](./osarray/api-1808259-setcapacityincrement.md)
  Sets the storage increment of the array.
- [setObject(const OSMetaClassBase *)](./osarray/api-1808261-setobject.md)
  Appends an object onto the end of the array, increasing storage if necessary.
- [setObject(unsigned int, const OSMetaClassBase *)](./osarray/api-1808266-setobject.md)
  Inserts or appends an object into the array at a particular index.
- [withArray](./osarray/api-1808272-witharray.md)
  Creates and initializes an OSArray populated with the contents of another array.
- [withCapacity](./osarray/api-1808279-withcapacity.md)
  Creates and initializes an empty OSArray.
- [withObjects](./osarray/api-1808285-withobjects.md)
  Creates and initializes an OSArray populated with objects provided.
### Instance Methods
- [- copyCollection](./osarray/api-1448234-copycollection.md)
- [- ensureCapacity](./osarray/api-3180809-ensurecapacity.md)
  Allocates capacity for members in array.
- [- flushCollection](./osarray/api-3180810-flushcollection.md)
  Removes and drops references to all members of array.
- [- free](./osarray/api-3180811-free.md)
- [- getCapacity](./osarray/api-3180812-getcapacity.md)
  Returns count of currently allocated capacity for members in array.
- [- getCapacityIncrement](./osarray/api-1448240-getcapacityincrement.md)
- [- getCount](./osarray/api-3180813-getcount.md)
  Returns count of members in array.
- [- getLastObject](./osarray/api-3180814-getlastobject.md)
  Returns the last member of the array.
- [- getMetaClass](./osarray/api-1448214-getmetaclass.md)
- [- getNextIndexOfObject](./osarray/api-3180815-getnextindexofobject.md)
  Searches the array for an object.
- [- getNextObjectForIterator](./osarray/api-1448224-getnextobjectforiterator.md)
- [- getObject](./osarray/api-3180816-getobject.md)
  Returns a member of the array.
- [- initIterator](./osarray/api-1448201-inititerator.md)
- [- initWithArray](./osarray/api-1448198-initwitharray.md)
- [- initWithCapacity](./osarray/api-1448218-initwithcapacity.md)
- [- initWithObjects](./osarray/api-1448254-initwithobjects.md)
- [- isEqualTo](./osarray/api-3180817-isequalto.md)
  Compares all members of two arrays with isEqualTo().
- [- isEqualTo](./osarray/api-3433839-isequalto.md)
  Compares the array with an OSObject
- [- iteratorSize](./osarray/api-1448229-iteratorsize.md)
- [- merge](./osarray/api-3180819-merge.md)
  Appends all members of an array to this array.
- [- removeObject](./osarray/api-3180820-removeobject.md)
  Removes a current member of the array.
- [- replaceObject](./osarray/api-3180821-replaceobject.md)
  Removes a current member of the array and replaces it with another object.
- [- replaceObject](./osarray/api-3567165-replaceobject.md)
- [- serialize](./osarray/api-1448205-serialize.md)
- [- setCapacityIncrement](./osarray/api-1448250-setcapacityincrement.md)
- [- setObject](./osarray/api-3180822-setobject.md)
  Appends an object as the last member of the array.
- [- setObject](./osarray/api-3433840-setobject.md)
  Sets an object as the member of the array at a given index.
- [- setObject](./osarray/api-3567166-setobject.md)
- [- setObject](./osarray/api-3567167-setobject.md)
- [- setOptions](./osarray/api-1448245-setoptions.md)
  Recursively sets option bits in an array and all child collections.
### Type Methods
- [+ withArray](./osarray/api-3180823-witharray.md)
  Allocates an OSArray object with given members and preallocated capacity.
- [+ withCapacity](./osarray/api-3180824-withcapacity.md)
  Allocates an OSArray object with preallocated capacity.
- [+ withObjects](./osarray/api-3180825-withobjects.md)
  Allocates an OSArray object with given members and preallocated capacity.

## Relationships

### Inherits From
- [OSCollection](./oscollection.md)

## See Also

### Collections
- [OSDictionary](./osdictionary.md)
  OSDictionary provides an associative store using strings for keys.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osarray)*