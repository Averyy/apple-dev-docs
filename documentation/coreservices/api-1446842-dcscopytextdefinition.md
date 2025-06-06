# DCSCopyTextDefinition(_:_:_:)

**Framework**: Core Services  
**Kind**: func

Returns the definition associated with the provided text range.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func DCSCopyTextDefinition(_ dictionary: DCSDictionary?, _ textString: CFString, _ range: CFRange) -> Unmanaged<CFString>?
```

#### Return_value

The definition of the word or phrase, as plain text. The returned text does not contain any elements that are marked with a `priority` attribute whose value is `2`.

#### Discussion

This function returns the description of the first matching record found in the active dictionaries. It searches first in the default word definition dictionary which, in the English environment, is the Oxford dictionary.

## Parameters

- `dictionary`: This parameter is reserved for future use, so pass  . Dictionary Services searches in all active dictionaries.
- `textString`: Text that contains the word or phrase to look up.
- `range`: If the   parameter contains the word or phrase, but does not specify it exactly, then pass the range returned by the function  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1446842-dcscopytextdefinition)*