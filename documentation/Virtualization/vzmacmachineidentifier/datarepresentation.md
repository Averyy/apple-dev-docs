# dataRepresentation

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

Returns the opaque data representation of the machine identifier.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var dataRepresentation: Data { get }
```

```objc
@property (copy, readonly) NSData * dataRepresentation;
```

## Discussion

You can use this to recreate the same machine identifier with [`init(dataRepresentation:)`](./init%28datarepresentation%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacmachineidentifier/datarepresentation)*