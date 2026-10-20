# withObjects

**Framework**: Kernel  
**Kind**: clm  
**Role**: Type Method

Allocates an OSArray object with given members and preallocated capacity.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```c
static OSArrayPtr withObjects(const OSObject **values, uint32_t count, uint32_t capacity);
```

*macOS*

```c
static OSPtr<OSArray> withObjects(const OSObject *objects[], unsigned int count, unsigned int capacity);
```

#### Return Value

NULL on failure, otherwise the allocated OSArray with reference count 1 to be released by the caller.

## Parameters

- `values`: C-array pointer to members for the array.
- `count`: Count of members being added to the array.
- `capacity`: Count of allocated capacity for members in array.

## See Also

### Creating an Array
- [+ withArray](./api-3180823-witharray.md)
  Allocates an OSArray object with given members and preallocated capacity.
- [+ withCapacity](./api-3180824-withcapacity.md)
  Allocates an OSArray object with preallocated capacity.
- [- merge](./api-3180819-merge.md)
  Appends all members of an array to this array.
- [- free](./api-3180811-free.md)
- [- flushCollection](./api-3180810-flushcollection.md)
  Removes and drops references to all members of array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osarray/3180825-withobjects)*