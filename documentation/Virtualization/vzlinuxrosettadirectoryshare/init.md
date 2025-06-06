# init()

**Framework**: Virtualization  
**Kind**: init

Creates a new Rosetta directory share, or returns an error if Rosetta isn’t installed.

**Availability**:
- macOS 13.0+

## Declaration

```swift
init() throws
```

#### Discussion

Check the status of Rosetta by examining the [`availability`](vzlinuxrosettadirectoryshare/availability.md) class property before creating a new Rosetta directory share to ensure the capability is both supported and available on host Mac. For complete instructions on installing Rosetta see [`Running Intel Binaries in Linux VMs with Rosetta`](running-intel-binaries-in-linux-vms-with-rosetta.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzlinuxrosettadirectoryshare/init())*