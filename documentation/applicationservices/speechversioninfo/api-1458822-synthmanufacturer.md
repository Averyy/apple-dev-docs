# synthManufacturer

**Framework**: Application Services  
**Kind**: structp

A unique identification of a synthesizer engine. If you develop synthesizers, then you should register a different four-character code for each synthesizer you develop with Developer Technical Support. The `creatorID` field of the voice specification structure and the `synthCreator` field of a speech extension data structure should each be set to the value stored in this field for the desired synthesizer.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var synthManufacturer: OSType
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/speechversioninfo/1458822-synthmanufacturer)*