# isEqualTo(const OSOrderedSet *)

**Framework**: Kernel  
**Kind**: instm

Tests the equality of two OSOrderedSet objects.

## Declaration

```swift
virtual bool isEqualTo(
 const OSOrderedSet *anOrderedSet) const;
```

#### Return_value

`true` if the two sets are equivalent, `false` otherwise.

#### Overview

Two OSOrderedSet objects are considered equal if they have same count and the same object pointer values in the same order.

## Parameters

- `anOrderedSet`: The ordered set object being compared against the receiver.

## See Also

- [containsObject](osorderedset/1808025-containsobject.md)
  Checks the ordered set for the presence of an object.
- [copyCollection](osorderedset/1808029-copycollection.md)
  Creates a deep copy of this ordered set and its child collections.
- [ensureCapacity](osorderedset/1808033-ensurecapacity.md)
  Ensures the set has enough space to store the requested number of distinct objects.
- [flushCollection](osorderedset/1808037-flushcollection.md)
  Removes and releases all objects within the ordered set.
- [free](osorderedset/1808043-free.md)
  Deallocatesand releases any resources used by the OSOrderedSet instance.
- [getCapacity](osorderedset/1808056-getcapacity.md)
  Returns the number of objects the ordered set can store without reallocating.
- [getCapacityIncrement](osorderedset/1808062-getcapacityincrement.md)
  Returns the storage increment of the ordered set.
- [getCount](osorderedset/1808070-getcount.md)
  Returns the current number of objects within the ordered set.
- [getFirstObject](osorderedset/1808079-getfirstobject.md)
  The object at index 0 in the ordered set if there is one, otherwise `NULL`.
- [getLastObject](osorderedset/1808089-getlastobject.md)
  The last object in the ordered set if there is one, otherwise `NULL`.
- [getObject](osorderedset/1808098-getobject.md)
  Gets the object at a particular index.
- [getOrderingRef](osorderedset/1808105-getorderingref.md)
  Returns the ordering context the ordered set was created with.
- [initWithCapacity](osorderedset/1808112-initwithcapacity.md)
  Initializes a new instance of OSOrderedSet.
- [isEqualTo(const OSMetaClassBase *)](osorderedset/1808121-isequalto.md)
  Tests the equality of an OSOrderedSet against an arbitrary object.
- [member](osorderedset/1808138-member.md)
  Checks the ordered set for the presence of an object.
- [orderObject](osorderedset/1808149-orderobject.md)
  Calls the ordered set's order function against a `NULL` object.
- [removeObject](osorderedset/1808158-removeobject.md)
  Removes an object from the ordered set.
- [setCapacityIncrement](osorderedset/1808163-setcapacityincrement.md)
  Sets the storage increment of the ordered set.
- [setFirstObject](osorderedset/1808169-setfirstobject.md)
  Adds an object to the OSOrderedSet at index 0 if it is not already present.
- [setLastObject](osorderedset/1808176-setlastobject.md)
  Adds an object at the end of the OSOrderedSet if it is not already present.
- [setObject(const OSMetaClassBase *)](osorderedset/1808180-setobject.md)
  Adds an object to the OSOrderedSet if it is not already present, storing it in sorted order if there is an order function.
- [setObject(unsigned int, const OSMetaClassBase *)](osorderedset/1808188-setobject.md)
  Adds an object to an OSOrderedSet at a specified index if it is not already present.
- [withCapacity](osorderedset/1808196-withcapacity.md)
  Creates and initializes an empty OSOrderedSet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osorderedset/1808130-isequalto)*