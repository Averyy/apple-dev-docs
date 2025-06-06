# OSOrderedSet

**Framework**: Kernel  
**Kind**: cl

OSOrderedSet provides an ordered set store of objects.

**Availability**:
- DriverKit 21.0+
- macOS 10.0+

## Declaration

```swift
class OSOrderedSet : OSCollection
```

#### Overview

OSOrderedSet is a container for Libkern C++ objects (those derived from OSMetaClassBase, in particular OSObject). Storage and access follow ordered set logic. A given object is stored in the set only once, but you can:

- Define a sorting function for automated ordering (upon addition only)
- Manually insert new objects in the set (overriding sorting)
- Add and remove objects in the set
- Test whether the set contains a particular object
- Get the object stored at a particular index.

Note that automated ordering is performed only upon addition of objects and depends on the existing objects being properly sorted. There is no function to re-sort the contents of an OSOrderedSet or to change the ordering function. In general, you should either use the one ordered-insertion function, or the indexed-insertion functions, and not mix the two.

As with all Libkern collection classes, OSOrderedSet retains objects added to it, and releases objects removed from it. An OSOrderedSet also grows as necessary to accommodate new objects,  Core Foundation collections (it does not, however, shrink).

##### 1656370

With very few exceptions in the I/O Kit, all Libkern-based C++ classes, functions, and macros are  to use in a primary interrupt context. Consult the I/O Kit documentation related to primary interrupts for more information.

OSOrderedSet provides no concurrency protection; it's up to the usage context to provide any protection necessary. Some portions of the I/O Kit, such as IORegistryEntry, handle synchronization via defined member functions for setting properties.

## Topics

### Miscellaneous
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
- [isEqualTo(const OSOrderedSet *)](osorderedset/1808130-isequalto.md)
  Tests the equality of two OSOrderedSet objects.
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
### Callbacks
- [OSOrderFunction](osorderedset/osorderfunction.md)
  The sorting function used by an OSOrderedSet to order objects.
### Instance Methods
- [- containsObject](osorderedset/1397815-containsobject.md)
- [- copyCollection](osorderedset/1397819-copycollection.md)
- [- ensureCapacity](osorderedset/1397843-ensurecapacity.md)
- [- flushCollection](osorderedset/1397837-flushcollection.md)
- [- free](osorderedset/1397823-free.md)
- [- getCapacity](osorderedset/1397828-getcapacity.md)
- [- getCapacityIncrement](osorderedset/1397813-getcapacityincrement.md)
- [- getCount](osorderedset/1397848-getcount.md)
- [- getFirstObject](osorderedset/1397872-getfirstobject.md)
- [- getLastObject](osorderedset/1397850-getlastobject.md)
- [- getMetaClass](osorderedset/1397864-getmetaclass.md)
- [- getNextObjectForIterator](osorderedset/1397845-getnextobjectforiterator.md)
- [- getObject](osorderedset/1397841-getobject.md)
- [- getOrderingRef](osorderedset/1397835-getorderingref.md)
- [- init](../driverkit/osorderedset/3758350-init.md)
- [- initIterator](osorderedset/1397831-inititerator.md)
- [- initWithCapacity](osorderedset/1397858-initwithcapacity.md)
- [- isEqualTo](osorderedset/1397817-isequalto.md)
- [- isEqualTo](osorderedset/3516840-isequalto.md)
- [- iteratorSize](osorderedset/1397868-iteratorsize.md)
- [- member](osorderedset/1397854-member.md)
- [- orderObject](osorderedset/1397847-orderobject.md)
- [- removeObject](osorderedset/1397856-removeobject.md)
- [- removeObject](osorderedset/3567171-removeobject.md)
- [- setCapacityIncrement](osorderedset/1397839-setcapacityincrement.md)
- [- setFirstObject](osorderedset/1397821-setfirstobject.md)
- [- setFirstObject](osorderedset/3567172-setfirstobject.md)
- [- setLastObject](osorderedset/1397861-setlastobject.md)
- [- setLastObject](osorderedset/3567173-setlastobject.md)
- [- setObject](osorderedset/1397826-setobject.md)
- [- setObject](osorderedset/3516841-setobject.md)
- [- setObject](osorderedset/3567174-setobject.md)
- [- setObject](osorderedset/3567175-setobject.md)
- [- setOptions](osorderedset/1397833-setoptions.md)
### Type Methods
- [+ withCapacity](osorderedset/1397866-withcapacity.md)
- [+ withCapacity](osorderedset/3753632-withcapacity.md)

## Relationships

### Inherits From
- [OSCollection](oscollection.md)
- [OSSet](osset.md)

## See Also

- [OSArray](osarray.md)
  OSArray provides an indexed store of objects.
- [OSDictionary](osdictionary.md)
  OSDictionary provides an associative store using strings for keys.
- [OSSet](osset.md)
  OSSet provides an unordered set store of objects.
- [OSCollection](oscollection.md)
  The abstract superclass for Libkern collections.
- [OSCollectionIterator](oscollectioniterator.md)
- [OSIterator](ositerator.md)
  The abstract superclass for Libkern iterators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osorderedset)*