# setCachingOptions(_:)

**Framework**: Virtualization  
**Kind**: method

Sets the Rosetta caching options using the options you specify.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func setCachingOptions(_ cachingOptions: VZLinuxRosettaDirectoryShare.CachingOptions?) throws
```

## Mentions

- [Running Intel Binaries in Linux VMs](running-intel-binaries-in-linux-vms.md)

## Parameters

- `cachingOptions`: One of the available [`VZLinuxRosettaDirectoryShare.CachingOptions`](vzlinuxrosettadirectoryshare/cachingoptions-swift.enum.md).

## See Also

- [var cachingOptions: VZLinuxRosettaDirectoryShare.CachingOptions?](vzlinuxrosettadirectoryshare/cachingoptions-swift.property.md)
  The value that enables translation caching and configures the socket communication type for Rosetta.
- [VZLinuxRosettaDirectoryShare.CachingOptions](vzlinuxrosettadirectoryshare/cachingoptions-swift.enum.md)
  Socket values you specify to configure Rosetta’s caching capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzlinuxrosettadirectoryshare/setcachingoptions(_:))*