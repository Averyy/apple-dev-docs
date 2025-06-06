# UTTypeCopyPreferredTagWithClass(_:_:)

**Framework**: Core Services  
**Kind**: func

Translates a uniform type identifier to a list of tags in a different type classification method.

**Availability**:
- iOS 3.0+ - Deprecated in 15.0
- iPadOS 3.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.3+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 8.0

## Declaration

```swift
func UTTypeCopyPreferredTagWithClass(_ inUTI: CFString, _ inTagClass: CFString) -> Unmanaged<CFString>?
```

#### Return_value

An array of tags (as CFStrings), or `NULL` if there was no translation available to convert the uniform type identifier to the specified class.

#### Discussion

If the type declaration included more than one tag with the specified class, the first tag in the declared tag array is the preferred tag.

## Parameters

- `inUTI`: The uniform type identifier to convert.
- `inTagClass`: The class of the tags you want to return. For more information, see  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1442744-uttypecopypreferredtagwithclass)*