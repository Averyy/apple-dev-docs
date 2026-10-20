# getNextIndexOfObject

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Searches the array for an object.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
uint32_t getNextIndexOfObject(const OSMetaClassBase *anObject, uint32_t index);
```

*macOS*

```cpp
virtual unsigned int getNextIndexOfObject(const OSMetaClassBase *anObject, unsigned int index);
```

#### Return Value

Index at which the object was found, or -1U if the member was not found in the array after the index parameter.

#### Discussion

Beginning at the passed index, iterate the array until the object instance is found or there are no more members. The search is done by pointer equality.

## Parameters

- `index`: Zero based index less than the array count to begin the search.

## See Also

### Accessing Elements
- [- getObject](./api-3180816-getobject.md)
  Returns a member of the array.
- [- getLastObject](./api-3180814-getlastobject.md)
  Returns the last member of the array.
- [- setObject](./api-3180822-setobject.md)
  Appends an object as the last member of the array.
- [- setObject](./api-3433840-setobject.md)
  Sets an object as the member of the array at a given index.
- [- iterateObjects](../../DriverKit/osarray/iterateobjects.md)
  Iterates the array calling a callback block for each member.
- [- replaceObject](./api-3180821-replaceobject.md)
  Removes a current member of the array and replaces it with another object.
- [- removeObject](./api-3180820-removeobject.md)
  Removes a current member of the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osarray/3180815-getnextindexofobject)*