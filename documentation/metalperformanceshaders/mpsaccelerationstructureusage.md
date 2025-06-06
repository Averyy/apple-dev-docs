# MPSAccelerationStructureUsage

**Framework**: Metal Performance Shaders  
**Kind**: struct

Options that describe how an acceleration structure will be used.

**Availability**:
- iOS 12.0+ - Deprecated in 17.0
- iPadOS 12.0+ - Deprecated in 17.0
- Mac Catalyst 13.0+ - Deprecated in 17.0
- macOS 10.14+ - Deprecated in 14.0
- tvOS 12.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
struct MPSAccelerationStructureUsage
```

## Topics

### Initializers
- [init(rawValue: UInt)](mpsaccelerationstructureusage/2998476-init.md)
### Type Properties
- [static var frequentRebuild: MPSAccelerationStructureUsage](mpsaccelerationstructureusage/2980778-frequentrebuild.md)
  Option indicating that the acceleration structure will be rebuilt frequently.
- [static var preferCPUBuild: MPSAccelerationStructureUsage](mpsaccelerationstructureusage/3152575-prefercpubuild.md)
- [static var preferGPUBuild: MPSAccelerationStructureUsage](mpsaccelerationstructureusage/3152576-prefergpubuild.md)
- [static var refit: MPSAccelerationStructureUsage](mpsaccelerationstructureusage/2980780-refit.md)
  Option that enables support for refitting the acceleration structure after it has been built.

## Relationships

### Conforms To
- [OptionSet](../swift/optionset.md)
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsaccelerationstructureusage)*