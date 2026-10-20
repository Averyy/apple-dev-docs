# init(dataRepresentation:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

Creates a new unique identifier for a VM with the provided data.

**Availability**:
- macOS 13.0+

## Declaration

```swift
init?(dataRepresentation: Data)
```

```objc
- (instancetype) initWithDataRepresentation:(NSData *) dataRepresentation;
```

## Parameters

- `dataRepresentation`: A data object that describes the machine identifier.

## See Also

### Creating a Machine Identifier
- [init()](./init%28%29.md)
  Creates a new unique identifier for a VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzgenericmachineidentifier/init(datarepresentation:))*