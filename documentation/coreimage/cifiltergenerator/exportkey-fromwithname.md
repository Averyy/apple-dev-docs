# exportKey(_:from:withName:)

**Framework**: Core Image  
**Kind**: method

Exports an input or output key of an object in the filter chain.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func exportKey(_ key: String, from targetObject: Any, withName exportedKeyName: String?)
```

#### Discussion

When you create a [`CIFilter`](cifilter-swift.class.md) object from a [`CIFilterGenerator`](cifiltergenerator.md) object, you might want the filter client to be able to set some of the parameters associated with the filter chain. You can make a parameter settable by  exporting the key associated with the parameter. If the exported key represents an input parameter of the filter, the key is exported as an input key. If the key represents an output parameter, it is exported as an output key.

## Parameters

- `key`: The key to export from the target object (for example,  ).
- `targetObject`: The object associated with the key (for example, the filter).
- `exportedKeyName`: A unique name to use for the exported key. Pass   to use the original key name.

## See Also

- [var exportedKeys: [AnyHashable : Any]](cifiltergenerator/exportedkeys.md)
  Returns an array of the exported keys.
- [func removeExportedKey(String)](cifiltergenerator/removeexportedkey(_:).md)
  Removes a key that was previously exported.
- [func setAttributes([AnyHashable : Any], forExportedKey: String)](cifiltergenerator/setattributes(_:forexportedkey:).md)
  Sets a dictionary of attributes for an exported key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltergenerator/exportkey(_:from:withname:))*