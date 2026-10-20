# removeObject(const OSSymbol *)

**Framework**: Kernel  
**Kind**: instm

Removes a key/object pair from the dictionary.

## Declaration

```cpp
virtual void removeObject(
 const OSSymbol *aKey);
```

#### Overview

The removed key (not necessarily `aKey` itself) and object are automatically released.

## Parameters

- `aKey`: An OSSymbol identifying the object to be removed from the dictionary.

## See Also

### Miscellaneous
- [copyCollection](./api-1808081-copycollection.md)
  Creates a deep copy of the dictionary and its child collections.
- [ensureCapacity](./api-1808087-ensurecapacity.md)
  Ensures the dictionary has enough space to store the requested number of key/object pairs.
- [flushCollection](./api-1808092-flushcollection.md)
  Removes and releases all keys and objects within the dictionary.
- [free](./api-1808101-free.md)
  Deallocates or releases any resources used by the OSDictionary instance.
- [getCapacity](./api-1808107-getcapacity.md)
  Returns the number of objects the dictionary can store without reallocating.
- [getCapacityIncrement](./api-1808116-getcapacityincrement.md)
  Returns the storage increment of the dictionary.
- [getCount](./api-1808124-getcount.md)
  Returns the current number of key/object pairs contained within the dictionary.
- [getObject](./api-1808133-getobject.md)
  Returns the object stored under a given key.
- [getObject(const OSString *)](./api-1808139-getobject.md)
  Returns the object stored under a given key.
- [getObject(const OSSymbol *)](./api-1808148-getobject.md)
  Returns the object stored under a given key.
- [initWithCapacity](./api-1808159-initwithcapacity.md)
  Initializes a new instance of OSDictionary.
- [initWithDictionary](./api-1808166-initwithdictionary.md)
  Initializes a new OSDictionary with the contents of another dictionary.
- [initWithObjects(const OSObject *, const OSString *, unsigned int, unsigned int)](./api-1808177-initwithobjects.md)
  Initializes a new OSDictionary with keys and objects provided.
- [initWithObjects(const OSObject *, const OSSymbol *, unsigned int, unsigned int)](./api-1808181-initwithobjects.md)
  Initializes a new OSDictionary with keys and objects provided.
- [isEqualTo](./api-1808187-isequalto.md)
  Tests the equality of an OSDictionary to an arbitrary object.
- [isEqualTo(const OSDictionary *)](./api-1808191-isequalto.md)
  Tests the equality of two OSDictionary objects.
- [isEqualTo(const OSDictionary *, const OSCollection *)](./api-1808194-isequalto.md)
  Tests the equality of two OSDictionary objects over a subset of keys.
- [merge](./api-1808198-merge.md)
  Merges the contents of a dictionary into the receiver.
- [removeObject](./api-1808205-removeobject.md)
  Removes a key/object pair from the dictionary.
- [removeObject(const OSString *)](./api-1808207-removeobject.md)
  Removes a key/object pair from the dictionary.
- [serialize](./api-1808214-serialize.md)
  Archives the receiver into the provided OSSerialize object.
- [setCapacityIncrement](./api-1808218-setcapacityincrement.md)
  Sets the storage increment of the dictionary.
- [setObject](./api-1808220-setobject.md)
  Stores an object in the dictionary under a key.
- [setObject(const OSString *, const OSMetaClassBase *)](./api-1808224-setobject.md)
  Stores an object in the dictionary under a key.
- [setObject(const OSSymbol *, const OSMetaClassBase *)](./api-1808227-setobject.md)
  Stores an object in the dictionary under a key.
- [withCapacity](./api-1808230-withcapacity.md)
  Creates and initializes an empty OSDictionary.
- [withDictionary](./api-1808234-withdictionary.md)
  Creates and initializes an OSDictionary populated with the contents of another dictionary.
- [withObjects(const OSObject *, const OSString *, unsigned int, unsigned int)](./api-1808237-withobjects.md)
  Creates and initializes an OSDictionary populated with keys and objects provided.
- [withObjects(const OSObject *, const OSSymbol *, unsigned int, unsigned int)](./api-1808240-withobjects.md)
  Creates and initializes an OSDictionary populated with keys and objects provided.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdictionary/1808209-removeobject)*