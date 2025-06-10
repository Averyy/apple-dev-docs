# removeExportedKey(_:)

**Framework**: Core Image  
**Kind**: method

Removes a key that was previously exported.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func removeExportedKey(_ exportedKeyName: String)
```

## Parameters

- `exportedKeyName`: The name of the key you want to remove.

## See Also

- [var exportedKeys: [AnyHashable : Any]](cifiltergenerator/exportedkeys.md)
  Returns an array of the exported keys.
- [func exportKey(String, from: Any, withName: String?)](cifiltergenerator/exportkey(_:from:withname:).md)
  Exports an input or output key of an object in the filter chain.
- [func setAttributes([AnyHashable : Any], forExportedKey: String)](cifiltergenerator/setattributes(_:forexportedkey:).md)
  Sets a dictionary of attributes for an exported key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltergenerator/removeexportedkey(_:))*