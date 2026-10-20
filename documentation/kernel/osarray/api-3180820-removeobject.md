# removeObject

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Removes a current member of the array.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
void removeObject(uint32_t index);
```

*macOS*

```cpp
virtual void removeObject(unsigned int index);
```

#### Discussion

Removes a current member of the array, shifting down all following members. The removed object is released.

## Parameters

- `index`: Zero based index less than the array count of the object to remove.

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
- [- replaceObject](./api-3180821-replaceobject.md)
  Removes a current member of the array and replaces it with another object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osarray/3180820-removeobject)*