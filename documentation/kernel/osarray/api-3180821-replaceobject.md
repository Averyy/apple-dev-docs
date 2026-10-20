# replaceObject

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Removes a current member of the array and replaces it with another object.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
bool replaceObject(uint32_t index, const OSMetaClassBase *anObject);
```

*macOS*

```cpp
virtual void replaceObject(unsigned int index, const OSMetaClassBase *anObject);
```

#### Return Value

true on success, which retains the added object and releases the current member, or false on failure which does not retain the object and leaves the current member.

## Parameters

- `index`: Zero based index less than the array count to add the object.
- `anObject`: Object to be added to the array.

## See Also

### Accessing Elements
- [- getObject](./api-3180816-getobject.md)
  Returns a member of the array.
- [- getLastObject](./api-3180814-getlastobject.md)
  Returns the last member of the array.
- [- getNextIndexOfObject](./api-3180815-getnextindexofobject.md)
  Searches the array for an object.
- [- setObject](./api-3180822-setobject.md)
  Appends an object as the last member of the array.
- [- setObject](./api-3433840-setobject.md)
  Sets an object as the member of the array at a given index.
- [- iterateObjects](../../DriverKit/osarray/iterateobjects.md)
  Iterates the array calling a callback block for each member.
- [- removeObject](./api-3180820-removeobject.md)
  Removes a current member of the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osarray/3180821-replaceobject)*