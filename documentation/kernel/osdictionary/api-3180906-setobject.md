# setObject

**Framework**: Kernel  
**Kind**: instm

Add or replace an object in the dictionary.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
virtual bool setObject(const OSString *aKey, const OSMetaClassBase *anObject);
```

#### Return_value

true on success, which retains the object, or false on failure which does not retain the object.

#### Discussion

The object is added to the dictionary with the key object. If an object with the given key existed prior to the call it is replaced and released. The dictionary capacity will be grown if necessary.

## Parameters

- `aKey`: An object pointer used to lookup the object. The key should be uniqued within the dictionary. Usually an OSString is passed as the key.
- `anObject`: Object to be added to the dictionary.

## See Also

- [- getObject](osdictionary/3180901-getobject.md)
  Returns a member of the dictionary.
- [- getObject](osdictionary/3433846-getobject.md)
  Returns a member of the dictionary.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdictionary/3180906-setobject)*