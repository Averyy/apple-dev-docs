# disableSecureBoot()

**Framework**: Virtualization  
**Kind**: method

Disables Secure Boot while preserving the existing configuration.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func disableSecureBoot() throws
```

#### Discussion

**Swift**:

```swift
 do {
     try variableStore.disableSecureBoot()
 } catch {
     // Handle error.
 }
```

**Objective-C**:

```objc
 NSError *error;
 if (![variableStore disableSecureBootWithError:&error]) {
     // Handle error.
 }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefivariablestore/disablesecureboot())*