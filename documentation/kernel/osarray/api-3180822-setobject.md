# setObject

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Appends an object as the last member of the array.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
bool setObject(const OSMetaClassBase *anObject);
```

*macOS*

```cpp
virtual bool setObject(const OSMetaClassBase *anObject);
```

#### Return Value

true on success, which retains the object, or false on failure which does not retain the object.

#### Discussion

Appends an object as the last member of the array. The array capacity will be grown if necessary.

## Parameters

- `anObject`: Object to be added as the last member of the array.

## See Also

### Accessing Elements
- [- getObject](./api-3180816-getobject.md)
  Returns a member of the array.
- [- getLastObject](./api-3180814-getlastobject.md)
  Returns the last member of the array.
- [- getNextIndexOfObject](./api-3180815-getnextindexofobject.md)
  Searches the array for an object.
- [- setObject](./api-3433840-setobject.md)
  Sets an object as the member of the array at a given index.
- [- iterateObjects](../../DriverKit/osarray/iterateobjects.md)
  Iterates the array calling a callback block for each member.
- [- replaceObject](./api-3180821-replaceobject.md)
  Removes a current member of the array and replaces it with another object.
- [- removeObject](./api-3180820-removeobject.md)
  Removes a current member of the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osarray/3180822-setobject)*