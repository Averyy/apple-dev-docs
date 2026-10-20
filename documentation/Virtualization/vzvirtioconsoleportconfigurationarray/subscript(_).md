# subscript(_:)

**Framework**: Virtualization  
**Kind**: subscript  
**Role**: Instance Subscript

Returns the Virtio console port configuration as the specified index.

**Availability**:
- macOS 13.0+

## Declaration

```swift
subscript(portIndex: Int) -> VZVirtioConsolePortConfiguration? { get set }
```

```objc
- (VZVirtioConsolePortConfiguration *) objectAtIndexedSubscript:(NSUInteger) portIndex;
```

#### Return Value

The [`VZVirtioConsolePortConfiguration`](../vzvirtioconsoleportconfiguration.md), or nil is the index exceeds the number of configurations in the array.

## Parameters

- `portIndex`: The index of the configuration to retrieve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioconsoleportconfigurationarray/subscript(_:))*