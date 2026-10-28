# getObject

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Returns a member of the array.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
OSObject * getObject(uint32_t index);
```

*macOS*

```cpp
virtual OSObject * getObject(unsigned int index);
```

## Return Value

Member at the given index or NULL if the index is greater or equal to the array count. The retain count of the result object is not incremented and the object should not be release by the caller.

## Discussion

If the index is less than the array count the member at that index is returned, with no additional retain count (the caller should not release). Otherwise NULL.

## Parameters

- `index`: Zero based index less than the array count to add the object.

## See Also

### Accessing Elements
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
- [- removeObject](./api-3180820-removeobject.md)
  Removes a current member of the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osarray/3180816-getobject)*