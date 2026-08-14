# getObject

**Framework**: Kernel  
**Kind**: instm

Returns a member of the dictionary.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
virtual OSObject * getObject(const char *aKey);
```

#### Return_value

Member at the given index or NULL if the index is greater or equal to the array count. The retain count of the result object is not incremented and the object should not be release by the caller.

#### Discussion

Looks up an existing object in the dictionary with the given key and returns it.

## Parameters

- `aKey`: A c-string key. An OSString is created from aKey and used as the key for the dictionary.

## See Also

- [- getObject](osdictionary/3180901-getobject.md)
  Returns a member of the dictionary.
- [- setObject](osdictionary/3180906-setobject.md)
  Add or replace an object in the dictionary.
- [- setObject](osdictionary/3433850-setobject.md)
  Add or replace an object in the dictionary.
- [- removeObject](osdictionary/3180905-removeobject.md)
  Remove an object by key from the dictionary.
- [- removeObject](osdictionary/3433849-removeobject.md)
  Remove an object by key from the dictionary.
- [- iterateObjects](../driverkit/osdictionary/iterateobjects-9h89s.md)
  Iterates the dictionary calling a callback block for each member.
- [- iterateObjects](../driverkit/osdictionary/iterateobjects-6cv0d.md)
  Iterates the dictionary calling a callback block for each member.
- [OSDictionaryIterateObjectsBlock](../driverkit/osdictionaryiterateobjectsblock.md)
- [OSDictionaryIterateObjectsCallback](../driverkit/osdictionaryiterateobjectscallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdictionary/3433846-getobject)*