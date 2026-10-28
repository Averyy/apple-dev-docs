# merge

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Adds all members of a dictionary to this dictionary.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
bool merge(const OSDictionary *otherDictionary);
```

*macOS*

```cpp
virtual bool merge(const OSDictionary *aDictionary);
```

## Return Value

true on success, which retains all the added objects, or false on failure which does not retain the objects.

## Discussion

Adds all members of a dictionary to this dictionary. Any keys in the dictionary that exist will be replaced. The dictionary capacity will be grown if necessary.

## Parameters

- `otherDictionary`: All members of thie dictionary will be added to the array.

## See Also

### Creating a Dictionary
- [+ withCapacity](./api-3180907-withcapacity.md)
  Allocates an OSDictionary object with preallocated capacity.
- [+ withDictionary](./api-3180908-withdictionary.md)
  Allocates an OSDictionary object with given members and preallocated capacity.
- [+ withObjects](./api-3180909-withobjects.md)
  Allocates an OSDictionary object with given members and preallocated capacity.
- [- free](./api-3180898-free.md)
- [- flushCollection](./api-3180897-flushcollection.md)
  Removes and drops references to all members of dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdictionary/3180904-merge)*