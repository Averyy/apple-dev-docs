# UTTypeCreatePreferredIdentifierForTag(_:_:_:)

**Framework**: Core Services  
**Kind**: func

Creates a uniform type identifier for the type indicated by the specified tag.

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
func UTTypeCreatePreferredIdentifierForTag(_ inTagClass: CFString, _ inTag: CFString, _ inConformingToUTI: CFString?) -> Unmanaged<CFString>?
```

#### Return_value

A new CFStringRef containing a uniform type identifier, or `NULL` if inTagClass is not a known tag class

#### Discussion

This function is used to translate a type declared using another declaration mechanism (for example, MIME types) into a uniform type identifier. This function searches all UTI declarations for a matching translation. If a conforming parameter is assigned, the search is reduced to the subset of type identifiers that conform to that type.

If there is more than one possible UTI for the specified tag, the UTI that will be returned is undefined. See [`UTTypeCreateAllIdentifiersForTag(_:_:_:)`](1447261-uttypecreateallidentifiersfortag.md) if you need to see all search results.

If no result is found, this function creates a dynamic type beginning with the `dyn` prefix. This allows you to pass the UTI around and convert it back to the original tag.

## Parameters

- `inTagClass`: The class of the   parameter. For more information, see  .
- `inTag`: The tag to translate into a uniform type identifier.
- `inConformingToUTI`: If not  , the returned uniform type identifier must conform to this parameter.

## See Also

- [func UTTypeCopyPreferredTagWithClass(CFString, CFString) -> Unmanaged<CFString>?](1442744-uttypecopypreferredtagwithclass.md)
  Translates a uniform type identifier to a list of tags in a different type classification method.
- [Uniform Type Identifiers Overview](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_intro/understand_utis_intro.html#//apple_ref/doc/uid/TP40001319)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1448939-uttypecreatepreferredidentifierf)*