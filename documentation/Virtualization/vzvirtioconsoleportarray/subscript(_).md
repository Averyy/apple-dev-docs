# subscript(_:)

**Framework**: Virtualization  
**Kind**: subscript  
**Role**: Instance Subscript

Returns the Virtio console port at the specified index.

**Availability**:
- macOS 13.0+

## Declaration

```swift
subscript(portIndex: Int) -> VZVirtioConsolePort? { get }
```

```objc
- (VZVirtioConsolePort *) objectAtIndexedSubscript:(NSUInteger) portIndex;
```

#### Return Value

A [`VZVirtioConsolePort`](../vzvirtioconsoleport.md) port, or `nil` if the index is outside the bounds of the array.

## Parameters

- `portIndex`: The index of the port to return, if present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioconsoleportarray/subscript(_:))*