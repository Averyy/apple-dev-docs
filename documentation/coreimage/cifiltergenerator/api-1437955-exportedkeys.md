# exportedKeys

**Framework**: Core Image  
**Kind**: instp

Returns an array of the exported keys.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var exportedKeys: [AnyHashable : Any] { get }
```

#### Return_value

An array of dictionaries that describe the exported key and target object. See [`kCIFilterGeneratorExportedKey`](kcifiltergeneratorexportedkey.md), [`kCIFilterGeneratorExportedKeyTargetObject`](kcifiltergeneratorexportedkeytargetobject.md),  and [`kCIFilterGeneratorExportedKey`](kcifiltergeneratorexportedkey.md) for keys used in the dictionary.

#### Discussion

This method returns the keys that you exported using the [`exportKey(_:from:withName:)`](cifiltergenerator/1438155-exportkey.md) method or that were exported before being written to the file from which you read the filter chain.

## See Also

- [func exportKey(String, from: Any, withName: String?)](cifiltergenerator/1438155-exportkey.md)
  Exports an input or output key of an object in the filter chain.
- [func removeExportedKey(String)](cifiltergenerator/1438191-removeexportedkey.md)
  Removes a key that was previously exported.
- [func setAttributes([AnyHashable : Any], forExportedKey: String)](cifiltergenerator/1438069-setattributes.md)
  Sets a dictionary of attributes for an exported key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1437955-exportedkeys)*