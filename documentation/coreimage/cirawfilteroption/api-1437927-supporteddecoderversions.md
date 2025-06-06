# supportedDecoderVersions

**Framework**: Core Image  
**Kind**: structdata

A key for the supported decoder versions. The associated value is  an [`NSArray`](https://developer.apple.com/documentation/foundation/nsarray) object that contains all supported decoder versions for the given image type, sorted in increasingly newer order. Each entry is an [`NSDictionary`](https://developer.apple.com/documentation/foundation/nsdictionary) object that contains key-value pairs. All entries represent a valid version identifier that can be passed as the `kCIDecoderVersion` value for the key `kCIDecoderMethodKey`. Version values are read-only; attempting to set this value raises an exception. Currently, the only defined key is `@"version"` which has as its value an [`NSString`](https://developer.apple.com/documentation/foundation/nsstring) that uniquely describing a given decoder version. This string might not be suitable for user interface display.. 

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.5+ - Deprecated in 12.0
- tvOS 10.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
static let supportedDecoderVersions: CIRAWFilterOption
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437927-supporteddecoderversions)*