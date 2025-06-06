# dataRepresentation

**Framework**: Virtualization  
**Kind**: property

Returns the opaque data representation of the hardware model.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var dataRepresentation: Data { get }
```

#### Discussion

You can use this to recreate the same hardware model with [`init(dataRepresentation:)`](vzmachardwaremodel/init(datarepresentation:).md).

## See Also

- [var isSupported: Bool](vzmachardwaremodel/issupported.md)
  A Boolean value that indicates whether the host supports this hardware model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmachardwaremodel/datarepresentation)*