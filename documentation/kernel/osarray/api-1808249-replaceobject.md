# replaceObject

**Framework**: Kernel  
**Kind**: instm

Replaces an object in an array at a given index.

## Declaration

```cpp
virtual void replaceObject( 
 unsigned intindex, 
 const OSMetaClassBase *anObject);
```

## Overview

The original object is released and the new object is retained.

## Parameters

- `index`: The index of the object to be replaced. Must be less than the array's count.
- `anObject`: The object to be placed into the array.

## See Also

### Miscellaneous
- [copyCollection](./api-1808122-copycollection.md)
  Creates a deep copy of an array and its child collections.
- [ensureCapacity](./api-1808132-ensurecapacity.md)
  Ensures the array has enough space to store the requested number of objects.
- [flushCollection](./api-1808145-flushcollection.md)
  Removes and releases all objects within the array.
- [free](./api-1808156-free.md)
  Deallocates or releases any resources used by the OSArray instance.
- [getCapacity](./api-1808168-getcapacity.md)
  Returns the number of objects the array can store without reallocating.
- [getCapacityIncrement](./api-1808174-getcapacityincrement.md)
  Returns the storage increment of the array.
- [getCount](./api-1808184-getcount.md)
  Returns the current number of objects within the array.
- [getLastObject](./api-1808193-getlastobject.md)
  Returns the last object in the array.
- [getNextIndexOfObject](./api-1808202-getnextindexofobject.md)
  Scans the array for the next instance of a specific object at or beyond a given index.
- [getObject](./api-1808210-getobject.md)
  Return the object stored at a given index.
- [initWithArray](./api-1808216-initwitharray.md)
  Initializes a new OSArray populated with the contents of another array.
- [initWithCapacity](./api-1808222-initwithcapacity.md)
  Initializes a new instance of OSArray.
- [initWithObjects](./api-1808226-initwithobjects.md)
  Initializes a new OSArray populated with objects provided.
- [isEqualTo(const OSArray *)](./api-1808231-isequalto.md)
  Tests the equality of two OSArray objects.
- [isEqualTo(const OSMetaClassBase *)](./api-1808236-isequalto.md)
  Tests the equality of an OSArray to an arbitrary object.
- [merge](./api-1808242-merge.md)
  Appends the contents of an array onto the receiving array.
- [removeObject](./api-1808246-removeobject.md)
  Removes an object from the array.
- [serialize](./api-1808255-serialize.md)
  Archives the receiver into the provided OSSerialize object.
- [setCapacityIncrement](./api-1808259-setcapacityincrement.md)
  Sets the storage increment of the array.
- [setObject(const OSMetaClassBase *)](./api-1808261-setobject.md)
  Appends an object onto the end of the array, increasing storage if necessary.
- [setObject(unsigned int, const OSMetaClassBase *)](./api-1808266-setobject.md)
  Inserts or appends an object into the array at a particular index.
- [withArray](./api-1808272-witharray.md)
  Creates and initializes an OSArray populated with the contents of another array.
- [withCapacity](./api-1808279-withcapacity.md)
  Creates and initializes an empty OSArray.
- [withObjects](./api-1808285-withobjects.md)
  Creates and initializes an OSArray populated with objects provided.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osarray/1808249-replaceobject)*