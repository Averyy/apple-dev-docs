# copyCollection

**Framework**: Kernel  
**Kind**: instm

Creates a deep copy of the dictionary and its child collections.

## Declaration

```swift
OSCollection * copyCollection(
 OSDictionary *cycleDict = 0);
```

#### Return_value

The newly copied dictionary, with a retain count of 1, or `NULL` if there is insufficient memory to do the copy.

#### Overview

The receiving dictionary, and any collections it contains, recursively, are copied. Objects that are not derived from OSCollection are retained rather than copied.

## Parameters

- `cycleDict`: A dictionary of all of the collections that have been copied so far, which is used to track circular references. To start the copy at the top level, pass  .

## See Also

- [ensureCapacity](osdictionary/1808087-ensurecapacity.md)
  Ensures the dictionary has enough space to store the requested number of key/object pairs.
- [flushCollection](osdictionary/1808092-flushcollection.md)
  Removes and releases all keys and objects within the dictionary.
- [free](osdictionary/1808101-free.md)
  Deallocates or releases any resources used by the OSDictionary instance.
- [getCapacity](osdictionary/1808107-getcapacity.md)
  Returns the number of objects the dictionary can store without reallocating.
- [getCapacityIncrement](osdictionary/1808116-getcapacityincrement.md)
  Returns the storage increment of the dictionary.
- [getCount](osdictionary/1808124-getcount.md)
  Returns the current number of key/object pairs contained within the dictionary.
- [getObject](osdictionary/1808133-getobject.md)
  Returns the object stored under a given key.
- [getObject(const OSString *)](osdictionary/1808139-getobject.md)
  Returns the object stored under a given key.
- [getObject(const OSSymbol *)](osdictionary/1808148-getobject.md)
  Returns the object stored under a given key.
- [initWithCapacity](osdictionary/1808159-initwithcapacity.md)
  Initializes a new instance of OSDictionary.
- [initWithDictionary](osdictionary/1808166-initwithdictionary.md)
  Initializes a new OSDictionary with the contents of another dictionary.
- [initWithObjects(const OSObject *, const OSString *, unsigned int, unsigned int)](osdictionary/1808177-initwithobjects.md)
  Initializes a new OSDictionary with keys and objects provided.
- [initWithObjects(const OSObject *, const OSSymbol *, unsigned int, unsigned int)](osdictionary/1808181-initwithobjects.md)
  Initializes a new OSDictionary with keys and objects provided.
- [isEqualTo](osdictionary/1808187-isequalto.md)
  Tests the equality of an OSDictionary to an arbitrary object.
- [isEqualTo(const OSDictionary *)](osdictionary/1808191-isequalto.md)
  Tests the equality of two OSDictionary objects.
- [isEqualTo(const OSDictionary *, const OSCollection *)](osdictionary/1808194-isequalto.md)
  Tests the equality of two OSDictionary objects over a subset of keys.
- [merge](osdictionary/1808198-merge.md)
  Merges the contents of a dictionary into the receiver.
- [removeObject](osdictionary/1808205-removeobject.md)
  Removes a key/object pair from the dictionary.
- [removeObject(const OSString *)](osdictionary/1808207-removeobject.md)
  Removes a key/object pair from the dictionary.
- [removeObject(const OSSymbol *)](osdictionary/1808209-removeobject.md)
  Removes a key/object pair from the dictionary.
- [serialize](osdictionary/1808214-serialize.md)
  Archives the receiver into the provided OSSerialize object.
- [setCapacityIncrement](osdictionary/1808218-setcapacityincrement.md)
  Sets the storage increment of the dictionary.
- [setObject](osdictionary/1808220-setobject.md)
  Stores an object in the dictionary under a key.
- [setObject(const OSString *, const OSMetaClassBase *)](osdictionary/1808224-setobject.md)
  Stores an object in the dictionary under a key.
- [setObject(const OSSymbol *, const OSMetaClassBase *)](osdictionary/1808227-setobject.md)
  Stores an object in the dictionary under a key.
- [withCapacity](osdictionary/1808230-withcapacity.md)
  Creates and initializes an empty OSDictionary.
- [withDictionary](osdictionary/1808234-withdictionary.md)
  Creates and initializes an OSDictionary populated with the contents of another dictionary.
- [withObjects(const OSObject *, const OSString *, unsigned int, unsigned int)](osdictionary/1808237-withobjects.md)
  Creates and initializes an OSDictionary populated with keys and objects provided.
- [withObjects(const OSObject *, const OSSymbol *, unsigned int, unsigned int)](osdictionary/1808240-withobjects.md)
  Creates and initializes an OSDictionary populated with keys and objects provided.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdictionary/1808081-copycollection)*