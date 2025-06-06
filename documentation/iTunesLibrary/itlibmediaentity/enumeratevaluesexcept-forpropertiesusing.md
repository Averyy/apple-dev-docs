# enumerateValuesExcept(forProperties:using:)

**Framework**: iTunes Library  
**Kind**: method

Executes a provided block with the fetched values for all properties in the entity except for the provided set.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
func enumerateValuesExcept(forProperties properties: Set<String>?, using block: @escaping (String, Any, UnsafeMutablePointer<ObjCBool>) -> Void)
```

#### Discussion

Use this method to get property values in a batch fashion. In some cases, enumerating over a set of property keys can be more efficient than fetching each individual property with [`value(forProperty:)`](itlibmediaentity/value(forproperty:).md).

## Parameters

- `properties`: A set of keys for the properties to enumerate, or   to enumerate all properties. Takes Media Item Properties and Playlist Properties from  .
- `block`: A block object that executes for each property in the properties set.

## See Also

- [func enumerateValues(forProperties: Set<String>?, using: (String, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](itlibmediaentity/enumeratevalues(forproperties:using:).md)
  Executes a provided block with the fetched values for the item properties.
- [func value(forProperty: String) -> Any?](itlibmediaentity/value(forproperty:).md)
  Gets the value for a specified media property key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibmediaentity/enumeratevaluesexcept(forproperties:using:))*