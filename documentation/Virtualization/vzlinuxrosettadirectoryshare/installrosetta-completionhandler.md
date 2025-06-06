# installRosetta(completionHandler:)

**Framework**: Virtualization  
**Kind**: method

Starts the installation of Rosetta.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class func installRosetta() async throws
```

#### Discussion

The completion handler returns an error object that contains information about a problem, or `nil` if the installation completed successfully.

## Parameters

- `completionHandler`: The completion handler the framework invokes after the request finishes processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzlinuxrosettadirectoryshare/installrosetta(completionhandler:))*