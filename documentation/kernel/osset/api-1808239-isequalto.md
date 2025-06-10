# isEqualTo(const OSSet *)

**Framework**: Kernel  
**Kind**: instm

Tests the equality of two OSSet objects.

## Declaration

```swift
virtual bool isEqualTo(
 const OSSet *aSet) const;
```

#### Return_value

`true` if the two sets are equivalent, `false` otherwise.

#### Overview

Two OSSet objects are considered equal if they have same count and the same object pointer values.

## Parameters

- `aSet`: The set object being compared against the receiver.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osset/1808239-isequalto)*