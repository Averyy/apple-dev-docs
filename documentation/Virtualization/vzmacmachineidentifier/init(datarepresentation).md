# init(dataRepresentation:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

Create a machine identifier described by the specified data representation.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init?(dataRepresentation: Data)
```

```objc
- (instancetype) initWithDataRepresentation:(NSData *) dataRepresentation;
```

## Parameters

- `dataRepresentation`: The opaque data representation of the machine identifier.

## See Also

### Creating a machine identifier
- [init()](./init%28%29.md)
  Creates a new unique machine identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacmachineidentifier/init(datarepresentation:))*