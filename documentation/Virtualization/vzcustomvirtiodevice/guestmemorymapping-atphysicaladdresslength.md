# guestMemoryMapping(atPhysicalAddress:length:)

**Framework**: Virtualization  
**Kind**: method

Returns guest memory mapping referred to by physicalAddress and length.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func guestMemoryMapping(atPhysicalAddress physicalAddress: UInt64, length: Int) -> VZGuestMemoryMapping?
```

#### Return Value

A [`VZGuestMemoryMapping`](vzguestmemorymapping.md) object that contains the guest memory in the host address space, or `nil` if `physicalAddress` and `length` do not reference a valid guest RAM region.

## Parameters

- `physicalAddress`: The guest physical address of the memory.
- `length`: Length of the memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevice/guestmemorymapping(atphysicaladdress:length:))*