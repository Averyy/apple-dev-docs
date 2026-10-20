# withCapacity

**Framework**: Kernel  
**Kind**: clm  
**Role**: Type Method

Allocates an OSDictionary object with preallocated capacity.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```c
static OSDictionaryPtr withCapacity(uint32_t capacity);
```

*macOS*

```c
static OSPtr<OSDictionary> withCapacity(unsigned int capacity);
```

#### Return Value

NULL on failure, otherwise the allocated OSDictionary with reference count 1 to be released by the caller.

## Parameters

- `capacity`: Count of allocated capacity for members in dictionary.

## See Also

### Creating a Dictionary
- [+ withDictionary](./api-3180908-withdictionary.md)
  Allocates an OSDictionary object with given members and preallocated capacity.
- [+ withObjects](./api-3180909-withobjects.md)
  Allocates an OSDictionary object with given members and preallocated capacity.
- [- merge](./api-3180904-merge.md)
  Adds all members of a dictionary to this dictionary.
- [- free](./api-3180898-free.md)
- [- flushCollection](./api-3180897-flushcollection.md)
  Removes and drops references to all members of dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdictionary/3180907-withcapacity)*