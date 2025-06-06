# UTTypeCreateAllIdentifiersForTag(_:_:_:)

**Framework**: Core Services  
**Kind**: func

Creates an array of all uniform type identifiers for the type indicated by the specified tag.

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
func UTTypeCreateAllIdentifiersForTag(_ inTagClass: CFString, _ inTag: CFString, _ inConformingToUTI: CFString?) -> Unmanaged<CFArray>?
```

#### Return_value

An array of uniform type identifiers, or `NULL` if inTagClass is not a known tag class

#### Discussion

This function is used to translate a type declared using another declaration mechanism (for example, MIME types) into a uniform type identifier. This function searches all UTI declarations for a matching translation and returns all possible results. If a conforming parameter is assigned, the search is reduced to the subset of type identifiers that conform to that type.

If no result is found, this function creates a dynamic type beginning with the `dyn` prefix.

## Parameters

- `inTagClass`: The class of the   parameter. For more information, see  .
- `inTag`: The tag to translate into a uniform type identifier.
- `inConformingToUTI`: If not  , all returned uniform type identifiers must conform to this parameter.

## See Also

- [func UTTypeCopyPreferredTagWithClass(CFString, CFString) -> Unmanaged<CFString>?](1442744-uttypecopypreferredtagwithclass.md)
  Translates a uniform type identifier to a list of tags in a different type classification method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447261-uttypecreateallidentifiersfortag)*