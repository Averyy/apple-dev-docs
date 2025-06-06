# OSArray

**Framework**: Kernel  
**Kind**: cl

OSArray provides an indexed store of objects.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class OSArray : OSCollection
```

#### Overview

OSArray is a container for Libkern C++ objects (those derived from OSMetaClassBase, in particular OSObject). Storage and access are by array index.

You must generally cast retrieved objects from [`OSObject`](osobject.md) to the desired class using OSDynamicCast. This macro returns the object cast to the desired class, or `NULL` if the object isn't derived from that class.

As with all Libkern collection classes, OSArray retains objects added to it, and releases objects removed from it (or replaced). An OSArray also grows as necessary to accommodate new objects,  Core Foundation collections (it does not, however, shrink).

With very few exceptions in the I/O Kit, all Libkern-based C++ classes, functions, and macros are  to use in a primary interrupt context. Consult the I/O Kit documentation related to primary interrupts for more information.

OSArray provides no concurrency protection; it's up to the usage context to provide any protection necessary. Some portions of the I/O Kit, such as IORegistryEntry, handle synchronization via defined member functions for setting properties.

## Topics

### Miscellaneous
- [copyCollection](osarray/1808122-copycollection.md)
  Creates a deep copy of an array and its child collections.
- [ensureCapacity](osarray/1808132-ensurecapacity.md)
  Ensures the array has enough space to store the requested number of objects.
- [flushCollection](osarray/1808145-flushcollection.md)
  Removes and releases all objects within the array.
- [free](osarray/1808156-free.md)
  Deallocates or releases any resources used by the OSArray instance.
- [getCapacity](osarray/1808168-getcapacity.md)
  Returns the number of objects the array can store without reallocating.
- [getCapacityIncrement](osarray/1808174-getcapacityincrement.md)
  Returns the storage increment of the array.
- [getCount](osarray/1808184-getcount.md)
  Returns the current number of objects within the array.
- [getLastObject](osarray/1808193-getlastobject.md)
  Returns the last object in the array.
- [getNextIndexOfObject](osarray/1808202-getnextindexofobject.md)
  Scans the array for the next instance of a specific object at or beyond a given index.
- [getObject](osarray/1808210-getobject.md)
  Return the object stored at a given index.
- [initWithArray](osarray/1808216-initwitharray.md)
  Initializes a new OSArray populated with the contents of another array.
- [initWithCapacity](osarray/1808222-initwithcapacity.md)
  Initializes a new instance of OSArray.
- [initWithObjects](osarray/1808226-initwithobjects.md)
  Initializes a new OSArray populated with objects provided.
- [isEqualTo(const OSArray *)](osarray/1808231-isequalto.md)
  Tests the equality of two OSArray objects.
- [isEqualTo(const OSMetaClassBase *)](osarray/1808236-isequalto.md)
  Tests the equality of an OSArray to an arbitrary object.
- [merge](osarray/1808242-merge.md)
  Appends the contents of an array onto the receiving array.
- [removeObject](osarray/1808246-removeobject.md)
  Removes an object from the array.
- [replaceObject](osarray/1808249-replaceobject.md)
  Replaces an object in an array at a given index.
- [serialize](osarray/1808255-serialize.md)
  Archives the receiver into the provided OSSerialize object.
- [setCapacityIncrement](osarray/1808259-setcapacityincrement.md)
  Sets the storage increment of the array.
- [setObject(const OSMetaClassBase *)](osarray/1808261-setobject.md)
  Appends an object onto the end of the array, increasing storage if necessary.
- [setObject(unsigned int, const OSMetaClassBase *)](osarray/1808266-setobject.md)
  Inserts or appends an object into the array at a particular index.
- [withArray](osarray/1808272-witharray.md)
  Creates and initializes an OSArray populated with the contents of another array.
- [withCapacity](osarray/1808279-withcapacity.md)
  Creates and initializes an empty OSArray.
- [withObjects](osarray/1808285-withobjects.md)
  Creates and initializes an OSArray populated with objects provided.
### Instance Methods
- [- copyCollection](osarray/1448234-copycollection.md)
- [- ensureCapacity](../driverkit/osarray/ensurecapacity.md)
  Allocates capacity for members in array.
- [- flushCollection](../driverkit/osarray/flushcollection.md)
  Removes and drops references to all members of array.
- [- free](../driverkit/osarray/free.md)
- [- getCapacity](../driverkit/osarray/getcapacity.md)
  Returns count of currently allocated capacity for members in array.
- [- getCapacityIncrement](osarray/1448240-getcapacityincrement.md)
- [- getCount](../driverkit/osarray/getcount.md)
  Returns count of members in array.
- [- getLastObject](../driverkit/osarray/getlastobject.md)
  Returns the last member of the array.
- [- getMetaClass](osarray/1448214-getmetaclass.md)
- [- getNextIndexOfObject](../driverkit/osarray/getnextindexofobject.md)
  Searches the array for an object.
- [- getNextObjectForIterator](osarray/1448224-getnextobjectforiterator.md)
- [- getObject](../driverkit/osarray/getobject.md)
  Returns a member of the array.
- [- initIterator](osarray/1448201-inititerator.md)
- [- initWithArray](osarray/1448198-initwitharray.md)
- [- initWithCapacity](osarray/1448218-initwithcapacity.md)
- [- initWithObjects](osarray/1448254-initwithobjects.md)
- [- isEqualTo](../driverkit/osarray/isequalto-5w7om.md)
  Compares all members of two arrays with isEqualTo().
- [- isEqualTo](../driverkit/osarray/isequalto-93qxy.md)
  Compares the array with an OSObject
- [- iteratorSize](osarray/1448229-iteratorsize.md)
- [- merge](../driverkit/osarray/merge.md)
  Appends all members of an array to this array.
- [- removeObject](../driverkit/osarray/removeobject.md)
  Removes a current member of the array.
- [- replaceObject](../driverkit/osarray/replaceobject.md)
  Removes a current member of the array and replaces it with another object.
- [- replaceObject](osarray/3567165-replaceobject.md)
- [- serialize](osarray/1448205-serialize.md)
- [- setCapacityIncrement](osarray/1448250-setcapacityincrement.md)
- [- setObject](../driverkit/osarray/setobject-3bore.md)
  Appends an object as the last member of the array.
- [- setObject](../driverkit/osarray/setobject-4ys3x.md)
  Sets an object as the member of the array at a given index.
- [- setObject](osarray/3567166-setobject.md)
- [- setObject](osarray/3567167-setobject.md)
- [- setOptions](osarray/1448245-setoptions.md)
  Recursively sets option bits in an array and all child collections.
### Type Methods
- [+ withArray](../driverkit/osarray/witharray.md)
  Allocates an OSArray object with given members and preallocated capacity.
- [+ withCapacity](../driverkit/osarray/withcapacity.md)
  Allocates an OSArray object with preallocated capacity.
- [+ withObjects](../driverkit/osarray/withobjects.md)
  Allocates an OSArray object with given members and preallocated capacity.

## Relationships

### Inherits From
- [OSCollection](oscollection.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osarray)*