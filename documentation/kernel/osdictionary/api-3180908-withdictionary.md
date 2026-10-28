# withDictionary

**Framework**: Kernel  
**Kind**: clm  
**Role**: Type Method

Allocates an OSDictionary object with given members and preallocated capacity.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```c
static OSDictionaryPtr withDictionary(const OSDictionary *dictionary, uint32_t capacity);
```

*macOS*

```c
static OSPtr<OSDictionary> withDictionary(const OSDictionary *dict, unsigned int capacity);
```

## Return Value

NULL on failure, otherwise the allocated OSDictionary with reference count 1 to be released by the caller.

## Parameters

- `dictionary`: Dictionary object containing members for the new dictionary.
- `capacity`: Count of allocated capacity for members in array.

## See Also

### Creating a Dictionary
- [+ withCapacity](./api-3180907-withcapacity.md)
  Allocates an OSDictionary object with preallocated capacity.
- [+ withObjects](./api-3180909-withobjects.md)
  Allocates an OSDictionary object with given members and preallocated capacity.
- [- merge](./api-3180904-merge.md)
  Adds all members of a dictionary to this dictionary.
- [- free](./api-3180898-free.md)
- [- flushCollection](./api-3180897-flushcollection.md)
  Removes and drops references to all members of dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdictionary/3180908-withdictionary)*