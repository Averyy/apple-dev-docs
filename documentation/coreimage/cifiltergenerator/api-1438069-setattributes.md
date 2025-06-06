# setAttributes(_:forExportedKey:)

**Framework**: Core Image  
**Kind**: instm

Sets a dictionary of attributes for an exported key.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setAttributes(_ attributes: [AnyHashable : Any], forExportedKey key: String)
```

#### Discussion

By default, the exported key inherits the attributes from its original key and target object. You can use this method to change one or more of the existing attributes for the key, such as the default value or maximum value. For more information on attributes, see [`CIFilter`](cifilter.md) and [`Core Image Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185).

## Parameters

- `attributes`: A dictionary that describes the attributes associated with the specified key. 
- `key`: The exported key whose attributes you want to set.

## See Also

- [var exportedKeys: [AnyHashable : Any]](cifiltergenerator/1437955-exportedkeys.md)
  Returns an array of the exported keys.
- [func exportKey(String, from: Any, withName: String?)](cifiltergenerator/1438155-exportkey.md)
  Exports an input or output key of an object in the filter chain.
- [func removeExportedKey(String)](cifiltergenerator/1438191-removeexportedkey.md)
  Removes a key that was previously exported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438069-setattributes)*