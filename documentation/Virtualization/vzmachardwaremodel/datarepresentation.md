# dataRepresentation

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

Returns the opaque data representation of the hardware model.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var dataRepresentation: Data { get }
```

```objc
@property (copy, readonly) NSData * dataRepresentation;
```

#### Discussion

You can use this to recreate the same hardware model with [`init(dataRepresentation:)`](./init%28datarepresentation%29.md).

## See Also

### Configuring the hardware model
- [var isSupported: Bool](./issupported.md)
  A Boolean value that indicates whether the host supports this hardware model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmachardwaremodel/datarepresentation)*