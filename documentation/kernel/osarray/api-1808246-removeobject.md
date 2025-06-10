# removeObject

**Framework**: Kernel  
**Kind**: instm

Removes an object from the array.

## Declaration

```swift
virtual void removeObject(
 unsigned intindex);
```

#### Overview

This function moves existing objects to fill the vacated index so that there are no gaps. The object removed is released.

## Parameters

- `index`: The index of the object to be removed.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osarray/1808246-removeobject)*