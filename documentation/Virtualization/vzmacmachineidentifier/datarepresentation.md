# dataRepresentation

**Framework**: Virtualization  
**Kind**: property

Returns the opaque data representation of the machine identifier.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var dataRepresentation: Data { get }
```

#### Discussion

You can use this to recreate the same machine identifier with [`init(dataRepresentation:)`](vzmacmachineidentifier/init(datarepresentation:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacmachineidentifier/datarepresentation)*