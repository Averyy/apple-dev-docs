# init(kernelURL:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

Creates a boot loader that launches the Linux kernel at the specified URL.

**Availability**:
- macOS 11.0+

## Declaration

```swift
init(kernelURL: URL)
```

```objc
- (instancetype) initWithKernelURL:(NSURL *) kernelURL;
```

## Return Value

A boot loader object for the specified Linux kernel.

## Parameters

- `kernelURL`: The location of a Linux kernel on the local file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzlinuxbootloader/init(kernelurl:))*