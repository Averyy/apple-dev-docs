# removeObject

**Framework**: Kernel  
**Kind**: instm

Removes an object from the set.

## Declaration

```cpp
virtual void removeObject(
 const OSMetaClassBase *anObject);
```

#### Overview

The object removed from the set is released.

## Parameters

- `anObject`: The OSMetaClassBase-derived object to be removed from the set.

## See Also

### Miscellaneous
- [containsObject](./api-1808031-containsobject.md)
  Checks the set for the presence of an object.
- [copyCollection](./api-1808046-copycollection.md)
  Creates a deep copy of this set and its child collections.
- [ensureCapacity](./api-1808068-ensurecapacity.md)
  Ensures the set has enough space to store the requested number of distinct objects.
- [flushCollection](./api-1808084-flushcollection.md)
  Removes and releases all objects within the set.
- [free](./api-1808104-free.md)
  Deallocates or releases any resources used by the OSSet instance.
- [getAnyObject](./api-1808128-getanyobject.md)
  Returns an arbitrary (not random) object from the set.
- [getCapacity](./api-1808152-getcapacity.md)
  Returns the number of objects the set can store without reallocating.
- [getCapacityIncrement](./api-1808173-getcapacityincrement.md)
  Returns the storage increment of the set.
- [getCount](./api-1808189-getcount.md)
  Returns the current number of objects within the set.
- [initWithArray](./api-1808200-initwitharray.md)
  Initializes a new OSSet populated with the contents of an OSArray.
- [initWithCapacity](./api-1808213-initwithcapacity.md)
  Initializes a new instance of OSSet.
- [initWithObjects](./api-1808221-initwithobjects.md)
  Initializes a new OSSet populated with objects provided.
- [initWithSet](./api-1808228-initwithset.md)
  Initializes a new OSSet populated with the contents of another OSSet.
- [isEqualTo(const OSMetaClassBase *)](./api-1808235-isequalto.md)
  Tests the equality of an OSSet against an arbitrary object.
- [isEqualTo(const OSSet *)](./api-1808239-isequalto.md)
  Tests the equality of two OSSet objects.
- [member](./api-1808245-member.md)
  Checks the set for the presence of an object.
- [merge(const OSArray *)](./api-1808250-merge.md)
  Adds the contents of an OSArray to the set.
- [merge(const OSSet *)](./api-1808253-merge.md)
  Adds the contents of an OSet to the set.
- [serialize](./api-1808260-serialize.md)
  Archives the receiver into the provided OSSerialize object.
- [setCapacityIncrement](./api-1808264-setcapacityincrement.md)
  Sets the storage increment of the set.
- [setObject](./api-1808269-setobject.md)
  Adds an object to the OSSet if it is not already present.
- [withArray](./api-1808277-witharray.md)
  Creates and initializes an OSSet populated with the contents of an OSArray.
- [withCapacity](./api-1808282-withcapacity.md)
  Creates and initializes an empty OSSet.
- [withObjects](./api-1808287-withobjects.md)
  Creates and initializes an OSSet populated with objects provided.
- [withSet](./api-1808291-withset.md)
  Creates and initializes an OSSet populated with the contents of another OSSet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osset/1808257-removeobject)*