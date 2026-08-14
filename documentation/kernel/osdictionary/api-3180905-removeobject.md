# removeObject

**Framework**: Kernel  
**Kind**: instm

Remove an object by key from the dictionary.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
virtual void removeObject(const OSString *aKey);
```

#### Return_value

true on success, which retains the object, or false on failure which does not retain the object.

#### Discussion

An object in the dictionary with the given key object is removed and released.

## Parameters

- `aKey`: An object pointer used to lookup the object. The key should be uniqued within the dictionary. Usually an OSString is passed as the key.

## See Also

- [- getObject](osdictionary/3180901-getobject.md)
  Returns a member of the dictionary.
- [- getObject](osdictionary/3433846-getobject.md)
  Returns a member of the dictionary.
- [- setObject](osdictionary/3180906-setobject.md)
  Add or replace an object in the dictionary.
- [- setObject](osdictionary/3433850-setobject.md)
  Add or replace an object in the dictionary.
- [- removeObject](osdictionary/3433849-removeobject.md)
  Remove an object by key from the dictionary.
- [- iterateObjects](../driverkit/osdictionary/iterateobjects-9h89s.md)
  Iterates the dictionary calling a callback block for each member.
- [- iterateObjects](../driverkit/osdictionary/iterateobjects-6cv0d.md)
  Iterates the dictionary calling a callback block for each member.
- [OSDictionaryIterateObjectsBlock](../driverkit/osdictionaryiterateobjectsblock.md)
- [OSDictionaryIterateObjectsCallback](../driverkit/osdictionaryiterateobjectscallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdictionary/3180905-removeobject)*