# merge

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Appends all members of an array to this array.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
bool merge(const OSArray *otherArray);
```

*macOS*

```cpp
virtual bool merge(const OSArray *otherArray);
```

#### Return Value

true on success, which retains all the added objects, or false on failure which does not retain the objects.

#### Discussion

Appends all members of an array to this array. The array capacity will be grown if necessary.

## Parameters

- `otherArray`: All members of thie array will be appended to the array.

## See Also

### Creating an Array
- [+ withArray](./api-3180823-witharray.md)
  Allocates an OSArray object with given members and preallocated capacity.
- [+ withCapacity](./api-3180824-withcapacity.md)
  Allocates an OSArray object with preallocated capacity.
- [+ withObjects](./api-3180825-withobjects.md)
  Allocates an OSArray object with given members and preallocated capacity.
- [- free](./api-3180811-free.md)
- [- flushCollection](./api-3180810-flushcollection.md)
  Removes and drops references to all members of array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osarray/3180819-merge)*